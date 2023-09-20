# IOT Based River Water Quality Monitoring System Using IBM Watson
## Features

List the key features of your system.

- River water quality monitoring through a web application.
- Detection of dust particles in the water.
- Monitoring of pH levels.
- Water temperature monitoring.
- Alerting authorities in case of poor water quality.

##Proposed solution

The main aim is to develop a system for continuous monitoring of
river water quality at remote places using wireless sensor networks with low power
consumption, low-cost and high detection accuracy. pH, conductivity, turbidity level, etc.
are the limits that are analyzed to improve the water quality. Following are the aims of
idea implementation 
(a) To measure water parameters such as pH, dissolved oxygen,
turbidity, conductivity, etc. using available sensors at a remote place. 
(b) To assemble
data from various sensor nodes and send it to the base station by the wireless channel.
(c) To simulate and evaluate quality parameters for quality control. 
(d) To send SMS to
an authorized person routinely when water quality detected does not match the preset
standards, so that, necessary actions can be taken.

## Experimental Investigation

As Hardware is not available I have taken random values in python for sensor data as
physical hardware is not available.
Coming to Software,the designed River water quality monitoring system can be
divided into:
•IBM WATSON IOT PLATFORM
• NODERED
• MIT APP INVENTOR
• WEB UI AND HTTP REQUESTS
• FAST2SMS

First we have to create an account in IBM cloud,then a device is to be created.using the
device credentials in the python code we have take some random values as Hardware is not
avaialble.Using different nodes in NODERED,a flow is created and connected to IBM
platform.using the url we can get data and pictorial representation by appending /data and /ui
respectively to the url in new page.This is further extende to mobile application use by using MIT
APP INVENTOR.A design and blocks are created according to the use.In order generste
message to the agent FAST2SMS app is created.This completes the software along with
hardware of the project.
