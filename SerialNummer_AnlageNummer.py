def a():
    q = True
    li = []
    s_n_lange = int(input("Gib die länge des Seriennummers: "))
    a_n_lange = int(input("Gib die länge des Anlagenummers: "))

    while q is True:
        s_nummer = input("Seriennummer: ")
        while len(s_nummer) < s_n_lange:
            if s_nummer[0] == "Ü":
                with open('serialnummer und anlagenummer.csv', 'w') as f:
                    for i in range(len(li)):
                        text1 = li[i][0]
                        text2 = li[i][1]
                        f.write(text1)
                        f.write(";")
                        f.write(text2)
                        f.write("\n")
                q = False
                return q
            print("Seriennummer ist zu kurz. Bitte nochmal scannen.")
            s_nummer = input("Seriennummer: ")
        a_nummer = input("Anlagenummer: ")
        if len(a_nummer) < a_n_lange:
            print("Anlagenummer ist zu kurz. Bitte nochmal scannen.")
            s_nummer = input("Seriennummer: ")
        li.append([s_nummer, a_nummer])
        print(li)


if __name__ == '__main__':
    print("Die Buchstabe Ü brecht den Programm ab und speichert die Liste!")
    a()
