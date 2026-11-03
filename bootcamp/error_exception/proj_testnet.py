import subprocess
command = 'ping -n 1 8.8.8.3'
output = subprocess.check_output(command.split())
print(output.decode())

with open("hosts.txt", 'r') as f:
    content = f.read().splitlines()
    for lines in content:
        try:
            command = f'ping -n 1 {lines}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'host down for line{lines} because:{e}')
            print('-' * 50)
            
            
            

     
