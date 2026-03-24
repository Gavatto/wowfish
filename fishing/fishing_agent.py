

import cv2 as cv
import numpy as np
import pyautogui
import time

class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("")
        self.fishing_thread = None

    def cast_lure(self):
        print("Casting...")
        pyautogui.press("1")
        time.sleep(2)
        self.find_lure()


    def find_lure(self):
        pass

    def move_to_lure(self):
        pass

    def watch_lure(self):
        pass

    def pull_line(self):
        pass

    def run(self):
        pass
