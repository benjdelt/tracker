# Tracker

Python script using Curses to display a simple timer in the command line. The logged timers are auto saved to CSV files.

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
   - Open `~/.pPython script using Curses to display a simple timer in the command line
   - Add this lPython script using Curses to display a simple timer in the command line
        ```bashPython script using Curses to display a simple timer in the command line
        export PATH=</path/to/tracker/directory>:$PATH
        ```
    See [this post](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path) for more information.

## Usage

### Start

```bash
$ tracker [TASK]
```

Logs time for a specific TASK to the command line and auto saves every minute in a CSV file.

### Save

The tracker will be auto saved upon quitting as well as every minute since the timer has started, even 
if it is paused. Press `s` to save manually.

The tracker is saved in a file named `{task}.csv` where `{task}` is the name of the task given when launching the tracker. If no file by that name exists, one will be created. If no task were provided when launching the tracker, it will be saved under `None.csv`.

The created file contains the following columns:

- `Started`: the date and time at which the tracker was launched.
- `Last Saved`: the date and time at which the tracker was saved.
- `Logged`: the time logged by the tracker since it started (excluding paused time) under the format `hh:mm:ss`.
- `Total`: the total time logged in the file under the format `hh:mm:ss`.

### Pause

Press `p` to pause or unpause the timer. While the timer is not updated when the tracker is paused, it is still auto saved every minute.

### Quit

Press `q` or `CTRL-C` (`CMD-C`) to quit the tracker. The total logged time will be displayed in the command line and auto saved in a CSV file.