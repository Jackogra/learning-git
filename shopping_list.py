"""
Twoim zadaniem będzie założenie nowego repozytorium lokalnego o nazwie learning-git-task i wypełnienie go commitami.
Wróćmy do poprzedniego zadania wysłanego Mentorowi. Tego z listą zakupów.
Spróbujmy zrobić je ponownie, ale teraz zapisuj commit po każdej większej zmianie w pliku (zrób przynajmniej trzy). 
Po każdej komendzie w terminalu zapisz zrzut ekranu (najlepiej samego okna terminala).
Zatem posługując się wskazówkami z poprzednich submodułów, wykonaj następujące operacje:
Załóż nowe repozytorium lokalne o nazwie learning-git-task.
Zainicjuj w nim Gita.
Załóż odpowiedni plik.
Zrób commit z tytułem "Init project".
Zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <nazwa sklepu> i kupuję tam <lista produktów>.
Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą.
Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.X to sumaryczna liczba towarów, które są na listach.
Wyślij zrzuty ekranu swojemu Mentorowi.


shopping_list = {"piekarnia":["chleb", "bułki", "pączek", "rogal"],"warzywniak":["marchew", "seler", "por"]}
article_counter = 0

for shop, articles in shopping_list.items():
    shop_capital_letter = shop.capitalize()
    articles_capital_letter = [item.capitalize() for item in articles]
    print(f"Idę do {shop_capital_letter} i kupuję tam {articles_capital_letter}.")
    article_counter += len(articles_capital_letter)

print("W sumie kupuję " + str(articles_counter) + " produktów.\n")
"""

#Drogi Mentorze - Specjalne Pozdrowienia dla Ciebie ode mnie :D 
