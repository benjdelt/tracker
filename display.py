import curses
import curses.panel
import sys
from select import select
from time import sleep, time

import timer


class UserInterface:
    def __init__(self, start):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)

        self.win = curses.newwin(20, 70, 0, 0)
        self.win.border(0)

        self.win.addstr(1, 30, "Tracker")
        self.win.addstr(2, 30, "=======")
        self.win.addstr(4, 1, "Press 'p' to pause/unpause or 'q' to quit.")

        self.start = start

    def refresh(self):
        curses.panel.update_panels()
        self.win.refresh()

    def quit_ui(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.curs_set(1)
        curses.echo()
        curses.endwin()
        exit(f"Time: {timer.get_time(self.start)}\n")


class Feeder:
    def __init__(self, start):
        self.running = False
        self.ui = UserInterface(start)
        self.start = start
        self.recorded_time = 0
        self.paused = False

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        self.feed()

    def feed(self):
        try:
            while self.running:
                while sys.stdin in select([sys.stdin], [], [], 0)[0]:
                    line = sys.stdin.read(1)
                    if line.strip() == "q":
                        self.stop()
                        self.ui.quit_ui()
                        break
                    elif line.strip() == "p":
                        if not self.paused:
                            self.recorded_time = timer.pause(self.start, self.recorded_time)
                            self.paused = True
                        else:
                            self.start = time()
                            self.paused = False
                        
                if not self.paused:
                    self.ui.win.addstr(9, 33, timer.get_time(self.start, self.recorded_time))
                self.ui.refresh()
                sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
            self.ui.quit_ui()


if __name__ == "__main__":
    feeder = Feeder(time())
    feeder.run()
