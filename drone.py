import asyncio
import tello_asyncio
from tello_asyncio import Tello, MissionPadDetection, Vector
tello_asyncio.DEFAULT_RESPONSE_TIMEOUT=30

async def main():
    drone = Tello()
    try:
        await drone.connect()

        # Command syntax reference here: https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf
        # "mled s [color: r or b or p] [letter]" -> display the given letter in the given color (red/blue/purple)
        # example: This line shows the letter "q" in blue
        await drone.send_ext_command("mled s b q")

        # "mled g [sequence of 0/r/b/p]" -> set each pixel of the display to off (0), red (r), blue (b) or purple (p)
        # example: This sets the screen to have 1 blank line, 1 red line, 1 blue line, 2 purple lines, 1 blue line, 1 red line, and one blank line
        await drone.send_ext_command("mled g 00000000rrrrrrrrbbbbbbbbppppppppppppppppbbbbbbbbrrrrrrrr00000000")

        # "mled [scroll direction: l or r or u or d] [color: r or b or p] [speed: 0.1 - 2.5] [words]" ->
        #    display the words shown, and scroll them in the given direction with the given speed
        # example: This shows the words "hi innovation lab!" in red, and they scroll up quickly
        await drone.send_ext_command("mled u r 2.5 hi innovation lab!")
        await asyncio.sleep(10)
    finally:
        await drone.disconnect()

asyncio.run(main())