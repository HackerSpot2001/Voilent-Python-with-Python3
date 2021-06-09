#! /usr/bin/python3
import hashlib

def encryptHash(text):
    encryptedHash1 = hashlib.sha512(text.encode()).hexdigest()
    # print("{} :- {}".format(text,encryptedHash1))
    return encryptedHash1
    # encryptedHash2 = hashlib.md5(text).hexdigest()
    # print(f"SHA512 :- {encryptedHash1}")
    # print(f"MD5  :- {encryptedHash2}")

def decryptHash(encryptHash,passfile):
    with open(passfile,"r") as f:
        for word in f.readlines():
            word = word.strip("\n")
            encryptWord = hashlib.sha512(word.encode()).hexdigest()
            if encryptWord == encryptHash :
                print("Password Found := {}".format(word))


# SHA512 :- 3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79
# MD5  :- 827ccb0eea8a706c4c34a16891f84e7b

if __name__ == "__main__":
    hashWOr = encryptHash("123456")
    decryptHash(hashWOr,"password.txt")