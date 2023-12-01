# ProductivityOpen CircuitPython-P1AM

The CircuitPython-P1AM library is a CircuitPython library for use with the AutomationDirect ProductivityOpen P1AM-200 CPU. It provides a simple interface to Productivity1000 series industrial IO modules.

In-depth information on the P1AM family and Productivity1000 Modules can be found on the reference page here: 
[P1AM Documentation](https://facts-engineering.github.io/)

Productivity Series modules offer several types of industrial grade I/O 
 - Analog and Temperature Inputs 
 - Analog Outputs
 - Discrete Inputs
 - Discrete Outputs and Relays
 - Specialty Modules

The P1AM-200 can be purchased on the [Automation Direct Webstore](https://www.automationdirect.com/adc/shopping/catalog/programmable_controllers/open_source_controllers_(arduino-compatible)/productivityopen_(arduino-compatible)/controllers_-a-_shields/p1am-200)

Productivity1000 Series Modules can be purchased on the [Automation Direct Webstore](https://www.automationdirect.com/adc/shopping/catalog/programmable_controllers/productivity1000_plcs_(stackable_micro))

## Usage
The CircuitPython-P1AM library provides a simple interface for controlling P1000 Modules. See the examples folder for more detailed examples for your products. 

```python
relay = base[1][2] # Relay on slot 1 channel 2
temperature_sensor = base[3][1] # Temperature sensor on slot 3 channel 1

relay.value = True # Set relay to ON
temperature = temperature_sensor.value # Read temperature sensor 

```
## What is CircuitPython?

CircuitPython is a programming language based on Python that is designed to run on microcontrollers. If you are familiar with Python, you will feel right at home using CircuitPython. For more information on CircuitPython, [Adafruit's guide](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython).

## Compatibility

This library is compatible with the P1AM-200. It **is not** compatible with the P1AM-100.

# Base Controller #
The P1AM Base Controller is the chip that directs communcations between the P1AM-CPU and the P1000 Modules. A P1000 Series power supply or external 24V supply is required to power the Base Controller and modules. On the P1AM-200, all pins used to communicate with the Base Controller are internal to the device, so no header pins are consumed.

