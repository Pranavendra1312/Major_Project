s='Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'
str=""
for i in s:
    if i!=' ':
        str=str+i

str=str+str.lower()

str=str+'`~!@#$%^&*()_-=+{}[]|;:"<>,.?/' + '0123456789'

qw=list(str)
dict={}
t=0
for i in qw:
    dict[i]=t
    t=t+1
##print(dict)
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def vig_encrypt(string, key):
    cipher_text = []
    for i in range(len(string)):
        # if(string[i]==' '):
        #     cipher_text.a
        x = dict[key[i]]
        x=x+dict[string[i]]
        x=x%92
        cipher_text.append(qw[x])
    return("" . join(cipher_text))
def vig_decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = dict[cipher_text[i]]
        x =((x-dict[key[i]])+92)%92
        orig_text.append(qw[x])
    return("" . join(orig_text))
##print(" ")
##
##print("==================Vigenere Encryption============================")
##print("")
##string=input("Enter plain text:")
##print("")
##key=input("Enter a key:")
##print("")
##key=generateKey(string,key)
### print("Key after padding is:",''.join(key))
### print("Cipher text is:")
##print("Cipher text is :",vig_encrypt(string,key))
##print("")
### print(' Decrypted  text is: ',vig_decrypt(vig_encrypt(string,key), key))
##
