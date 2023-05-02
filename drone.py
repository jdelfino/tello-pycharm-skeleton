import asyncio
import tello_asyncio
from tello_asyncio import Tello, MissionPadDetection, Vector
tello_asyncio.DEFAULT_RESPONSE_TIMEOUT=30

async def main():
    drone = Tello(on_state=on_drone_state)
    try:
        await drone.connect()
        await drone.takeoff()
        await drone.enable_mission_pads()
        await drone.set_mission_pad_detection(MissionPadDetection.DOWN)

        await drone.move_up(50)
        await drone.move_forward(100)
        await asyncio.sleep(5) # Pauses for 5 seconds
        await drone.go_to(Vector(0, 0, 40), 20, 4)
        await asyncio.sleep(5)

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