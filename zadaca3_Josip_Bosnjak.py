import re

unos = input(str("Unesi string:"))

p1 = re.search("^j", unos)

p2 = re.search("k$", unos)

p3 = re.search("[0-5]", unos)

p4 = re.search("\s", unos)

if p1 and p2 and p3 and p4:
           print("podudaranje!")

else:
           print("nema podudaranja.")
