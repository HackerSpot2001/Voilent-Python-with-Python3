#! /usr/bin/python3
# import zipfile
from zipfile import ZipFile
from tqdm import tqdm


# wordlist = "password.txt"
# filename = "BCA.zip"
# number_of_word = len(list(open(wordlist,"rb")))
# print("Total word in {}: {}".format(wordlist,number_of_word))
# with open(wordlist,"r") as word_list:
#     for word in tqdm(word_list,total=number_of_word,unit="word"):
#         with ZipFile(filename,"r") as file:
#             word = word.strip('\n')
#             try:
#                 file.extractall(pwd=bytes(word,'utf-8'))
#                 print("password Found:- {}".format(word.decode()))
#             except zipfile.error as e:
#                 print(e)
