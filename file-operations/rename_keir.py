import fnmatch
import os
import glob
import sys
import collections

file_tree = collections.defaultdict(set)
for filename in glob.glob('*.exr'):
  file_tree[filename[:4]].add(filename)

if not file_tree:
  print 'error: no files to move.'
  sys.exit(1)

for root_filename, filenames in file_tree.iteritems():
    print "Making directory ", root_filename, " in ", os.getcwd()
    # os.mkdir(root_filename)
    for filename in filenames:
        new_filename = os.path.join(root_filename, filename)
        print "Renaming ", filename, " to ", new_filename
        # os.rename(filename, new_filename)
