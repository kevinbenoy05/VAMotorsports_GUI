# Arduino Experiments

I've been (slowly) experimenting with the Arduino and took considerable time to work out the environment and create libraries compatible with Visual Studio 2012.

## Visual Studio Libraries

You can find Visual Studio projects in the **Libraries** directory for the following:
* The [*AVR LibC*](./Libraries/AVR%20Libc), containing the basic C framework (**i.e.** stdio, stdlib, math, etc.)
* The [*Low Level Arduino library*](./Libraries/Libraries), containing the interfacing helpers
* The [*Core Arduino library*](./Libraries/Core), containing the Arduino board framework and basic functions/helpers
* The [*Pom Library*](./Libraries/Pom), containing advanced helpers I required along my work. Quite empty at the moment, but will keep growing.

## Visual Studio Arduino Lessons

You can also find the basic Arduino lessons (the most complex ones at least, I didn't bother with the simple ones) in the form of Visual Studio projects:
* LED Blink
* Keypad
* Temperature Sensor
* Joystick
* Infra-Red Sensor
* LED Matrix
* RFID Sensor
* etc.

## Notes

I kept interesting [notes](./Arduino%20ROOT%20DOC.md) to quickly remember the subtleties of the Arduino dialect and environment.

Maybe of interest to you:
* How to add your custom C/C++ library to the core library
* How to easily compile you C files into assembly language (**i.e.** making the GCC compiler generate a .S file that you can later modify)


## Tests

### CC1101

I played a bit with the Radio-Frequency chip CC1101 by Texas Instrument, I rewrote the driver and kind of managed to drive it correctly except at the moment I never quite could receive anything.

I'll try again with another RF device, the nRF24L01 this time.
