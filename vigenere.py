#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:45:44 2019

@author: darshit
"""
print("hello")
choice = int(input("input 1 for encryption and 2 for decryption: "))

if (choice == 1):
    def vig(a,b,lena):
        encrypt = []
        for i in range(lena):
            moda = ((ord(a[i])+ord(b[i])-97)%26) + 97
            #print(moda)
            encrypt.append(chr(moda))
        print("encrypted text",encrypt)
    
    a = list(input("enter pt"))
    b = list(input("rnter key"))
    lena = len(a)
    lenb = len(b)
    
    atz = [chr(i) for i in range(97,123)]
    
    if lenb < lena:
        for i in range(lena-lenb):
            b.append(b[i])
            #print(b)
        vig(a,b,lena)
    elif lenb > lena:
        for i in range(lenb-lena,lenb):
            b.remove(b[i])
            #print(b) 
        vig(a,b,lena)
    else:
        vig(a,b,lena)    

elif (choice == 2):
    def vig(a,b,lena):
        decrypt = []
        for i in range(lena):
            moda = ((ord(a[i])-ord(b[i])-97)%26) + 97
            #print(moda)
            decrypt.append(chr(moda))
        print("encrypted text",decrypt)
    
    a = list(input("Enter cipher text: "))
    b = list(input("Enter key: "))
    lena = len(a)
    lenb = len(b)
    
    atz = [chr(i) for i in range(97,123)]
    
    if lenb < lena:
        for i in range(lena-lenb):
            b.append(b[i])
            #print(b)
        vig(a,b,lena)
    elif lenb > lena:
        for i in range(lenb-lena,lenb):
            b.remove(b[i])
            #print(b) 
        vig(a,b,lena)
    else:
        vig(a,b,lena)
        
else:
    print("wrong choice")
