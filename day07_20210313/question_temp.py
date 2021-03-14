import os
import re
route_n_result = os.popen('route -n').read()
print(route_n_result)
print('----------------')
print(route_n_result.strip().split('\n'))
#print(route_n_result)
for route in route_n_result.strip().split('\n')[2:]:
	re_route = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
						r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
						r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+'
						r'(\w+)\s+\d+\s+\d+\s+ \w+',route.strip()).groups()
	if re_route[1] == 'UG':
		print('网关为:',re_route[0])
		break

