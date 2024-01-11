import asyncio
import tello_asyncio
from tello_asyncio import Tello, MissionPadDetection, Vector

tello_asyncio.DEFAULT_RESPONSE_TIMEOUT = 30


async def main():
    drone = Tello(on_state=on_drone_state)
    try:
        await drone.connect()
        await drone.takeoff()
        await drone.enable_mission_pads()

        await drone.move_up(50)
        while drone.mission_pad != 4:
            await drone.move_forward(50)
            await asyncio.sleep(2)

        await drone.go_to(relative_position=Vector(0, 0, 60), speed=20, mission_pad=4)
        await drone.turn_clockwise(360)

        await drone.land()
    finally:
        await drone.disconnect()


def on_drone_state(drone, state):
    if state.mission_pad == -1:
        print(f"(b: {state.battery}%) I don't see a mission pad")
    else:
        print(f"(b: {state.battery}%) I see mission pad: {state.mission_pad}, " +
              f"I'm in position: (x: {state.mission_pad_position.x}, " +
              f"y: {state.mission_pad_position.y}, z:{state.mission_pad_position.z})")

    drone.mission_pad = state.mission_pad
    drone.mission_pad_position = state.mission_pad_position


asyncio.run(main())
