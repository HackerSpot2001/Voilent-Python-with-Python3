#!/usr/bin/python3
import patoolib
# from zipfile import ZipFile

# Extract Zip File using zipfile
# with ZipFile("new2.zip","r") as zfile:
#     zfile.printdir() # to See the files in zip 
#     zfile.extractall()

# Create a Zip using 
# with ZipFile("new2.zip","w") as file:
#     file.setpassword(pwd=bytes("teena","utf-8"))
#     file.write("password.txt")
#     print("{} was created".format(file))


# Write files in a zip 
# with ZipFile("new.zip","w") as file:
#     file.write("banner.py")
#     file.printdir()


# Append File in Zip
# with ZipFile("test.zip","a") as file:
#     file.printdir()
#     file.write("new.zip")
#     file.printdir()


# Extract Files using Password
# with ZipFile("new.zip","r") as file:
#     file.setpassword(bytes("teena","utf-8"))
#     file.extractall()


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


# Zip Creation using Patool Module



# # patoolib.create_archive("BCA.zip",("test.py","output.txt","password.txt"))
patoolib.extract_archive(archive="rockyou.txt.gz",outdir="rocky.txt")
