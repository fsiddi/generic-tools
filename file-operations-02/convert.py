import subprocess
import os
import shutil

FOLDER = "/shared/mango/weeklies/"

for dirname, dirnames, filenames in os.walk(FOLDER):
    print filenames