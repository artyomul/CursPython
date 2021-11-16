# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

lista_elemente = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista_elemente)

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

ascendent_list = lista_elemente.copy()
ascendent_list.sort()
print(ascendent_list)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

descendent_list = lista_elemente.copy()
descendent_list.sort(reverse=True)
print(descendent_list)

# afișarea numerelor cu indici pari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

lista_para = ascendent_list[1::2]
print(lista_para)

# afișarea numerelor cu indici impari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

lista_inpara = ascendent_list[::2]
print(lista_inpara)

# afișarea elementelor multipli ai lui 3.

lista_multipli = ascendent_list[2::3]
print(lista_multipli)
