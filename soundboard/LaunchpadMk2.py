import atexit
import time
from threading import Thread
from launchpad_py import LaunchpadMk2 as LpMk2


class LaunchpadMk2(LpMk2):
    on_finish = []
    on_button = []

    continue_listener = True
    listener_thread: Thread = None

    def __init__(self, number=0):
        super().__init__()
        self.Open(number, name="Mk2")
        atexit.register(self.__on_exit__)
        self.continue_listener = True
        self.listener_thread = Thread(target=self.__start_listener__)
        self.listener_thread.setName("Launchpad Mk2")
        self.listener_thread.start()

    def __on_exit__(self):
        time.sleep(5)
        if super().Check(0):
            self.Reset()
            self.Close()

    def __start_listener__(self):
        sTime = time.time()
        self.continue_listener = True
        while self.continue_listener:
            btns = self.ButtonStateXY()
            if btns:
                for event in self.on_button:
                    event(btns[0], btns[1], btns[2])
        for finisher in self.on_finish:
            finisher(sTime - time.time())

    def register_on_button_press(self, on_button: callable, on_finish=lambda t: print("Finished!")):
        self.on_button.append(on_button)
        self.on_finish.append(on_finish)