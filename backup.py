import sys
import os
import subprocess
import argparse

#path to adb
bin = "adb.exe"

def main():
    
    parser = argparse.ArgumentParser(description="usage: backup.py [options] src dest", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("src", help="Source location")
    parser.add_argument("dest", help="Destination location")
    parser.add_argument("-s", "--show-only", action="store_true", help="Show number of files not in dest")
    parser.add_argument("-i", "--init", action="store_true", help="Init adb to discover devices")

    args = vars(parser.parse_args())

    if args["init"]:
        cmd = bin + " devices"
        print(subprocess.check_output(cmd).decode())
    
    ## Get files in local
    local_files = []
    for root, subfolder, files in os.walk(args["dest"]):
        local_files.extend(files)
    
    ## Generate file list from device
    cmd = bin + " shell (cd {0} && ls *.*)".format(args["src"])
    source_files = subprocess.check_output(cmd).decode()
    source_files = source_files.splitlines()

    ## Get files from device not in local
    files_to_update = []
    for file in source_files:
        if file not in local_files:
            files_to_update.append(file)

    print("files_to_update: {}".format(len(files_to_update)))

    if not args["show_only"]:
        for file in files_to_update:
            cmd = bin + " pull \"" + args["src"] + "/" + file + "\" " +  args["dest"]
            os.system(cmd)

if __name__ == "__main__":
    main()