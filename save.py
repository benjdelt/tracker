import csv
import time

import config
import timer


class Save:

    def __init__(self, first_start, paused, recorded_time, start, task):
        self.task = task
        self.header = ["Start", "Last Saved", "Logged", "Total"]
        self.row_start = time.ctime(first_start)

        if paused:
            self.row_logged = timer.format_time(recorded_time)
        else:
            self.row_logged = timer.get_time_string(start, recorded_time)

        self.current_row = {
            "Start": self.row_start,
            "Last Saved": time.ctime(),
            "Logged": self.row_logged,
            "Total": self.row_logged
        }
        self.lines = []

    def get_data_from_file(self):
        with open(f"{config.csv_path}/{self.task}.csv", "r") as csvfile:
            taskreader = csv.DictReader(csvfile)
            for row in taskreader:
                last_task = row
                self.lines.append(row)
            # If the line exists, remove it
            if last_task["Start"] == self.row_start:
                self.lines = self.lines[:-1]
            # Only add the total and logged time if there is more than one line
            # otherwise, the total remains the logged time
            if len(self.lines) > 0:
                last_task = self.lines[-1]
                total_seconds = timer.parse_time_string(last_task["Total"])
                self.current_row["Total"] = timer.format_time(
                    timer.parse_time_string(self.row_logged) + total_seconds
                )

    def write_to_file(self):
        with open(f"{config.csv_path}/{self.task}.csv", "w", newline='') as csvfile:
            self.lines.append(self.current_row)
            taskwriter = csv.DictWriter(csvfile, self.header)
            taskwriter.writeheader()
            for line in self.lines:
                taskwriter.writerow(line)

    def save_to_csv(self):
        try:
            self.get_data_from_file()
        except FileNotFoundError:
            pass
        finally:
            self.write_to_file()
