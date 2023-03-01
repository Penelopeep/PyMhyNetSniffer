from dataclasses import dataclass

from google.protobuf.message import Message
from MihoyoNetSniffer.packet import Direction


@dataclass
class ParsedPacket:
    time_stamp: int
    direction: Direction
    packet_name: str
    header: Message
    content: Message