import os
import threading
from os import path, sep
from dataclasses import dataclass

from google.protobuf.message import Message

from MihoyoNetSniffer.packet import GameNetwork, Thread, Direction
from MihoyoNetSniffer.protbuf_parser import ProtobufParser
from datetime import datetime
from MihoyoNetSniffer.ParsedPacket import ParsedPacket
from google.protobuf.json_format import MessageToJson



class Sniffer:
    def __init__(self, pipe_name='genshin_packet_pipe', dump_file: str = None):
        cmdid_path = path.dirname(path.abspath(__file__)) + sep + 'cmdid.csv'
        self.socket_client = GameNetwork(pipe_name, dump_file)
        self.protobuf_parser = ProtobufParser(cmdid_path)
        self.handle = {}
        self.process_loop = Thread(target=self._packet_process_loop)
        self.packets = []
        self.banned_packets: list[str] = []
        self.whitelisted_packets: list[str] = []

    def add_handle(self, packet_name, func):
        packet_id = self.protobuf_parser.cmd_name_map[packet_name]
        old_handles = self.handle.get(packet_id, None)
        if old_handles:
            old_handles.append(func)
            return
        self.handle[packet_id] = [func]

    def add_to_blacklist(self, packet_name):
        self.banned_packets.append(packet_name)

    def add_to_whitelist(self, packet_name):
        self.whitelisted_packets.append(packet_name)

    def start(self):
        self.socket_client.start()
        self.process_loop.start()

    def stop(self):
        self.socket_client.stop()
        self.process_loop.join()

    def load_from_file(self, file_path):
        def yield_wrapper():
            return next(iter_obj, None)

        from MihoyoNetSniffer.packet import load_from_dump
        with open(file_path, 'rb') as f:
            iter_obj = load_from_dump(f)
            self._packet_process_loop(load_from_dump(yield_wrapper))

    def _packet_process_loop(self, override_func=None):
        if override_func:
            get_packet = override_func
        else:
            get_packet = self.socket_client.get_packet
        i = 0
        while True:
            raw_packet = get_packet()
            if raw_packet is None:
                return
            if self.protobuf_parser.get_packet_name(raw_packet.message_id) in self.banned_packets:
                del raw_packet
                continue
            if len(self.whitelisted_packets) > 0 and self.protobuf_parser.get_packet_name(
                    raw_packet.message_id) not in self.whitelisted_packets:
                del raw_packet
                continue
            i += 1
            packet = ParsedPacket(
                raw_packet.time_stamp, raw_packet.direction,
                self.protobuf_parser.get_packet_name(raw_packet.message_id),
                *self.protobuf_parser.parse_raw_packet(raw_packet)
            )
            time = datetime.now().strftime("%H-%M-%S")
            print("dumping", i, time, self.protobuf_parser.get_packet_name(raw_packet.message_id))
            if not path.exists(".\\dumped"):
                os.mkdir(".\\dumped")
            with open(f'.\\dumped\\{i} {time} {self.protobuf_parser.get_packet_name(raw_packet.message_id)}.json',
                      "w") as f:
                data = MessageToJson(packet.content)
                f.write(data)
            count = len(self.packets)
            self.packets.append(packet)
            handles = self.handle.get(raw_packet.message_id, None)
            del raw_packet
            if not handles:
                continue
            for handle in handles:
                handle(count, packet)  # 到底要不要多线程呢
