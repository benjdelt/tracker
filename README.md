# Tracker

Python script using Curses to display a simple timer in the command line.

**As the Windows version of Python doesn’t include the Curses module, Windows is not supported (yet).**

## Installation Instructions

1. Fork this repository, then clone your fork of this repository.
2. Run the tracker executable:
   ```bash
   $ ./tracker
   ```
3. Optional: Add the directory to the `$PATH` variable so you can call the script from anywhere using the following command:
   ```bash
   $ tracker
   ```
   - Open `~/.profile` (or `~/.zshrc` for zsh) with the editor of your choice
   - Add this line to the end of the file:
        ```bash
        export PATH=</path/to/tracker/directory>:$PATH
        ```
    See [this post](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path) for more information.
