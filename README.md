# CompSciSoc

Open `.hex` files in https://makecode.microbit.org/

## Python in Desktop
### Flashing via CLI
We can use `uflash` 

# Findings
| Date | Description |
| ---- | ----------- |
| 06/06/2024 | When reading from serial, you have to read the line twice for some reason, otherwise there is a large amount of delay. This literally means duplicating the line and can be store as anything (suggested `_`)