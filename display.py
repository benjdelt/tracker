import curses
import curses.panel
import sys
from select import select
from time import sleep, time

from timer import get_time


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
        self.win.addstr(4, 1, "Press 'q' to quit.")

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
        exit(f"Time: {get_time(self.start)}")


class Feeder:
    def __init__(self, start):
        self.running = False
        self.ui = UserInterface(start)
        self.start = start

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

                self.ui.win.addstr(9, 33, get_time(self.start))
                self.ui.refresh()
                sleep(1)
        except KeyboardInterrupt:
            self.stop()
            self.ui.quit_ui()


if __name__ == "__main__":
    feeder = Feeder(time())
    feeder.run()
