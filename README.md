# Tracker

Python script using Curses to display a simple timer in the command line.

**As the Windows version of Python doesn’t include the Curses module, Windows is not supported (yet).**

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
   - Open `~/.profile` (or `~/.zshrc` for zsh) with the editor of your choice
   - Add this line to the end of the file:
        ```bash
        export PATH=</path/to/tracker/directory>:$PATH
        ```
    See [this post](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path) for more information.

## Usage

```bash
$ tracker [TASK]
```

Logs time for a specific TASK to the command line.

While the script is running,: 
- Press `p` to pause or unpause the timer. 
- Press `q` or `CTRL-C` (`CMD-C`) to quit the tracker. The total logged time will be displayed in the command line.