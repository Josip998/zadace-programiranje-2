#Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)


import random


def random_ocjena():
    return random.randint(1, 5)


lista = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa',
         'Marko', 'Dario', 'Mihael',
         'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon',
         'Ivan', 'Ante', 'Ivan',
         'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip',
         'Tomislav', 'Luka', 'Ivan',
         'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka',
         'Ana', 'Emanuel',
         'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante',
         'Marijan', 'Mario',
         'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas',
         'Ivan', 'Freda', 'Kristina',
         'Josip', 'Lucija']

ocjene = dict()

for ime in lista:
    ocjene[ime] = random_ocjena()

broj_ocjena = dict()
pozitivne_ocjene = 0

for student in ocjene:
    print("Student: %s | Ocjena: %d" % (student, ocjene[student]))
    ocjena = ocjene[student]
    if ocjena > 1:
        pozitivne_ocjene += 1
    if ocjena in broj_ocjena:
        broj_ocjena[ocjena] += 1
    else:
        broj_ocjena[ocjena] = 1

for ocjena in broj_ocjena:
    print("Ocjena %d se pojavljuje %d puta" % (ocjena, broj_ocjena[ocjena]))

print("Pozitivne ocjene: %d" % (pozitivne_ocjene))
print("Prolaznost: %d%%" % ((pozitivne_ocjene / len(ocjene)) * 100))
