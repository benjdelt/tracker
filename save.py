import csv
import time
import timer

def save(first_start, paused, recorded_time, start, task):
    header = ["Start", "Finish", "Logged", "Total"]
    row_start = time.ctime(first_start)
    row_finish = time.ctime()
    if paused:
        row_logged = timer.format_time(recorded_time)
    else:
        row_logged = timer.get_time_string(start, recorded_time)
    current_row = {"Start": row_start, "Finish": row_finish, "Logged": row_logged, "Total": row_logged}
    lines = []
    try:
        # Read the file to get the total and check if the current line already exists
        with open(f"./{task}.csv", "r") as csvfile:
            taskreader = csv.DictReader(csvfile)
            headers = taskreader.fieldnames
            for row in taskreader:
                last_task = row
                lines.append(row)
            if last_task["Start"] == row_start:
                lines = lines[0:-1]
            if len(lines) > 0:
                last_task = lines[-1]
                total_seconds = timer.parse_time_string(last_task["Total"])
                current_row["Total"] = timer.format_time(timer.parse_time_string(row_logged) + total_seconds)
        csvfile.close()
        # Add the current line or update it
        with open(f"./{task}.csv", "w", newline='') as csvfile:
            lines.append(current_row)
            taskwriter = csv.DictWriter(csvfile, header)
            taskwriter.writeheader()
            for line in lines:
                taskwriter.writerow(line)
    # If the file doesn't exist, create it, add the headers and the line
    except FileNotFoundError:
        with open(f"./{task}.csv", "w", newline='') as csvfile:
            taskwriter = csv.DictWriter(csvfile, header)
            taskwriter.writeheader()
            taskwriter.writerow(current_row)