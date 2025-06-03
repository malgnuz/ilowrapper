#!hpeilo/bin/python3
import argparse
import hpilo

global ilo
# Function to get the iLO firmware version
def get_fw(a):
   return a.get_fw_version()

# Get the server's name
def get_name(a):
   return a.get_server_name()

# Get the power supplies status
def pw_supply_status(a):
    health = a.get_embedded_health()
    return health['health_at_a_glance']['power_supplies']

# Get all data from server
def get_data(a):
    return a.get_host_data()
   
# Power on a server
def power_on(a):
    return a.set_host_power()

# Power off a server
def power_off(a):
    return a.set_host_power(False)

# Get the power status from a server
def power_status(a):
    return a.get_host_power_status()

# Get the serial number from a server
def get_serial(a):
    return a.get_host_data()[1]['Serial Number']

# Power cycle a server
def reset(a):
    return a.reset_server()

def retrieve_arguments():
    parser = argparse.ArgumentParser(description='Returns servers facts from iLO',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('server',help='The server IP address')
    parser.add_argument('username',help='The username of the administrative user')
    parser.add_argument('password',help='The password of the administrative user')
    parser.add_argument('--fw', action='store_true', help='Print firmware version of the server')
    parser.add_argument('--serial', action='store_true', help='Print serial number of the server')
    parser.add_argument('--name', action='store_true', help='Print name of the server')
    parser.add_argument('--ps', action='store_true', help="Print the status of the server's power supplies")
    parser.add_argument('--d', action='store_true', help="Print data of the server")
    parser.add_argument('--poweron', action='store_true', help="Power on the server")
    parser.add_argument('--poweroff', action='store_true', help="Power off the server")
    parser.add_argument('--powerstatus', action='store_true', help="Get power status of the server")
    parser.add_argument('--reset', action='store_true', help="Power cycle the server")
    args = parser.parse_args()
    return args

def main():

  args = retrieve_arguments()
  ilo = hpilo.Ilo(args.server,args.username,args.password)

  if args.fw:
     print(get_fw(ilo))

  if args.name:
     print(get_name(ilo))

  if args.ps:
     print(pw_supply_status(ilo))

  if args.d:
     print(get_data(ilo))

  if args.poweron:
     print(power_on(ilo))

  if args.poweroff:
     print(power_off(ilo))

  if args.serial:
     print(get_serial(ilo))

  if args.powerstatus:
     print(power_status(ilo))

  if args.reset:
     print(reset(ilo))

if __name__ == "__main__":
    main()
