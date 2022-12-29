import re
def validemail(email):
    if(re.match(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",email)):
        return "valid email "+email
    else:
        return "not valid email "+email
file1=open("file.txt",'r')
while True:
         line=file1.readline()
         if line=="":
            break
         line=line[:1]
         print(validemail(line))
file1.close()   