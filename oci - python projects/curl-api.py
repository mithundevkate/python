import shlex
import subprocess
cmd = '''curl -i -u mithundevkate:1d3215423883b399aefb137a15516cc237b7e923  https://api.github.com/user'''
args = shlex.split(cmd)
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, stderr = process.communicate()

print (stdout)
'''
for line in stdout:
    print (line),
'''
retval = process.wait()
