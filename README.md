# CompSciSoc

Open `.hex` files in https://makecode.microbit.org/

## Python in Desktop
### Flashing via CLI
We can use [`uflash`](https://github.com/ntoll/uflash) (I suggest not searching for this without safe search...). Basic usage shown below:

- `uflash [file]` - flash file to MicroBit
- `uflash -w [file]` - watch file for changes and immediately flash

### Intellisense and Linting Errors
We can install the module [`pseudo-microbit`](https://pypi.org/project/pseudo-microbit/) to remove any linting errors when using Microbit functions as well as to generate Intellisense auto-complete.

## Findings
| Date | Description |
| ---- | ----------- |
| 06/06/2024 | When reading from serial, you have to read the line twice for some reason, otherwise there is a large amount of delay. This literally means duplicating the line and can be store as anything (suggested `_`) |
| 07/06/2024 | MicroPython comes with a limited number of libraries that can be found here: https://docs.micropython.org/en/latest/library/index.html. However, this can be expanded by accessing the MicroBit persistent file system using [`ufs`](https://github.com/ntoll/microfs).

## Project Structure
```
CompSciSoc/         root
├─ examples/        mini example projects such as tilting turtle
├─ lib/             library files useful in many projects such as serial tilting
├─ mb/              microbit python files
├─ Minigames/       full minigames
```