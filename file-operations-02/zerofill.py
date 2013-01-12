import os, shutil

FOLDER = '/Volumes/render/mango/brender/edit/graded_edit_final'
ROOT = 'graded_edit_final'
ZEROFILL = 9
#control = 0

for image in os.listdir(FOLDER):
	#print image
	old_name = os.path.join(FOLDER, image)
	ending = image.rsplit(ROOT)[1]
	#print ending
	if len(ending) < ZEROFILL:
		ending = ending.zfill(ZEROFILL)
		new_image_name = ROOT + ending
		new_name = os.path.join(FOLDER, new_image_name)
		print old_name, ">>", new_name
		
		os.rename (old_name, new_name)
		#control += 1

#print control