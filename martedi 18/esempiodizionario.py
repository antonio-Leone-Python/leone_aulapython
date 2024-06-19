studente = {
    "età": 20,
    "sesso": "femmina",
    "nome" : "alice"

}

studente["città"]="roma"

print(studente.keys())# stampa solo le cose generiche 
print(studente.values())#stampa solo le cose specifiche 

print(studente.get("nome"))

