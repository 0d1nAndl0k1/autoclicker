import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# delay is the how often to it clicks in a milla sec .75 is about 10cps
# Start/stop key is the key you use to start the auto clicker it can be anything but i just used x
# Exit key is the key you use to complety close the script so if you use this for a game you wouldn't want it to be a essential button that why its -
delay = 0.075
button = Button.left
start_stop_key = KeyCode(char='x')
exit_key = KeyCode(char='-')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
