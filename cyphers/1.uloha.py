def encode(text:str,key:str)->str:
    result=''
    counter=-1
    temp=0
    for i in text:
        if i.isupper():
            temp=65
        elif i.islower():
            temp=97
        counter+=1    
        v1=(ord(key[counter%len(key)]))-97
        v2=(ord(i)-temp)
        change=(((v1+v2+1)%26)+temp)
        move=chr(change)
        if ord(i)==32:
            result+=' '
        else:
            result+=move
    return result

def decode(text:str,key:str)->str:
    result=''
    counter=-1
    temp=0
    for i in text:
        if i.isupper():
            temp=65
        elif i.islower():
            temp=97
        counter+=1    
        v1=(ord(key[counter%len(key)]))-97
        v2=(ord(i)-temp)
        change=(((v2-v1-1)%26)+temp)
        move=chr(change)
        if ord(i)==32:
            result+=' '
        else:
            result+=move
    return result

print(encode('Ahoj svet','kvet'))
print(decode('Ldtd oaye','kvet'))