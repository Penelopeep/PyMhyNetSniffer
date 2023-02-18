from MihoyoNetSniffer.sniffer import Sniffer

a = Sniffer()

# Blacklisted packets, add/remove a command to add to this list, remember to remove "#"
#a.add_to_blacklist('PlayerMoveReq')
#a.add_to_blacklist('PingReq')
#a.add_to_blacklist('PingRsp')

# Whitelisted packets, add/remove a command to add to this list, remember to remove "#"
#a.add_to_whitelist('PlayerMoveReq')
#a.add_to_whitelist('PingReq')
#a.add_to_whitelist('PingRsp')

a.start()
try:
    a.process_loop.join()
except KeyboardInterrupt:
    pass
finally:
    a.stop()
