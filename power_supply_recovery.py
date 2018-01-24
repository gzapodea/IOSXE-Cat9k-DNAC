
# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems

from cli import cli
import requests
import json
import urllib3
import spark_apis


from init import SPARK_ROOM

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

urllib3.disable_warnings(InsecureRequestWarning)  # Disable insecure https warnings


if __name__ == '__main__':

    syslog_input = cli("show logging | in %PLATFORM_FEP-1-FRU_PS_SUSTAINED_OVERLOAD_RECOVERY")
    syslog_lines = syslog_input.split("\n")
    lines_no = len(syslog_lines)-2
    syslog_info = syslog_lines[lines_no]

    device_name = cli("show run | in hostname")
    print ('Device hostname: ', device_name)

    spark_apis.post_room_message(SPARK_ROOM, "The device with the " + device_name + " has detected:")
    spark_apis.post_room_message(SPARK_ROOM, syslog_info)
    spark_apis.post_room_message(SPARK_ROOM, "Switch Beacon LED turned OFF")

    cli.configure("hw-module beacon off switch 1")

    print("End Application Run")
