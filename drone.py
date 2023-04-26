import asyncio
from tello_asyncio import Tello

async def main():
    drone = Tello()
    try:
        await drone.wifi_wait_for_network(prefix="RMTT")
        await drone.connect()
        await drone.takeoff()
        await drone.turn_clockwise(360)
        await drone.land()
    finally:
        await drone.disconnect()

asyncio.run(main())