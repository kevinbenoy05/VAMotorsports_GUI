from sx126x.SX126X import SX126X
from time import sleep
from asyncio import run
import datetime

TIMEOUT = 60  # 1 minute timeout

SLP = 0.05  # 50ms tick


async def main():
    node = SX126X("/dev/ttyUSB0")
    tx, rx, freq, data = await node.receive()
    # create file
    now = datetime.now()
    file_name = str(now)
    f = open(f"logs/{file_name}", "w")  # it should be ok to not f.close()
    while True:
        tx, rx, freq, data = await node.receive()
        if data:
            f.write(f"{data}\n")
            print(tx, rx, freq, data)  # debugging
        sleep(SLP)


if __name__ == "__main__":
    run(main())
