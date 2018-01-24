

# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems


import urllib3
import spark_apis

from cli import cli
from init import SPARK_ROOM

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

urllib3.disable_warnings(InsecureRequestWarning)  # Disable insecure https warnings


syslog_input = cli("show logging | in %PLATFORM_THERMAL-1-FRU_FAN_FAILURE:")
syslog_lines = syslog_input.split("\n")
lines_no = len(syslog_lines)-2
syslog_info = syslog_lines[lines_no]

device_name = cli("show run | in hostname")
print("Device hostname: ", device_name)

spark_apis.post_room_message(SPARK_ROOM, "The device with the " + device_name + " has detected:")
spark_apis.post_room_message(SPARK_ROOM, syslog_info)
spark_apis.post_room_message(SPARK_ROOM, "Switch Beacon LED turned ON")

cli("configure terminal\nhw-module beacon on switch 1")

print("End Application Run")
