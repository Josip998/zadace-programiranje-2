#Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
#Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena.
#Nedovoljan 0-49%
#Dovoljan 50-65%
#Dobar 65-80%
#Vrlodobar 80-90%
#Izvrstan 90-100%

from csv import reader

def dodijeli_ocjenu(bodovi):
    try:
        bodovi = int(bodovi)
        if bodovi <= 49:
            return "nedovoljan"
        elif 50 <= bodovi <= 65:
            return "dovoljan"
        elif 65 <= bodovi <= 80:
            return "dobar"
        elif 80 <= bodovi <= 90:
            return "vrlodobar"
        else:
            return "izvrstan"
    except ValueError:
        pass
    except Exception:
        pass

with open('rezultati.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    ntorke = list(map(tuple, csv_reader))
    sortirano = sorted(ntorke, key=lambda tup: tup[1], reverse=True)
    print(sortirano)
    ocjene = []
    for student in ntorke:
        obj = dict()
        obj["ime"] = student[0]
        obj["prezime"] = student[1]
        obj["bodovi"] = student[2]
        obj["ocjena"] = dodijeli_ocjenu(student[2])
        ocjene.append(obj)
    print(ocjene)
