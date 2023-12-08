import sys
import os
import subprocess

#path to adb
bin = "adb.exe"

def main(argv):
    source_dir = argv[1]
    output_dir = argv[2]

    ## Get files in local
    local_files = []
    for root, subfolder, files in os.walk(output_dir):
        local_files.extend(files)
    
    ## Generate file list from device
    cmd = bin + " shell ls " + source_dir
    source_files = subprocess.check_output(cmd).decode()
    source_files = source_files.splitlines()

    ## Get files from device not in local
    files_to_update = []
    for file in source_files:
        if file not in local_files:
            files_to_update.append(file)

    print("files_to_update: {}".format(len(files_to_update)))

    for file in files_to_update:
        cmd = bin + " pull \"" + source_dir + "/" + file + "\" " +  output_dir
        # print(cmd)
        os.system(cmd)

if __name__ == "__main__":
    main(sys.argv)