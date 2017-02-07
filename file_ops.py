file = open("countries.txt")

countries = []
for line in file :
	line = line.strip()
	countries.append(line)
file.close()
print (countries)
print (len(countries))

for country in countries :
	if (country[0] == 'T') :
		print (country)

string = raw_input("Enter the string you want to append to file >")

print("read the string")
file = open("Test.txt","w")
file.write(string+"\n")
file.close()