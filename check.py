from urllib import request as url
from pprint import pprint
import re
import yaml
#mac_vendor_list = url.urlopen('https://standards-oui.ieee.org/oui/oui.txt').read().decode()
regex = r'(?P<mac_prefix>\w{2}-\w{2}-\w{2})\s+\(hex\)\s+(?P<vendor>.+)'
macvendor = {}
with open('oui.txt', encoding="utf8") as f:
    for line in f:
        match = re.match(regex, line)
        if match:
            mac_prefix, vendor = list(match.groups(1))[0].replace('-',''), match.group(2)
            macvendor[mac_prefix] = vendor
print(f'there are {len(macvendor)} records')
pprint(macvendor)

with open('macvendor.yml', 'w') as out:
    yaml.dump(macvendor, out, default_flow_style=False)