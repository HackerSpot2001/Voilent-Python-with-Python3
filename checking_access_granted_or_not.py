#! /usr/bin/python3
import os 
filename = "new.txt"


# # print(file.write("This is from popen"))
# try:
#     with open(filename,"r") as f:
#         print(f.readlines())

# except IOError as e:
#     print("Problem :- {}".format(e))

# if not os.access(filename,os.R_OK):
#     print("Access Denied")
# else:
#     print("Access Granted")
#     with open(filename,"r") as f:
#         print(f.readline())
#         print(f.readline())
#         print(f.readline())
#         print(f.readline())
#         print(f.readline())
#         print(f.readline())
# if not os.path.isfile(filename):
#     print("This file doesnot Exists")
#     exit()
# # elif os.path.isfile(filename):
# #     print("This file is exists")
# #     exit()
# elif os.access(filename,os.R_OK):
#     print("Access granted")
#     exit()
# elif not os.access(filename,os.R_OK):
#     print("Access Denied")
#     exit()
# elif os.access(filename,os.R_OK):
#     print("Access granted")
#     exit()
# elif not os.access(filename,os.R_OK):
#     print("Access Denied")
#     exit()

# comm = "ls"
# file = os.popen(filename,'w')
# file = os.popen(comm,'w')
# file.write("This is from popen")



# Rename a file
os.rename(filename,"new123.txt")