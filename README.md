# Remote_Light_Controller

This is i system that sends ON and OFF  commands to a remote Lamp

## How it works briefly:

In this system for the client side content (html file) is for the publisher.

1) connectes to the mqtt broker 
2) publishes data through websockets.

For the server side content (python file) is for the subscriber.
1) It connectsto the broker
2) Subscribes to the publisher's topic
3) Starts lamp simulation and receiving data published by the publisher.

## 🔧 Installation

To run this project locally:

```bash
#clone the repository
git clone https://github.com/Mugabepro-1/Remote_Light_Controller.git

# Install teh mqtt package 
pip install paho.mqtt

#Then run the python file
python3 light_simulation.py


