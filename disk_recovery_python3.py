
# Monday, 11 July 2016
# Python Script to Recover Deleted Files And Partitions
# Ever deleted a file permanently and wished to recover it. Here's a python script designed to do this task in Linux operating system.

# When this script works
# File is deleted and that space is not used for any other file
# When you quick format your storage device

# When this doesn't work
# When file is deleted and space is used to store another file. 
# When you format your storage device

# Dependencies
# For partition recovery fdisk(usually comes pre-installed in a modern distro)
# For file recovery sleuthkit
# Alternatives
# Here is a list of software that I personally use to recover files when necessary. Though now I would prefer my own script.
# Linux: Photorec Command Line Tool
# Windows: Recuva GUI Tool

# Script for Partition Recovery
import os
print ("Partion Recovery Script-Abhishek Munagekar")
print ("List of devices attached to system is")
os.system("lsblk")
devname=raw_input("Enter the device name\n")
#show the list of partition
commandline='echo -e "p\nq\n" | fdisk /dev/'+devname 
print ("Showing partition table")
os.system(commandline)

pno=raw_input("Enter the partition no to recover ")
#delete the partition
commandline='echo -e "n\n\n' + pno +'\n\n\nw\n" | fdisk /dev/'+devname 
os.system(commandline)