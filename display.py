import curses
import sys
import time
from select import select

import config
import timer
from save import Save
from user_interface import UserInterface


class Feeder:
    def __init__(self, task):
        self.running = False
        self.ui = UserInterface()
        self.task = task
        self.first_start = time.time()
        self.start = time.time()
        self.recorded_time = 0
        self.paused = False

    def run(self):
        self.running = True
        self.ui.win.addstr(11, 1, f"Task: ")
        self.ui.win.addstr(11, 7, f"{self.task}", curses.color_pair(2))
        self.feed()

    def quit(self):
        self.running = False
        self.ui.quit_ui()
        if self.paused:
            self.start = time.time() + 1
        task = f" in {self.task}" if self.task != "None" else ""
        exit(f"Time{task}: {timer.get_time_string(self.start, self.recorded_time)}")

    def feed(self):
        try:
            while self.running:
                while sys.stdin in select([sys.stdin], [], [], 0)[0]:
                    line = sys.stdin.read(1)
                    if line.strip().lower() == "q":
                        if config.autosave_q:
                            save = Save(
                                self.first_start,
                                self.paused,
                                self.recorded_time,
                                self.start,
                                self.task
                            )
                            save.save_to_csv()
                        self.quit()
                        break
                    elif line.strip().lower() == "p":
                        if self.paused:
                            self.start = time.time()
                            self.ui.win.addstr(14, 29, "          ")
                            self.paused = False
                        else:
                            self.recorded_time = timer.compute_time(
                                self.start,
                                self.recorded_time
                            )
                            self.ui.win.addstr(14, 29, "**PAUSED**", curses.color_pair(1))
                            self.paused = True
                    elif line.strip().lower() == "s":
                        save = Save(
                            self.first_start,
                            self.paused,
                            self.recorded_time,
                            self.start,
                            self.task
                        )
                        save.save_to_csv()
                if not self.paused:
                    self.ui.win.addstr(
                        9,
                        33,
                        timer.get_time_string(self.start, self.recorded_time),
                        curses.A_BOLD
                    )
                if not config.autosave_delay == 0:
                    if int(time.time()) != int(self.start):
                        if (int(time.time()) - int(self.start)) % config.autosave_delay == 0:
                            save = Save(
                                self.first_start,
                                self.paused,
                                self.recorded_time,
                                self.start,
                                self.task
                            )
                            save.save_to_csv()

                self.ui.refresh()
                time.sleep(0.1)
        except KeyboardInterrupt:
            if config.autosave_c:
                save = Save(
                    self.first_start,
                    self.paused,
                    self.recorded_time,
                    self.start,
                    self.task
                )
                save.save_to_csv()
            self.quit()


if __name__ == "__main__":
    feeder = Feeder(time.time())
    feeder.run()
