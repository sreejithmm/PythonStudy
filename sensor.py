def censor (text, word):
    new = ""
    for item in text.split():
        print item 
        if item  == word:
            new += "****"
            new += " "
        else:
           new += item 
           new += " "
    return new

print censor("hey hey hey","hey")
