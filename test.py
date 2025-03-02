import requests
import os

# Ensure the directory exists
download_dir = "downloaded_files"
os.makedirs(download_dir, exist_ok=True)

with open("C:/Users/nishi/Desktop/web-vuln-scanner/downloaded_files/urls.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    response = requests.get(url)
    
    if response.status_code == 200:
        filename = os.path.join(download_dir, url.split("/")[-1])
        
        with open(filename, "wb") as f:
            f.write(response.content)
        
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url} (Status Code: {response.status_code})")
