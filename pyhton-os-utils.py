# Created on Jul 24, 2013

# @author: tuna

import os
import shutil
import subprocess

print("Current Working Directory", os.getcwd())
print("Getting JAVA_HOME env variable", os.getenv("JAVA_HOME"))

# remove a directory with its content and ignore errors =True
shutil.rmtree("/tmp/pythonexample/", True)

# creating a directory with 777 permission
os.mkdir("/tmp/pythonexample/", 0o0777)

# listing directory
direc = os.listdir("/tmp/")

# file name listing inside /tmp
for currfile in direc:
    print(currfile)

# copy directory tree
shutil.copytree("/home/tuna/Downloads", "/tmp/pythonexample/tmpbackup")

print(os.listdir("/tmp/pythonexample/tmpbackup"))

# calling xterm as subprocess
subprocess.call("/usr/bin/xterm")
