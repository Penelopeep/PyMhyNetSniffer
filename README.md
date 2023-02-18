# PyMhyNetSniffer
a packet sniffer used with Akebi-GC

I'll try to keep it updated and maybe I'll add more functions some time.
For now, it's base + writting to file + blacklist/whitelist

Right now protos are set for 3.4

How to use:
- install python 3.something, I personally used 3.10.4
- install pip if you don't have it (windows should have it by default)
- open terminal and use `pip install -r requirements.txt` to install the required modules
- edit `test.py` to add/remove blacklisted/whitelisted packets
- run the script with `python test.py` or `python3 test.py` if you have multiple python versions installed

Credits:
- [Akebi-GC](https://discord.gg/akebi) - for the base
- [Acrepi](https://discord.gg/acrepi) - #ripfreeakebi3.4
- [Bkebi](https://discord.gg/bkebi) - cos it apparently exists
- BUnipendix for [original sniffer](https://github.com/BUnipendix/PyMhyNetSniffer)
- Hiro for [protos](https://github.com/NickTheHuy/3.4_proto)