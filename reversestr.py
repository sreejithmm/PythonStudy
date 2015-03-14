def reverse(text):
    rev=""
    for i in range(0,len(text)):
        rev += text[len(text)-1-i]         
    return rev

print reverse("hai")
