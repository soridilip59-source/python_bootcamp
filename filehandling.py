

filehandle = open("diary.txt","w")

filehandle.write("I really like this session becauase it helps me learning  about python and I really want to learn python. \n")
filehandle
filehandle.close()

filehandle2 = open("diary.txt","r")

content = filehandle2.read()
print(content)

filehandle2.close()