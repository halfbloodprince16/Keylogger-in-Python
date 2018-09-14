with open("file.log", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
s =""
for i in array :
	s=s+i.rstrip("\n")
	
s = s.replace("space"," ")
s = s.replace("Return","\n")

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

x = int(find_str(s,"BackSpace"))
s = s[:x-1]+s[x:]
s = s.replace("BackSpace","")



txt = open("text.txt","a")
txt.write(s)
txt.close


try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
with open("text.txt") as f:
	for lines in f:	 	
		for j in search(lines, tld="co.in", num=5, stop=1, pause=2): 
		    print(j)


