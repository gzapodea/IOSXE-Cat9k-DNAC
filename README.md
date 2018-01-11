
# **IOSXE-Cat9k-DNAC**

This repo will be used to share sample code that will use IOS XE, Catalyst 9k and DNA Center programmability features.


**verify_ip_duplicates.py**

This simple script will:
- This script will:
 - load a file with a configuration to be deployed to a network device
 - identify the IPv4 addresses that will be configured on interfaces
 - search in the DNA Center database if these IPV4 addresses are configured on any interfaces
 - find if any clients are using the IPv4 addresses
 - determine if deploying the configuration file will create an IP duplicate


**dnac-apis.py**

This experimental module includes functions to be used with DNA Center


**utils.py**

This module includes common functions to be used by various python modules. They do not belong to any technology or product family.


**init.py**

The init module where you will need to enter the values for your environment


**configuration_template.txt**

Sample configuration file. Replace this file with the one you would like to check.


