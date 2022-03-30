from pypresence import Presence
import time
import re, sys, subprocess, os

client_id = 'CLIENT_ID_GOES_HERE'
maquina = input("Machine name: ")

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + " <ip_address>\n")
    sys.exit(1)

def get_ttl(ip_address):

    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]

    return ttl_value

def get_os(ttl):

    ttl = int(ttl)

    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    else:
        return "Not Found"

if __name__ == '__main__':

    ip_address = sys.argv[1]

    ttl = get_ttl(ip_address)

    os_name = get_os(ttl)
    print("%s (ttl -> %s): %s" % (ip_address, ttl, os_name))

RPC = Presence(client_id)
RPC.connect()

if os_name == "Linux":
    imagen = "linux"
elif os_name == "Windows":
    imagen = "windows"
else:
    print("Error: OS not recognized.")
    exit()
    
tmux = "tmux rename-window " + "\"" + maquina + " | " + ip_address + "\""
os.system(tmux)

RPC.update(state="Hacking The Box...", details="/dev/tcp/" + ip_address, large_image="htb", small_image=imagen, large_text="HTB: " + maquina, small_text=os_name, start=time.time())
print("Discord Connection Success! (Don't end the script until the machine is finished)")

while True:
    time.sleep(15)
