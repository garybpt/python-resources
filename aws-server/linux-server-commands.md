# Linux Server Commands

Note - to connect to the server, the .pem file must be present in the open directory. 

**Connect to the AWS server**

ssh -i "[.pem file name]" [AWS IP address]

**Run a Python script permanently on server**

nohup python3 script-name.py &

**Kill script**

One option - in root directory, run:

pkill -9 -f [script-name.py]

Another option, in root directory, run:

'''
ps -elf | grep python - This will find the PID number for the script you want to kill. It will be the second number.

kill -9 [PID-number]
'''