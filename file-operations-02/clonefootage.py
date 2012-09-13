import subprocess
import os
import shutil

FOLDER_SRC = "/Users/fsiddi/Desktop/clonefootage/footage_src"
FOLDER_DST = "/Users/fsiddi/Desktop/clonefootage/footage_dst"


for dirname, dirnames, filenames in os.walk(FOLDER_SRC):
	for filename in filenames:
		if "linear_hd" in dirname:
			filename_src = os.path.join(dirname, filename)
			dirname_dst = dirname.replace(FOLDER_SRC, FOLDER_DST)
			''''if filename.endswith(".png"):
				if not os.path.exists(dirname_dst):
					os.makedirs(dirname_dst)
				filename_jpg = filename.replace(".png", ".jpg")
				filename_dst = os.path.join(dirname_dst, filename_jpg)
				print filename_src + " >> " + filename_dst
			elif filename.endswith(".jpg"):
				if not os.path.exists(dirname_dst):
					os.makedirs(dirname_dst)
				filename_dst = os.path.join(dirname_dst, filename)
				print filename_src + " >> " + filename_dst'''
			if filename.endswith(".exr"):
				if not os.path.exists(dirname_dst):
					#pass
					os.makedirs(dirname_dst)
				filename_dst = os.path.join(dirname_dst, filename)
				print filename_src + " >> " + filename_dst
				shutil.copy(filename_src, filename_dst)
			else:
				pass
			#subprocess.call(["convert", filename_src, "-resize", "1280x1280", filename_dst])
		else:
			print "skipping " + dirname