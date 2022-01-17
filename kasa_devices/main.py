import asyncio
from kasa import SmartPlug
from kasa import Discover

devices = asyncio.run(Discover.discover())
for addr, dev in devices.items():
    asyncio.run(dev.update())
    print(f"{addr} >> {dev}")


async def main():
    p = SmartPlug("192.168.10.101")

    await p.update()
    print(p.alias)

    await p.turn_off()


if __name__ == "__main__":
    asyncio.run(main())
