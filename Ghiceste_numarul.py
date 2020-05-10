import random
counting = 0
incercari = 10
elem_indroduse_de_jucator = []
numar_trebu_ghicit = random.randint(0, 100)
print(f"Bun venit acesta este o mica joaca dumneavostra aveti {incercari} ca sa ghiciti numarul care este ascuns ")
while True:
    if incercari < 10:
        print(f"Va informez ca acesata a fost {counting} incercare 🙂")
    elif incercari == 1:
        print("Aceasta este ultima incercare 🙂 ")
    numar_introdus = int(input("Introdu numarul care credeti ca este"))
    elem_indroduse_de_jucator.append(numar_introdus)
    incercari -= 1
    counting += 1
    if numar_introdus == numar_trebu_ghicit:
        print("felicitari")
        print(f"Ati ghicit din {counting} incercare")
        break
    if numar_introdus < numar_trebu_ghicit:
        print("Un pic mai mult")
    elif numar_introdus < numar_trebu_ghicit:
        print("Un pic mai putin")
    if incercari == 0:
        print("Game Over")
        break
    lista = []
    for masivcik in elem_indroduse_de_jucator:
        lista.append(masivcik)
        lista_finala = lista
    if incercari == 3:
        print(f"Mai aveti {incercari} incercari posbil va ajuta {lista_finala}")
        par=numar_trebu_ghicit/2
        if par==float:
            print("Acesta este par")
        else:print("Nu este par")