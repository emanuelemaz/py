nomi = ('Franco', 'Virgilio', 'Marco')
cognomi = ('Esposito', 'Bianchi', 'Distammo')

lista = []

for nome, cognome in zip(nomi, cognomi):
    lista.append({'nome': nome, 'cognome': cognome})

print(lista)