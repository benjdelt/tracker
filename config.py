import json
import timer
import sys

def strip_final_slash(path):
    return path[:-1] if path[-1] == "/" else path

file_path = sys.argv[0].split("//")[0]
with open(f"{file_path}/config.json", "r") as config_file:
    config = json.loads(config_file.read())
    try:
        csv_path = strip_final_slash(config["csv-path"])
    except:
        csv_path = "."
    try:
        autosave_delay = timer.parse_time_string(config["autosave-delay"])
    except:
        autosave_delay = 60
    try:
        autosave_q = bool(config["autosave-q"])
    except:
        autosave_q = True
    try:
        autosave_c = bool(config["autosave-c"])
    except:
        autosave_c = False
