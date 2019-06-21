#!/usr/bin/python3

# otevrit contributors.txt
# vypsat
# rozdelit na radky
# vypsat seznam
# ["prvni radek", "druhy radek" ...]
# odstranit prazdne radky ""

# odstranit radky zacinajici na "    "
# vypsat zbytek

#print("start")
#print("*")

print('"Name", "Commits"')
with open("contributors.txt") as f:
    data=f.readlines()
    #print(data)
    for line in data:
        line = line[:-1]
        if line.strip() =="": 
             continue
        if line[0:4] == "    ":
             continue 
        x=line.find("(")
        y=line.find(")")
        name=line[:x]
        cnt=line[x+1:y]
        #Spodni dva formaty delaji to same.
        #print('"{}",{}'.format(name, cnt))
        print('"' + name + '",'+cnt)

    
