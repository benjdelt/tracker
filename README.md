# Tracker

Python script using Curses to display a simple timer in the command line. The logged timers can be autosaved to CSV files.

**As the Windows version of Python doesn’t include the Curses module, Windows is not supported.**

## Getting Started

Make sure that Python 3 is installed of your computer:

```bash
$ python3 --version
```

If Python 3 is not installed, you can follow these instructions:
- [Ubuntu](https://docs.python-guide.org/starting/install3/osx/)
- [Mac](https://docs.python-guide.org/starting/install3/linux/)

Once Python 3 is installed, you can start with Tracker:

1. Fork this repository, then clone your fork of this repository and `cd` into it.
2. Change the `tracker` file permissions to make it executable:
   ```bash
   $ chmod +x ./tracker
   ```
3. Run the tracker executable:
   ```bash
   $ ./tracker
   ```
4. *Optional*: Add the directory to the `$PATH` variable so you can call the script from anywhere using the following command:
   ```bash
   $ tracker
   ```
   - Open `~/.profile` (or `~/.zshrc` for zsh) with the editor of your choice.
   - Add this line to the end of the file:
        ```bash
        export PATH=</path/to/tracker/directory>:$PATH
        ```
    See [this post](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path) for more information.

## Usage

### Start

```bash
$ tracker [TASK]
```

Logs time for a specific TASK to the command line. See [Configuration](#Configuration) for autosave features.

### Task

The name of a task can be provided in the command line when launching the tracker. It allows you to categorize your trackers according to different tasks. The task name will be used as the CSV file name when the tracker is saved.

The task name can't start with a dash (`-`) or contain spaces. 

### Save

The tracker will be autosaved upon quitting as well as every minute since the timer has started (by default, see [Configuration](#Configuration) to change the autosave behavior), even if it is paused. Press `s` to save manually.

The tracker is saved under the current folder by default (see [Configuration](#Configuration) to change the destination folder) in a file named `{task}.csv` where `{task}` is the name of the task given when launching the tracker. If no file by that name exists, one will be created. If no task were provided when launching the tracker, it will be saved under `None.csv`.

The created file contains the following columns:

- `Started`: the date and time at which the tracker was launched.
- `Last Saved`: the date and time at which the tracker was saved.
- `Logged`: the time logged by the tracker since it started (excluding paused time) under the format `hh:mm:ss`.
- `Total`: the total time logged in the file under the format `hh:mm:ss`.

### Pause

Press `p` to pause or unpause the timer. While the timer is not updated when the tracker is paused, it is still autosaved every minute by default (see [Configuration](#Configuration) to change the delay).

### Quit

Press `q` to quit the tracker. The total logged time will be displayed in the command line and autosaved in a CSV file by default (see [Configuration](#Configuration) to deactivate the autosave when quitting).

Press `CTRL-C` / `CMD-C` to quit the tracker by interrupting the process. The total logged time will be displayed in the command line but will not be autosaved in a CSV file by default (see [Configuration](#Configuration) to activate the autosave when quitting).

### Configuration

There is a `config.json` file in the tracker folder that you can edit to easily customize some tracker functionalities.

- `csv-path`(String): the absolute or relative path where the CSV files are saved. The files are saved under `{csv-path}/{task}.csv`. The default value is `./`.
- `autosave-delay`(String): the delay after which the tracker is automatically saved. Provide a string under the format `hh:mm:ss` where `hh` and `mm` are optional, i.e.: for `5:00`, the tracker will be saved every 5 minutes and for `1:00:00`, it will be saved every hour. To diable the autosave feature, set it to `0`. The default value is `1:00`.
- `autsave-q`(Boolean): if set to `true`, the tracker will be saved when you quit by pressing `q`. The default value is `true`.
- `autsave-c`(Boolean): if set to `true`, the tracker will be saved when you interrupt the process (`CTRL-C` / `CMD-C`). The default value is `false`.