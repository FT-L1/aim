import requests
import os

from tqdm import tqdm

url = "https://rpmfind.net/linux/opensuse/tumbleweed/repo/oss/x86_64/bash-5.3.9-6.3.x86_64.rpm"
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

# progress bar :3
with tqdm(total=total_size, unit='iB', unit_scale=True) as bar:

    with open("bash.rpm", "wb") as f:

        for chunk in response.iter_content(chunk_size=1024):

            f.write(chunk)
            bar.update(len(chunk))

