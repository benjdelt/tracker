import sys
import os
import csv
from user_interface import UserInterface
from select import select

import time

import timer


class Feeder:
    def __init__(self, task):
        self.running = False
        self.ui = UserInterface()
        self.task = task or "None"
        self.first_start = time.time()
        self.start = time.time()
        self.recorded_time = 0
        self.paused = False

    def run(self):
        self.running = True
        self.ui.win.addstr(11, 1, f"Task: {self.task}")
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
                    if line.strip() == "q":
                        self.quit()
                        break
                    elif line.strip() == "p":
                        if self.paused:
                            self.start = time.time()
                            self.ui.win.addstr(14, 29, "          ")
                            self.paused = False
                        else:
                            self.recorded_time = timer.compute_time(
                                self.start,
                                self.recorded_time
                            )
                            self.ui.win.addstr(14, 29, "**PAUSED**")
                            self.paused = True
                    elif line.strip() == "s":
                        start = time.ctime(self.first_start)
                        finish = time.ctime()
                        if self.paused:
                            logged = self.recorded_time
                        else:
                            logged = timer.get_time_string(self.start, self.recorded_time)
                        current_row = {"Start": start, "Finish": finish, "Logged": logged}
                        lines = []
                        try:
                            with open(f"./{self.task}.csv", "r") as csvfile:
                                taskreader = csv.DictReader(csvfile)
                                headers = taskreader.fieldnames
                                for row in taskreader:
                                    last_task = row
                                    lines.append(row)
                                if last_task["Start"] == start:
                                    lines = lines[0:-1]
                            csvfile.close()
                            with open(f"./{self.task}.csv", "w", newline='') as csvfile:
                                lines.append(current_row)
                                taskwriter = csv.DictWriter(csvfile, ["Start", "Finish", "Logged"])
                                taskwriter.writeheader()
                                for line in lines:
                                    taskwriter.writerow(line)

                        except FileNotFoundError:
                            with open(f"./{self.task}.csv", "w", newline='') as csvfile:
                                taskwriter = csv.DictWriter(csvfile, ["Start", "Finish", "Logged"])
                                taskwriter.writeheader()
                                taskwriter.writerow(current_row)
                if not self.paused:
                    self.ui.win.addstr(
                        9,
                        33,
                        timer.get_time_string(self.start, self.recorded_time)
                    )
                self.ui.refresh()
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.quit()


if __name__ == "__main__":
    feeder = Feeder(time.time())
    feeder.run()
