import csv
#---#---#---#---#

reader = csv.reader(open("db.csv"), delimiter =";")

dictFermate = {0: 'Casarene (Squibb)', 1: 'Osteria della Fontana', 2: 'Fontana Ceraso', 3: 'Pantanello', 4: 'Tofe Pistone', 5: 'Quattro strade', 6: 'Sub Nord', 7: 'Sub Sud', 8: 'Porta S. Francesco', 9: 'S. Giorgetto', 10: 'Cantina Sociale', 11: 'Osteria La Noce', 12: 'Via Casilina, km. 67', 13: 'Strada Provinciale Anagni/Ferentino (Muraglione)', 14: 'Cardinali', 15: 'Tufano', 16: 'Vallevona', 17: 'Bivio Morolo', 18: 'Fosso del Lupo', 19: 'Piscina', 20: 'Vignola', 21: 'S. Bartolomeo', 22: 'Faito', 23: 'Ponte Piano', 24: 'Cimitero', 25: 'Via Casalotto', 26: 'Via Collacciano', 27: 'F. Ceraso', 28: 'Bivio Fiuggi (Coop)', 29: 'Prato', 30: 'Strada Regionale Anticolana', 31: 'Bivio S. Filippo', 32: 'Strada Provinciale Anagni/Acuto', 33: 'Ponte delle Cavatole', 34: 'Acqua Cetosa', 35: 'Monti', 36: 'S. Filippo', 37: 'Ristorante La Rena', 38: 'Via Casilina, km.68', 39: 'Via Madonna delle Grazie', 40: 'Via Madonna di Tufano', 41: 'Cava S. Magno', 42: 'Impianti Sportivi', 43: 'Centro Storico', 44: 'Viale Roma', 45: 'Via Cerere Navicella', 46: 'Cucugnano', 47: 'Via Ponte del Papa', 48: 'Strada Ricci', 49: 'V. Bagnara', 50: 'V.P. Sabatino', 51: 'Via Fucigno', 52: 'Via La Sassera', 53: 'Bivio Ricci', 54: 'Stazione FS', 55: 'Via Rotabile S. Francesco', 56: 'Viale G. Matteotti', 57: 'Collegio Leoniano', 58: 'Ex Tribunale', 59: 'Ufficio Postale', 60: 'Porta S. Maria', 61: 'Via V. Emanuele', 62: 'Porta Cerere', 63: 'Convitto R. Margherita', 64: 'Ist. Tecnico', 65: 'Bar Rossi'}

def stampabene(dictFermate):
    print("Fermate/ID:")
    for ID, fermate in dictFermate.items():
        print("{} ({})".format(ID, fermate))

stampabene(dictFermate)

f = int(input("\nDigita il numero della fermata che ti interessa: "))

print("\n")

ff = dictFermate.get(f, 0)

print("\n[Orario, Giorni, Percorso]\n")

for riga in reader:
    if any(ff in s for s in riga):
        print(str(riga) + "\n")

input('\nPremi INVIO per uscire.')