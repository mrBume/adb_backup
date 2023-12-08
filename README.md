# adb_backup
Simple python script that use adb to backup smartphone files

This program is intended to backup Android files in a computer using debug mode.
The smartphone shall be connected to computer thought USB to allow higher transfer speeds.

__Adb.exe__ should be installed in the computer in order to use this program.

The program will compare the files in __src__ agains __dest__, and will copy all the files not present in __dest__.

usage:

    python backup.py src dest

- ***src***:  path to files in android. Example "sdcard/DCIM/Camera"
- ***dest***: path to backup files. Example "D:/Photos"
