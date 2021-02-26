from soundboard import LaunchpadMk2

class Soundboard:
    def __init__(self):
        self.n = int(input("Please choose a number of wrong pads: "))
        self.lp = LaunchpadMk2.LaunchpadMk2()
        self.lp.Reset()
        self.lp.register_on_button_press(on_button=self.on_button_press)
        self.add_sound()

    def add_sound(self):
        p = input("Please enter the path to you´re yound file and don´t delete it after that: ")

    def on_button_press(self, x, y, pres):
        pass



if __name__ == "__main__":
    Soundboard()
