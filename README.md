# M365-Pi-Controller

Another weird controller of xioami m365 electric scooter however controlled by rasperry pi zero W.

## How to assembly
Parts needed:

* Raspberry pi zero W
* OLED 0,96 I2c
* 4 x 1k Ohm resistors
* 4 x 10k Ohm resistors
* 4 x push buttons switch
* about 4m of wire
* micro usb male connector

### Breadboard:

![breadboard](/images/m365_bb.png "breadboard" )

### Schematic:

![schema](/images/m365_schema.png "schema")

### Example soldering on pcb prototype board:

<img src="./images/display.jpg?raw=true" width="425" /> <img src="./images/display_upside_down.jpg?raw=true" width="425"/>
<img src="./images/all.jpg?raw=true" width="425"/> <img src="./images/pads.jpg?raw=true" width="425" />

### Power raspberry pi zero from scooter
Bluetooth scooter controller has to be modified as well in such a way that lead out 5V from the controller to power raspberry pi zero W. \
If you still have warranty, the way not to lose it is to buy a used bluetooth controller (costs around 15$) \
See below images.

<img src="./images/bt_ctrl_side.jpg?raw=true" width="425" /> <img src="./images/bt_ctrl_back.jpg?raw=true" width="425"/> 

## How to run
Install clear raspbian into your SD card from <a href="https://www.raspberrypi.org/downloads/raspbian/">here</a>.

After that, run these commands:
<pre>
sudo apt-get update
sudo apt-get upgrade
</pre>

Next write:
`sudo nano /lib/systemd/system/bluetooth.service`\
and change line 
<pre>
ExecStart=/usr/local/libexec/bluetooth/bluetoothd --experimental
</pre>
Next write: 
`sudo systemctl edit bluetooth.service` \
and paste bellow configuration to file 
<pre>
[Service] 
ExecStartPre=/bin/bash -c 'echo 6 > /sys/kernel/debug/bluetooth/hci0/conn_min_interval; echo 60 > /sys/kernel/debug/bluetooth/hci0/conn_max_interval'
</pre>

Next step to do is connecting your rpi to scooter. \
Turn on your scooter firstly and write commands bellow:
<pre>
sudo hcitool lescan
sudo hcitool lecc --random [scooter mac address]

sudo bluetoothctl
trust [scooter mac address]
pair [scooter mac address]
exit
</pre>
