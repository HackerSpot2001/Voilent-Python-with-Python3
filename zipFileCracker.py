#! /usr/bin/python3
from zipfile import ZipFile
from threading import Thread
import optparse
import sys

# def extractFIle(zfile,password):
#     try:
#         with ZipFile(zfile,"r") as file:    
#             file.extractall(pwd=bytes(password,"utf-8"))
#             print("Password Found :- {}".format(password))
#     except Exception as e:
#         print(e)

# def mainFunction():
#     parser = optparse.OptionParser("usage%prog "+"-f <zipfile> -d <dictionary>")
#     parser.add_option("-f",dest="zname",type="string",help="specify zip file")
#     parser.add_option("-d",dest="dname",type="string",help="specify dictionary file")
#     option,args=parser.parse_args()
#     if (option.zname == None) | (option.dname == None) :
#         print(parser.usage)
#         exit(0)

#     else:
#         zname = option.zname
#         dname = option.dname
#         with open(dname,"r") as passFile:
#             for line in passFile.readlines():
#                 password = line.strip("\n")
#                 t = Thread(target=extractFIle,args=(zname,password))
#                 t.start()




'''
Our Main Script

def extractFIle(zfile,password):
    try:
        with ZipFile(zfile,"r") as file:    
            file.extractall(pwd=bytes(password,"utf-8"))
            print("Password Found :- {}".format(password))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    usage = "python3 zipFileCracker.py zipFile wordlist"
    if len(sys.argv) !=3:
        print(usage)
        sys.exit()
    
    zipfile = sys.argv[1]
    wordlist = sys.argv[2]
    with open(wordlist,"r") as passFile:
        for line in passFile.readlines():
            password = line.strip("\n")
            t = threading.Thread(target=extractFIle,args=(zipfile,password))
            t.start()

'''




"""

###########################
#                         #
#    Testing Purpose      #
#                         #
###########################



def zip_password_cracker(zip_file,pass_file):
    with ZipFile(zip_file,"r") as file:
        with open(pass_file,"r") as passFIle:
            for word in passFIle.readlines():
                word = word.strip('\n')
                password = file.extractall(pwd=bytes(word,'utf-8'))
                if not password:
                    print("Password not Successfully Cracked :- {} ".format(word))
                else:
                    print("Password Cracked successfully :- {}".format(word))

                    
if __name__ == "__main__":
    usage = "python3 zip_file_password_cracker.py zip_file pass_file"
    if len(sys.argv) !=3:
        print(usage)
        sys.exit()
    
    try:
        filename = sys.argv[1]
        passFile = sys.argv[2]
        zip_password_cracker(filename,passFile)
    except Exception as e:
        print(e)

"""



"""
usage = "python3 zip_pass_cracker.py zip_file pass_file"
if len(sys.argv) != 3:
    print(usage)
    sys.exit()

filename = str(sys.argv[1])
print(filename)
passFile = str(sys.argv[2])
print(passFile)
with ZipFile(filename,"r") as file:
    with open(passFile,"r") as pass_file:
        for word in  pass_file.readlines():
            word = word.strip('\n')
            if  (file.setpassword(pwd=bytes(word,"utf-8"))):
                print("Password Found :- {}".format(word))
            # if not password1 :
            #     print("Password not found :- {}".format(word))
"""
