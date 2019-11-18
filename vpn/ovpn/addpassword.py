#!/usr/bin/python3
import os
import re
from shutil import copyfile
from urllib.request import urlopen
from zipfile import ZipFile

print("Please make sure you added pass.txt to this dorectory")
input("Press enter to continoue or ctrl+c to exit")

ovpn_certs_url = "https://www.privateinternetaccess.com/openvpn/openvpn.zip"

# Got this code from https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/
zipurl = ovpn_certs_url
    # Download the file from the URL
zipresp = urlopen(zipurl)
    # Create a new file on the hard drive
tempzip = open("/tmp/tempfile.zip", "wb")
    # Write the contents of the downloaded file into the new file
tempzip.write(zipresp.read())
    # Close the newly-created file
tempzip.close()
    # Re-open the newly-created file with ZipFile()
zf = ZipFile("/tmp/tempfile.zip")
    # Extract its contents into <extraction_path>
    # note that extractall will automatically create the path
zf.extractall(path = '.')
    # close the ZipFile instance
zf.close()

ovpn_files = []
for i in os.listdir('.'):
    if "ovpn" in i:
        ovpn_files.append(i)
print(ovpn_files)
for i in range(len(ovpn_files)):
    #Thanks to this site for the help https://pythonexamples.org/python-replace-string-in-file/
    new_directory = "VPN" + f"{i:03d}"
    fin = open(ovpn_files[i], "rt")
    data = fin.read()
    data = data.replace("auth-user-pass", "auth-user-pass "+"/etc/openvpn/"+new_directory+"/pass.txt")
    fin.close()

    fin = open(ovpn_files[i], "wt")
    fin.write(data)
    fin.close()
    os.mkdir(new_directory)
    os.rename("./"+ovpn_files[i], "./"+new_directory+"/"+ovpn_files[i])
    try:
        copyfile("./pass.txt",  "./"+new_directory+"/"+"pass.txt")
    except:
        print("No pass.txt available")
