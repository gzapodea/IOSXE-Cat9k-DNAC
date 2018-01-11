#! /usr/bin/env python3


# developed by Gabi Zapodeanu, TSA, GPO, Cisco Systems


import requests
import json
import time
import os
import os.path
import urllib3
import socket
import re

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

from init import GOOGLE_API_KEY
from init import DNAC_URL, DNAC_PASS, DNAC_USER


urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)
