import os

working_directory = os.path.abspath('./python')

for filename in os.listdir(working_directory):
    print filename + " -> " + filename + ".exr"
    filepath = os.path.join(working_directory, filename)
    os.rename(filepath, filepath + ".exr")