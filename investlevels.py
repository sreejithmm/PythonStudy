import re

nomediapattern = r"(\<Media omitted\>)"
regexMedia = re.compile(nomediapattern, flags=re.M)

dateAndTimepattern = r"((\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)\s\+[0-9 ]+(:).*)"
regexDate = re.compile(dateAndTimepattern, flags=re.M)

sreejithpattern = r"((\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)\s?sreejith\s?mm:\s.*)"
regexSreejith= re.compile(sreejithpattern, flags=re.M)

nareshpattern = r"((?i)(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)\s?Naresh:\s.*#Query.*)"
regexNaresh = re.compile(nareshpattern, flags=re.M)





fp = open("investlevels.txt")

text = fp.read()


fp.close()



#print(text)

chatText = regexMedia.sub("", text)
chatText = regexDate.sub("", chatText)

chatText = regexSreejith.sub("", chatText)


#print(chatText)


chatText = re.findall(nareshpattern,chatText)

wfp = open("onlylevels.txt","w")
for levels in chatText:
    print(levels[0])
    wfp.write(levels[0])
    wfp.write("\n")


wfp.close()



