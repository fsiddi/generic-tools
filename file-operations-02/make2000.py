import subprocess
import os
import shutil

FOLDER = "/Volumes/render/mango/cleaned"
FOLDER_NEW = "/Volumes/render/mango/cleaned_jpeg2000"

for dirname, dirnames, filenames in os.walk(FOLDER):
    for filename in filenames:
        if "/linear" in dirname:
            filename_src = os.path.join(dirname, filename)
            dirname_dst = dirname.replace(FOLDER, FOLDER_NEW)
            if filename.endswith(".png"):
                if not os.path.exists(dirname_dst):
                    os.makedirs(dirname_dst)
                filename_jpg = filename.replace(".png", ".jpg")
                filename_dst = os.path.join(dirname_dst, filename_jpg)
                print filename_src + " >> " + filename_dst
                subprocess.call(["convert", filename_src, "-resize", "1280x1280", filename_dst])
            elif filename.endswith(".jpg"):
                if not os.path.exists(dirname_dst):
                    os.makedirs(dirname_dst)
                filename_dst = os.path.join(dirname_dst, filename)
                print filename_src + " >> " + filename_dst
            #subprocess.call(["convert", filename_src, "-resize", "1280x1280", filename_dst])
        else:
            print "skipping " + dirname