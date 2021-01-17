def seriennummer():
    # This will guide the user to choose option
    print("Drücke \n 1 um die Seriennummer und Anlagenummer erfassen \n 2 um Anlagenummer erfassen ")

    option = int(input(" dein Auswahl: "))

    def a():
        q = True
        li = []
        s_n_lange = int(input("Gib die Länge der Seriennummer an: "))
        a_n_lange = int(input("Gib die Länge der Anlagenummer an: "))
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
                a_nummer = input("Seriennummer: ")
            li.append([s_nummer, a_nummer])
            print(li)

    def b():
        q = True
        li = []
        s_n_lange = int(input("Gib die Länge der Anlagenummer an: "))
        while q is True:
            a_nummer = input("Anlagenummer: ")
            while len(a_nummer) < s_n_lange:
                if a_nummer[0] == "Ü":
                    with open('anlagenummer.csv', 'w') as f:
                        for i in range(len(li)):
                            text1 = li[i]
                            f.write(text1)
                            f.write("\n")
                    q = False
                    return q
                print("Seriennummer ist zu kurz. Bitte nochmal scannen.")
                a_nummer = input("Seriennummer: ")
            li.append(a_nummer)
            print(li)

    def default():
        print("Incorrect option")

    dictionary = {
        1: a,
        2: b,
    }
    dictionary.get(option, default)()


if __name__ == '__main__':
    print("Um das Programm zu beenden und die Liste zu speichern drücken Sie die Taste Ü!")
    seriennummer()
