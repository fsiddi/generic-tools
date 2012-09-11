import shutil
import os

FOLDER = "/shared/development/shots_all/shots_day5/"
machines = []
files = []

for dirname, dirnames, filenames in os.walk(FOLDER):
    
    for subdirname in dirnames:
        increment = 1
        #print os.path.join(dirname, subdirname)
        filecount = len(os.listdir(os.path.join(dirname, subdirname)))
        fill_lenght = len(str(filecount))
        # print fill_lenght
        # print filecount
        # print os.path.join(dirname, subdirname)
        
        
        
        for file in os.listdir(os.path.join(dirname, subdirname)):
            root = file.rsplit("_")[0]
            # print "---"
            # print str(increment).zfill(fill_lenght)
            src_file = dirname + subdirname + "/" + file
            dst_file = dirname + subdirname + "/" + root + "_" + str(increment).zfill(fill_lenght) + ".png"
            
            print src_file + " >> " + dst_file
            
            os.rename (src_file, dst_file)
            
            increment += 1
            