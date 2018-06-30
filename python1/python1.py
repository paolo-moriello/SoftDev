import re
import sys

a = []
for line in sys.stdin:
    number = re.findall('\d+', line)
    number = int(number[0])
    a.append([number, line])

a.sort(reverse=True, key=lambda tup: tup[0])

for i in range(int(sys.argv[1])):
    sys.stdout.write(a[i][1])

while(i < len(a)-1 and a[i+1][0] == a[i][0]):
    i += 1
    sys.stdout.write(a[i][1])

