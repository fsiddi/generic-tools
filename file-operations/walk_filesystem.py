import os

FOLDER = '/Users/fsiddi/Desktop/folder'

def source_list(path, filename_check=None):
   for dirpath, dirnames, filenames in os.walk(path):
        
      #skip svn
      if dirpath.startswith("."):
         continue
        
      for filename in filenames:
         filepath = join(dirpath, filename)
         if filename_check is None or filename_check(filepath):
               yield filepath

def is_exr(filename):
   ext = splitext(filename)[1].lower()
   return (ext == ".exr")

# fi = list(source_list(PATH_TO_EXR, filename_check=is_exr))
    

#for dirpath, dirnames, filenames in os.walk(FOLDER):
   #print filenames
   #for subdirname in dirnames:
   #print os.path.join(dirname, subdirname)
   #for filename in filenames:
   #print os.path.join(dirname, filename)
   

for dirpath, dirnames, filenames in os.walk(FOLDER):
    for subdirname in dirnames:
        print os.path.join(dirpath, subdirname)
        print subdirname
        subpath = os.path.join(dirpath, subdirname)
        for dirpath, dirnames in filenames in os.walk(subpath):
           print "subdir"
        
    for filename in filenames:
        print os.path.join(dirname, filename)
        print "moar hello"
