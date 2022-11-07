def encode(text:str,key:str)->str:
    empty=''
    for i in range(len(text)):
        change=ord(key[i%len(key)])-96
        txt=(ord(text[i])-97+change)%26+97
        ky=chr(txt)
        empty+=ky
    return empty

def decode(text:str,key:str)->str:
    empty=''
    for i in range(len(text)):
        move=ord(key[i%len(key)])-96
        txt=(ord(text[i])-97-move)%26+97
        ky=chr(txt)
        empty+=ky
    return empty

print(encode('ahojsvet','kvet'))
print(decode('ldtddrjn','kvet'))