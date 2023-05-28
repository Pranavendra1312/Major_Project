import Huffman as hf
import RSA as rsa
import Vig_qw as vig
import LSB as lsb
import cv2
import os

# Project flow
# Plain text -> Vigenere -> RSA -> Huffman_encoding -> PLS-LSB

while(True):
    option=int(input("\n 1.Enter 1 for encoding \n 2.Enter 2 for decoding \n 3.Enter 3 to quit \n"))
    if(option==1):
        print("================================ ENCODING ==========================================")
        if os.path.exists("out.txt"):
            os.remove("out.txt")
        if os.path.exists("pls.txt.enc"):
            os.remove("pls.txt.enc")
        if os.path.exists("pls.txt"):
            os.remove("pls.txt")
        # if os.path.exists("images/out1.png"):
        #     os.remove("images/out1.png")
        plain_text=input("Enter plain text : ")
        print("")
        print("======================== VIGENERE ENCRYPTION ==================================")
        print("")
        key=input("Enter vigenere key : ")
        key=vig.generateKey(plain_text,key)
        Vig_encryp_text=vig.vig_encrypt(plain_text,key)
        print("Vigenere Cipher_text is: ",Vig_encryp_text)
        # print(vig.vig_decrypt(Vig_encryp_text,key))
        print("")
        print("======================== RSA ENCRYPTION ==================================")
       
        p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
        q = int(input(" - Enter another prime number (Not one you entered above): "))
        public,private=rsa.generate_key_pair(p,q)
        print("Public and Private keys are:",public,private)
        
        rsa_encryp_text=rsa.encrypt(public,Vig_encryp_text)
        print("RSA Cipher_text is : ",rsa_encryp_text)

    
        # print(rsa.decrypt(private,rsa_encryp_text))
        b='*'.join([str(elem) for elem in rsa_encryp_text])
        # print(b)
        print("")
        print("======================== HUFFMAN ENCODING ==================================")
        # print("")
        hf_enc,hf_tree=hf.HuffmanEncoding(b)
        # print(hf_tree)
        print("Cipher text after huffman encoding is :")

        print(hf_enc)
        print("======================== EMBEDDING USING PLS-LSB ==================================")
        if os.path.exists("images/in1.png"):
            lsb.LsbEncoding(hf_enc)
            if os.path.exists("pls.txt"):
                os.remove("pls.txt")
        else : 
            print("Image is not Present")

        
        # lsb.show_image(output_image,'ENCODED_IMAGE')
    elif(option==2):
        print("================================ DECODING ==========================================")
        print("")
        if os.path.exists("pls.txt.enc"):
            embedded_text = lsb.LsbDecoding()
                
        else :
            print("PLS file is not present !")
        
        print("======================== PLS-LSB DECODING==================================")
        print("")
        stego_image=input("Enter the name of the stego-image:")
        
        print("Huffman compressed text is:",embedded_text)
        x=hf.HuffmanDecoding(embedded_text,hf_tree)
        print("")
        print("======================== HUFFMAN DECODING==================================")
        print("")
        print("Huffman decoded text is",x)
        p=x.split('*')
        p=[int(elem) for elem in p]
        rsa_decryp_text=rsa.decrypt(private,rsa_encryp_text)
        print("======================== RSA DECRYPTION ====================================")
        print("")
        print("RSA decrypted text is",rsa_decryp_text)
        print("")
        print("====================== VIGENERE DECRYPTION ==================================")
        print("")

        key=input('Enter vigenere key :')
        print("")
        key=vig.generateKey(rsa_decryp_text,key)
        vig_decryp_text=vig.vig_decrypt(rsa_decryp_text,key)
        print("Obtained plain text is",vig_decryp_text)


    else :
        break


    





















