#!/usr/bin/env python
import requests
import os
import argparse
import json
import shutil


# upstream default config. DO NOT MODIFY UNDER ANY CIRCUMSTANCES, write to /usr/share/aim/defaults.json instead
upstream_default = {
    ""
}
# global variables, such as the directory to install to and so on (per user)
username = os.environ.get("USER")

imagedir = f"/home/{username}/.local/share/aim/Appimages/" 
desktopdir = f"/home/{username}/.local/share/applications/"
icondir = f"/home/{username}/.local/share/icons/hicolor/scalable/apps"
infodir = f"/home/{username}/.local/share/aim/info/"
config = f"/home/{username}/.config/aim.json"
defaultconfig = "/usr/share/aim/defaults.json"
defaultexists = os.path.isfile(defaultconfig)


# check whether the paths for the user exist
if not os.path.exists(imagedir):
    print("WARNING: Appimage directory doesn't exist, creating..")
    os.makedirs(imagedir)

if not os.path.exists(infodir):
    os.makedirs(infodir)

if os.path.isfile(config):
    print("WARNING: config file does not exist, dumping default config..")
    
    # check whether there's a default, and use upstream defaults otherwise
    if defaultexists:
        open("config", "a")
        shutil.copy("defaultconfig", "config")
    else:
        print("WARNING: no default config found, dumping upstream default..")
        with open(config, "w") as file:
            json.dump(upstream_default, file, indent=4)



# check whether we are root and alter the paths if so
#if you are a distributor, make sure these directories exist
is_root = os.getuid() == 0

if is_root == True:
    print ("running as root, operating for all users")
    icondir = "/usr/share/icons/hicolor/scalable/apps/"
    desktopdir= "/usr/share/applications/"
    imagedir = "/var/lib/aim/Appimages/"
    infodir = "/var/lib/aim/info/"
    config = "/etc/aim.json"
else:
    print(f"running as normal user, operating for user {username} only")

# the url with the repo, hopefully this will be more decentralized soon

url = "http://192.168.178.46"



# set up the arguments for parsing te input

parser = argparse.ArgumentParser(description="AppImage Manager (aim)")

parser.add_argument("action", choices=["install", "remove", "update", "upgrade", "fetch"], help="install: installs <package>; \nremove: removes <package>; \nupdate: updates ALL packages; \nupgrade: upgrades <package>")
parser.add_argument("package", help="the name of the AppImage you want to install.")

arguments = parser.parse_args()

print(arguments.action)

print(arguments.package)



if arguments.action == "install":
    



























































# url = "https://ocs-dl.fra1.cdn.digitaloceanspaces.com/data/files/1741562446/Luanti-5.15.0.AppImage?response-content-disposition=attachment%3B%2520Luanti-5.15.0.AppImage&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=RWJAQUNCHT7V2NCLZ2AL%2F20260424%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260424T165757Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=6ff441d4015db018ad77cc63e296558f23e99a0cbeb598d4197e7f81f436b179"

# response = requests.get(url)


# with open("lunati.Appimage", "wb") as file:
#     file.write(response.content)
 
# print("random game is here!")

