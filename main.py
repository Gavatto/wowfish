import time
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
from threading import Thread

class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.fishing_thread = None

        self.curv_img = None #BGR image
        self.curv_imgHSV = None #HSV image

        self.zone = "Feralas"
        self.time = "night"

        #print("Main Agent is running")

def update_screen(agent):
    t0 = time.time()
    while True:
        agent.curv_img = ImageGrab.grab()
        agent.curv_img = np.array(agent.curv_img)
        agent.curv_img = cv.cvtColor(agent.curv_img, cv.COLOR_RGB2BGR)
        agent.curv_imgHSV = cv.cvtColor(agent.curv_img, cv.COLOR_BGR2HSV)

        cv.imshow("Computer Vision", agent.curv_img)
        cv.imshow("Computer Vision - HSV", agent.curv_imgHSV)
        key = cv.waitKey(1)
        if key == ord("q"):
            break
        ex_time = time.time() - t0
        print(f"FPS: " + str(1/ex_time))
        t0 = time.time()


def print_menu():
    print("Enter a command:")
    print("\tS\tStart the main agent")
    print("\tZ\tSet the zone")
    print("\tF\tStart fishing")
    print("\tQ\tQuit")

if __name__ == "__main__":
    main_agent = MainAgent()

    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            update_screen_thread = Thread(target=update_screen, args=(main_agent,), name="UpdateScreenThread", daemon=True)
            update_screen_thread.start()
            print("Thread started")
        elif user_input == "z":
            pass
        elif user_input == "f":
            pass
        elif user_input == "q":
            cv.destroyAllWindows()
            break
        else:
            print("Invalid command")
            print_menu()
            
    print("Quitting...")
