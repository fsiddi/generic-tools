import fnmatch
import os

root_filenames = set()
working_directory = os.path.abspath('./python')
print working_directory

for filename in os.listdir(working_directory):
    #  take care only of exr files
    if fnmatch.fnmatchcase(filename, '*.exr'):
        root_filenames.add(filename[:4])
    #print filename

for root_filename in root_filenames:
    print "Making directory " + root_filename + " in " + working_directory
    os.mkdir(working_directory + '/' + root_filename)
    for filename in os.listdir(working_directory):
        if fnmatch.fnmatch(filename[:4], root_filename) and fnmatch.fnmatchcase(filename, '*.exr'):
            full_path = os.path.join(working_directory, filename)
            new_path = os.path.join(working_directory, root_filename + '/' + filename)
            #print file
            print "moving " + full_path + " into " + new_path         
            os.rename(full_path, new_path)
