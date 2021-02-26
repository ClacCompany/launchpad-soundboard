from playsound import playsound
from threading import Thread
import Launchpad
import glob
import os

lpmode = open("launchpad", "r").read()
if len(lpmode) > 0:
    LAUNCHPAD = lpmode
else:
    LAUNCHPAD = input("Please enter your Launchpad: ")
    open("launchpad", "w").write(LAUNCHPAD)


class Soundboard:
    def __init__(self):
        s0 = {
            "pro": Launchpad.LaunchpadPro,
            "mk2": Launchpad.LaunchpadMk2
        }
        self.lp = s0.get(LAUNCHPAD.lower(), Launchpad.LaunchpadMk2)()
        self.lp.Reset()
        self.lp.ButtonStateRaw()
        self.sounds = []
        self.buttons = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                        (1, 6), (1, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 1), (3, 2), (3, 3),
                        (3, 4), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 1),
                        (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
                        (6, 7), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        self.lp.LedAllOn()
        self.lp.register_on_button_press(on_button=self.on_button_press)
        self.lp.continue_listener = True
        self.init_sounds()

    def init_sounds(self):
        os.chdir("sounds")
        for file in glob.glob("*.mp3"):
            self.sounds.append(file)
        for file in glob.glob("*.wav"):
            self.sounds.append(file)
        while True:
            pass

    def on_button_press(self, x, y, pres):
        if pres > 0 and self.sounds:
            if (x, y) in self.buttons:
                i = self.buttons.index((x, y))
                try:
                    Thread(target=playsound, args=(self.sounds[i],)).start()
                except IndexError:
                    print("This button is not defined")


if __name__ == "__main__":
    Soundboard()
