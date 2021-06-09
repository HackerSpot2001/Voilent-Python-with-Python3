#!/usr/bin/python3
import crypt

# def text2hash_encryptor(text,file):
def text2hash_encryptor(passowrd_file):
    '''
    Create a Encrypt hash of an text 
    '''
    with open(passowrd_file,"r") as f:
        for word in f.readlines():
            word = word.strip('\n')
            text_to_hash = crypt.crypt(word)
            with open("output.txt","a+") as g:
                g.writelines(f"{word} : {text_to_hash}\n")
                return text_to_hash
        
def hash2text_decryptor(inp_hash):
    salted = inp_hash[0:2]
    with open("password.txt","r") as f:
        for word in f.readlines():
            word = word.strip("\n")
            cryptWord = crypt.crypt(word=word,salt=salted)
            if cryptWord == inp_hash:
                print("passowrd Found :- {}".format(word))
            else:
                print("Password NOt found")


if __name__ == "__main__":
    hashing = text2hash_encryptor("password.txt")
    hash2text_decryptor(hashing)