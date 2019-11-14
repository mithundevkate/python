import requests
import json
import platform
import subprocess


## provide folder path to get repo cloned. Please provide OS specific formats
folder_path_to_clone = "C:\Personal\GitHub"

## call git API
r = requests.get(' https://api.github.com/users/mithundevkate/repos')

''''
git_list_win = []
git_list_nonwin = []
repo_name = []
'''

# if all OK then start cloning bro !!!
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    for i in repoItem:
        '''
        print ("Repo_name-->", i['name'])
        if (i['private'] == False):
            print("Public Repo --> Yes")
        print("SSH clone url -->", i['ssh_url'])
        print("HTTPS clone url -->", i['clone_url'])
        '''

        ## Bill gates spotted :D
        if platform.system() == "Windows":
           # git_list_win.append(i['clone_url'])
            #repo_name.append(i['name'])
            process = subprocess.Popen('git clone %s C:\Personal\GitHub\%s' % (i['clone_url'],i['name']) ,bufsize=2048, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.wait()
            if process.returncode == 0:
                print("Cloning done successfully in repository -->" , i['name'])
                continue

        ## Mother of ALL OS spotted :)
        else:
            #git_list_nonwin(i['ssh_url'])
            #epo_name.append(i['name'])
            process  = subprocess.Popen('git clone %s C:\Personal\GitHub\%s' % (i['ssh_url'],i['name']) ,bufsize=2048, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.wait()
            if process.returncode == 0:
                print("Cloning done successfully in repository -->" , i['name'])
                continue

