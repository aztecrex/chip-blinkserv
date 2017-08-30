# Demo Web Server Control

Demonstrate a web server running on a C.H.I.P. and
controlling its devices.

## Demos

### LED

Turn LED on and off via Web API.

## Hardware

- C.H.I.P. tiny computer (4.4 OS tested)
- for the LED demo, a LED

### LED demo wiring

The extended pins can sink enough current to light an LED. But only
barely enough to light one by sourcing it. So, wire it so that LOW on
the XIO pin turns on the lamp. The XIO pins on the C.H.I.P are weird
if you are used to other GPIO chips.  See the docs for info.

To be especially safe, the spec sheet suggests a 2K resistor between
3.3V and the LED anode. I did't do that myself but I probably should
have.

- cathode goes to XIO-P0
- anode goes to 3.3V (through 2K resistor to be safe)

## How To Run

This project requires Python3 installed on the C.H.I.P. tiny computer.

Install these depencies into your Python3 environment with `pip`.

- Flask
- GPIO-IO

Modify `run.sh` with the name of your Python3 virtualenv activation
source.

`sudo ./run.sh`

Currently needs to execute as root to export IO pins and bind to port 80.

## Connect

Point your browser to the C.H.I.P.'s address. If Avahi is working,
just use it's name.  Navigate to the demo you want to see.

## API

### LED

The LED control exposes 3 HTTP resources:

- `/api/led` : `GET` this resource for the status of the LED
- `/api/led/on` `POST` to this resource to turn the LED on
- `/api/led/off` `POST` to this resource to turn the LED off



