import curses
import curses.panel


class UserInterface:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)

        self.win = curses.newwin(20, 70, 0, 0)
        self.win.border(0)

        self.win.addstr(1, 30, "Tracker")
        self.win.addstr(2, 30, "=======")
        instructions = "Press 'p' to pause/unpause, 's' to save to CSV or 'q' to quit."
        self.win.addstr(4, 1, instructions)

    def refresh(self):
        curses.panel.update_panels()
        self.win.refresh()

    def quit_ui(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.curs_set(1)
        curses.echo()
        curses.endwin()
