def anti_vowel(text):
    str=""
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    for i in range(0,len(text)):
        isit=text[i] in vowels
        if(isit== False):
            str+=text[i]
    return str

print anti_vowel("AeroPlane")

