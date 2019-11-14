# #!/usr/bin/env python
# Author : Mithun Devkate
# Version : 1.0

import requests
import json
import platform
import subprocess

## provide folder path to get repo cloned. Please provide OS specific formats
folder_path_to_clone = "C:\Personal\GitHub"

## call git API and pass he value for USER , ORG etc in api
r = requests.get('https://api.github.com/users/mithundevkate/repos')

# if all OK then start cloning bro !!!
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    for i in repoItem:
        ## Bill gates spotted :D
        if platform.system() == "Windows":
            process = subprocess.Popen('git clone %s %s\%s' % (i['clone_url'],i['name']) ,bufsize=2048, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.wait()
            if process.returncode == 0:
                print("Cloning done successfully in repository -->" , i['name'])
                continue

        ## Mother of ALL OS spotted :)
        else:
            process  = subprocess.Popen('git clone %s %s/%s' % (i['ssh_url'],i['name']) ,bufsize=2048, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.wait()
            if process.returncode == 0:
                print("Cloning done successfully in repository -->" , i['name'])
                continue

