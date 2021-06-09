#!/usr/bin/python3
import sys
from time import sleep
from PyPDF2 import PdfFileReader
from threading import Thread, ThreadError
from tqdm import tqdm

def pdf_Brute(pdfFile,passwd):
    print("[*] Testing Password: {}".format(passwd))
    pdfReader = PdfFileReader(pdfFile)
    ret = pdfReader.decrypt(passwd)
    if ret == 1:
        print("Login Succesfull With: {}".format(passwd))
        
    else:
        pass

if __name__ == "__main__":
    # print("*"*60)
    # print("  >>>>>>>>>\tPDF Password Brute-Forcer\t>>>>>>>>>")
    # print("*"*60+"\n")
    # pdf = str(input("Enter PDF <File or Path> :- "))
    # wordList = str(input("Enter Wordlist <File or Path> :- "))
    # with open(wordList,"r") as f:
    #     passwords = f.readlines()
    #     number_of_words = len(passwords)
    #     for password in tqdm(passwords,desc="Testing Passwords:- ",total=number_of_words):
    #         password = password.strip("\n")
    #         pdf_Brute(pdf,password)
    #         thread_object = Thread(target=pdf_Brute,args=(pdf,password))
    #         thread_object.start()
    #         if get_pass:
    #             sys.exit()
    #         # if ThreadError:
    #         #     sleep(0.04)

    print("*"*60)
    print("  >>>>>>>>>\tPDF Password Brute-Forcer\t>>>>>>>>>")
    print("*"*60+"\n")
    pdf = str(input("Enter PDF <File or Path> :- "))
    wordList = str(input("Enter Wordlist <File or Path> :- "))
    with open(wordList,"r") as f:
        for password in f.readlines():
            password = password.strip("\n")
            pdf_Brute(pdf,password)