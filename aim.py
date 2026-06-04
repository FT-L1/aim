#!/usr/bin/env python

# I would also like to mention, that the only reason this file is named "aim.py" 
# is because VS Code Syntax highlighting wouldn't work otherwise
# some day later on I'll remove the .py extension
import requests
import os
import argparse
import json
import shutil

# grabbing the username
username = os.environ.get("USER")


# getting the config
config = f"/home/{username}/.config/aim.json"
with open(config, "r") as file:
    configFileOptions = json.load(file)

# upstream default config. DO NOT MODIFY, write to /usr/share/aim/defaults.json instead
upstream_default = {
    "coreRepoEnabled" : True,
    "repos" : 
    {
        1 : "https://example.com/"
    },
    "imagedirDir" : f"/home/{username}/.local/share/aim/Appimages/",
    "imageDirRoot" : "/var/lib/aim/Appimages/",
    "configPathRoot" : "/etc/aim.json"
    
}
# global variables, such as the directory to install to and so on (per user)

imagedir = f"/home/{username}/.local/share/aim/Appimages/" 
desktopdir = f"/home/{username}/.local/share/applications/"
icondir = f"/home/{username}/.local/share/icons/hicolor/scalable/apps/"
infodir = f"/home/{username}/.local/share/aim/info/"
defaultconfig = "/usr/share/aim/defaults.json"
defaultexists = os.path.isfile(defaultconfig)


# check whether the paths for the user exist
if not os.path.exists(imagedir):
    print("WARNING: Appimage directory doesn't exist, creating..")
    os.makedirs(imagedir)

if not os.path.exists(infodir):
    print("WARNING: info directory doesn't exist, creating..")
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

# if you are a distributor, make sure these directories exist
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


# function for checking whether a file even exists
def fileExists(url):
    try:
        response = requests.head(url) # remember to put a timeout option here!!

        return response.status_code == 200
    except requests.RequestException:
        return False
    
# function for fetching a file
def fetchFile(url, destination):
    response = requests.get(url)

    with open(f"{destination}{arguments.package}.Appimage", "wb"):
        for chunk in response.iter_content(chunk_size=4096):
            file.write(chunk)


# the url with the repo, hopefully this will be more decentralized soon

url = "http://192.168.178.46/" # local ip of my laptop



# set up the arguments for parsing the input

parser = argparse.ArgumentParser(description="AppImage Manager (aim)")

parser.add_argument("action", choices=["install", "remove", "update", "upgrade", "fetch"], help="install: installs <package>; \nremove: removes <package>; \nupdate: updates ALL packages; \nupgrade: upgrades <package>")
parser.add_argument("package", help="the name of the AppImage you want to install.")

arguments = parser.parse_args()

print(arguments.action)

print(arguments.package)



if arguments.action == "install":
    print(f"Attempting to find {arguments.action}")

elif arguments.action == "remove":
    print(f"removing {arguments.package}")
    
    if os.path.isfile(f"{imagedir}/{arguments.package}.Appimage"):
        os.remove(f"{imagedir}/{arguments.package}.Appimage")
    else:
        print("WARNING: no such app in Appimage directory")
    
    if os.path.isfile(f"{desktopdir}/{arguments.package}.desktop"):
        os.remove(f"{desktopdir}/{arguments.package}-aim.desktop")
    else:
        print("WARNING: no such desktop entry in xdg desktop entry directory")

    if os.path.isfile(f"{icondir}/placeholdertest.svg"):     # note to self: remember to actually point to some icon path or name
        os.remove(f"{icondir}/placeholdertest.svg")
    else:
        print("WARNING: no such icon")

    if os.path.isfile(f"{infodir}/{arguments.package}.json"):
        os.remove(f"{infodir}/{arguments.package}.json")
    else:
        print("WARNING: no such info file")

    print(f"removed {arguments.package}")
elif arguments.action == "fetch":
    print(f"attempting to download {arguments.package} into working directory")

    if fileExists(f"{url}Appimages/{arguments.package}.Appimage"):     # make sure to actually add custom repositories here aswell
        fetchFile(f"{url}", os.getcwd())
    else:
        print("ERROR: file does not exist or server/network down")

