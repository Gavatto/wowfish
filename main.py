import time
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
from threading import Thread

class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.fishing_thread = None

        self.curv_img = None
        self.curv_imgHSV = None

        self.zone = "Feralas"
        self.time = "night"

        print("Main Agent is running")

def update_screen(agent):
    t0 = time.time()
    while True:
        agent.curv_img = ImageGrab.grab()
        agent.curv_img = np.array(agent.curv_img)
        agent.curv_img = cv.cvtColor(agent.curv_img, cv.COLOR_RGB2BGR)

        cv.imshow("Computer Vision", agent.curv_img)
        key = cv.waitKey(1)
        if key == ord("q"):
            break
        ex_time = time.time() - t0
        print(f"FPS: " + str(1/ex_time))
        t0 = time.time()

if __name__ == "__main__":
    main_agent = MainAgent()

    update_screen_thread = Thread(target=update_screen, args=(main_agent, ), name="UpdateScreenThread", daemon=False)
    update_screen_thread.start()
