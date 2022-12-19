import os

s_arr = []
s = os.popen("sensors | grep -i CPU").read()
s_arr = s.split()
print(s_arr[1][1:])
