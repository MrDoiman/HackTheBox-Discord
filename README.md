# HackTheBox Discord
This script sets a custom Discord Rich Presence with your HackTheBox Machine Loader, sets in which system you are (whether Windows/Linux) depending on the TTL, also changes your tmux window name following the next format "Machine Name | Machine IP".

# Installation

Client Side:
```
git clone https://github.com/MrDoiman/HackTheBox-Discord/
pip install pypresence
```
**IMPORTANT:** You must have python3 and tmux installed.

Discord Side:
You must create an application in the [discord's developers portal](https://discord.com/developers/applications) and insert your client ID on the parameter called *client_id*, then you have to upload the [assets](assets/) found on the project folder and upload the images to the Discord Rich Presence app. 

Note: It may take up to 10 minutes to upload the images and you must keep the images names.

# Execution
**Important:** Run in a tmux session.

```
python3 htb.py <ip_address>
```

# Common Errors

1. As the script was coded to work with macOS, it may not locate where you ping utility is, whether you are using Linux or other OS. For fixing that, edit the following line with your ping command path:

![Err1Fix](https://cdn.discordapp.com/attachments/902618257159233596/958644066793426964/errfix1.png)
