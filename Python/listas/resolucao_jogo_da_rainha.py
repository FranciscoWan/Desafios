n_cartas = int(input('''    Quantas cartas terão na lista?
Digite um número de 1 a 52
Nº de castas: '''))

lista_cartas = [i for i in range(1, n_cartas+1)]

for i in range(n_cartas-1):
    print(f"A {i+1}º carta descartada foi a de número {lista_cartas[0]}.")
    lista_cartas.pop(0)
    lista_cartas.append(lista_cartas[0])
    lista_cartas.pop(0)
print(f"A carta remanescente foi a de número {lista_cartas[0]}.")
