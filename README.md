# ilowrapper
A wrapper that leverages python-hpilo to interact with servers through the iLO interface

## Requirements:

* Python3.5 or newer
* python-hpilo package -> https://seveas.github.io/python-hpilo/install.html
* iLO IP address of the server.
* iLO credentials of the server.
* Connectivity to BMC network.

> Note: it's recommended to use a python virtual environment to install the **python-hpilo** package with **pip**.

## Usage

To print help run: 

```
python3 ilofacts.py -h
```

Current version has the following features:
- Print firmware version.
- Print server's name.
- Print Power Supplies status.
- Print all data from the server.
