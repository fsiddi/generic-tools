import shutil
import os

FOLDER = "/shared/development/shots_all/shots_day5/"
machines = []
files = []

for file in os.listdir(FOLDER):
    files.append(file)

for file in files:
    machine_name = file.rsplit("_")[0]
    print machine_name
    machines.append(machine_name)

print "----"

machines = set(machines)
for machine in machines:
    print FOLDER + machine
    os.mkdir (FOLDER + "/" + machine)
    
    for file in files:
        if file.startswith(machine + "_"):
            src_file = FOLDER + file
            dst_folder = FOLDER + machine + "/."
            print src_file + " >> " + dst_folder
            shutil.move(src_file, dst_folder)