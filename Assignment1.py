f1 = open("HP Lovecraft’s Beyond the Wall of Sleep.txt", "r",encoding="utf8").read()
f2 = open("Jane Austin’s Pride and Prejudice.txt", "r",encoding="utf8").read()
s=set(f2.split())
l=[]
for word in f1.split():
    if word in s:
        l.append(word)

print(l)
