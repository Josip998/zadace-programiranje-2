import re

regexmail = "(^[a-z]+)[.]([a-z]+)([@]fpmoz[.]sum[.]ba$)"

while True:
    mail = input("Unesi mail:")
    result = re.match(regexmail, mail)
    if result:
        print("Uspjesno ste unijeli vas mail!")
        email = result.groups()
        break
    else:
     print("Neispravan unos maila.")
     
prvoslovoimena = email[0][0]
prezime = email[1]

regexeduid = "^"+prvoslovoimena+prezime+"(\d*[@]sum[.]ba$)"

while True:
    eduid = input("Unesi EduID:")
    result2 = re.match(regexeduid, eduid)
    if result2:
        print("ispravan unos eduida.")
        break
    else:
        print("Neispravan unos eduida.")

