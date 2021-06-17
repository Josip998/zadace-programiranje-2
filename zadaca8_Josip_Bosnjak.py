def prva_funkcija(ime):
    return "Pozdrav " + ime

unos = input("Unesite ime: ")
print(prva_funkcija(unos))

druga = lambda ime: "Dobrodošao " + ime
print(druga("Josip"))

def treca_funkcija(prva_funkcija):
    return prva_funkcija(unos)

print(treca_funkcija(prva_funkcija))

    
