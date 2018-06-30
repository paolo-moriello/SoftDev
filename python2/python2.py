import socket
import pickle
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 1024
user = 'paolomoriello'
secret = 'd442989b3c1f4f6545acd37b5760a438'
NUMBERS = ['  ###   #   # # #   ##  #  ##   # # #   #   ###  ', '   #     ##    # #      #      #      #    ##### ', ' ##### #     #      # ##### #      #      #######', ' ##### #     #      # #####       ##     # ##### ', '#      #    # #    # #######     #      #      # ', '########      #       #####       ##     # ##### ', ' ##### #     ##      ###### #     ##     # ##### ', '########    #     #     #     #      #      #    ', ' ##### #     ##     # ##### #     ##     # ##### ', ' ##### #     ##     # ######      ##     # ##### ']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE)
print(data)
s.send(user+'\n')
print(user)
data = s.recv(BUFFER_SIZE)
print(data)
s.send(secret+'\n')
print(secret)
data = s.recv(BUFFER_SIZE)
print(data)

a = 0
b = 10000
num = (a+b)/2
s.send(str(num)+'\n')
print(num)
data = s.recv(BUFFER_SIZE)
print(data)
while('nope' in data):
	if('bigger' in data):
		a = num
	else:
		b = num
	num = (a+b)/2
	s.send(str(num)+'\n')
	print(num)
	data = s.recv(BUFFER_SIZE)
	print(data)

data = s.recv(BUFFER_SIZE)
print(data)

lines = data.split("\n")
words=['','','']
for i in range(0, 7):
	words[0] += lines[i][:7]
	words[1] += lines[i][16:23]
	words[2] += lines[i][32:39]
	for j in range(len(lines[i]),39):
		words[2] += ' '
num = 0
#print(words)
for i in range(3):
	num *= 10
	j = 0
	while(words[i] != NUMBERS[j]):
		j += 1
	num += j

print(num)
s.send(str(num)+'\n')
data = s.recv(BUFFER_SIZE)
print(data)

data = s.recv(BUFFER_SIZE)
print(data)
data = data.split("\n")[1:9]
data = '\n'.join(data)
load = pickle.loads(data)
print(str(load.microsecond))
s.send(str(load.microsecond)+'\n')


data = s.recv(BUFFER_SIZE)
print(data)
data = s.recv(BUFFER_SIZE)
print(data)
data = data.split(" ")
day = int(data[5])
month = datetime.datetime.strptime(data[6], '%b').month
year = int("20"+data[7][:2])
day_of_week = datetime.date(year, month, day)
print(day_of_week.strftime("%A"))
s.send(day_of_week.strftime("%A")+"\n")

data = s.recv(BUFFER_SIZE)
data = data.split("\n")[2]
print(data)



s.close()
