#RUNNING SYSTEM COMMANDS
#THE OS MODULE


# try this on shell
# import os
# output = os.popen('ls -l/etc').read() #this opens a pipe and return the value
# print(output)


# os.system(type null > '/home/binlawal/abc.txt')#this command will create an empty text file called abc.txt

#another way to run system commands from python is to use the subprocess module
#the subprocess module provides more powerful facilities for spawning new processes and retreiving thier results
#using subprocess is preferable to using the os module , the advantage of using the subprocess module vs os module is that it is more flexible we have access
#to standardoutput(stdout), standarderror(stderr), the real status code and it offers better error handlin, lets see how to use subprocess to execute system commands 


#we will take a look at two important functions

subprocess.check_call()
subprocess.check_output()

check_call() runs the command with arguments and waits for the command to complete if the return code was zero it means that there was no error and it returns  otherwise it raises "call process error exception" 
th second function check_output is similar to check_call but it also return the command output

# inshort subprocess.check_call() to runs a command and subprocess.check_output() runs a command and returns its output
the argument of check_ouput() function is a list that has as elements the command and its arguments
i.e
cmd = ['arp', '-a']
import subprocess
subprocess.check_output(cmd)
and it returns the output of the command as an object of type byte we can convert it to a string using the decode method


#another example is to execute the ping command from python
cmd = ['ping', '-n', '2', '8.8.8.8' ]
output = subprocess.check_output(cmd)
#to convert to a string 
str_output = output.decode()