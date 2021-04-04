import datetime


def seriennummer():
    date = str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"_"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    # This will guide the user to choose option
    print("Drücke \n 1 um die Seriennummer und Anlagenummer erfassen \n 2 um Anlagenummer erfassen ")

    option = int(input(" dein Auswahl: "))

    def a():

#      T = "####################################################################################\n# Alle Seriennummer
#      die mit Z anfangen sind eigentlich Y wegen ein Scanner Fehler. #\n############################################
#      ########################################\n\n"

        q = True
        li = []
        s_n_lange = int(input("Gib die Länge der Seriennummer an: "))
        a_n_lange = int(input("Gib die Länge der Anlagenummer an: "))
        projekt = str(input("Merkmale/Projekt: "))
        while q is True:
            s_nummer = input("Seriennummer: ")
            if s_nummer[0] == "Ü" or s_nummer[0] == "ü":
                with open(str(projekt)+'_serialnummer und anlagenummer_'+str(date)+'.csv', 'w') as f:
#                   f.write(T)
                    f.write(projekt)
                    f.write("\n")
                    for i in range(len(li)):
                        text1 = li[i][0]
                        text2 = li[i][1]
                        f.write(text1)
                        f.write(";")
                        f.write(text2)
                        f.write("\n")
                    f.close()
                q = False
                return q
            while len(s_nummer) < s_n_lange or len(s_nummer) > s_n_lange:
                print("Falsches Seriennumme. Bitte nochmal scannen.")
            s_nummer = input("Seriennummer: ")
            a_nummer = input("Anlagenummer: ")
            if len(a_nummer) < a_n_lange or len(a_nummer) > a_n_lange:
                print("Falsches Anlagenummer. Bitte nochmal scannen.")
                a_nummer = input("Anlagenummer: ")
            li.append([s_nummer, a_nummer])
            print("Letzer scan: ", li[len(li)-1][0], ",", li[len(li)-1][1])

    def b():
        q = True
        li = []
        a_n_lange = int(input("Gib die Länge der Anlagenummer an: "))
        projekt = str(input("Merkmale/Projekt: "))
        while q is True:
            a_nummer = input("Anlagenummer: ")
            while len(a_nummer) < a_n_lange or len(a_nummer) > a_n_lange:
                if a_nummer[0] == "Ü" or a_nummer[0] == "ü":
                    with open(str(projekt)+'_anlagenummer_'+str(date)+'.csv', 'w') as f:
                        f.write(projekt)
                        f.write("\n")
                        for i in range(len(li)):
                            text1 = li[i]
                            f.write(text1)
                            f.write("\n")
                        f.close()
                    q = False
                    return q
                print("Falsches Anlagenummer. Bitte nochmal scannen.")
                a_nummer = input("Anlagenummer: ")
            li.append(a_nummer)
            print(li[len(li)-1])

    def c():
        q = True
        li = []
        h_n_lange = int(input("Gib die Länge der Hostname an: "))
        projekt = str(input("Merkmale/Projekt: "))
        while q is True:
            hn_nummer = input("Hostname: ")
            while len(hn_nummer) < h_n_lange or len(hn_nummer) > h_n_lange:
                if hn_nummer[0] == "Ü" or hn_nummer[0] == "ü":
                    with open(str(projekt) + '_hostname_' + str(date) + '.csv', 'w') as f:
                        f.write(projekt)
                        f.write("\n")
                        for i in range(len(li)):
                            text1 = li[i]
                            f.write("d-"+text1)
                            f.write("\n")
                        f.close()
                    q = False
                    return q
                print("Falsches Hostname. Bitte nochmal scannen.")
                hn_nummer = input("Hostname: ")
            li.append(hn_nummer)
            print(li[len(li) - 1])

    def default():
        print("Incorrect option")

    dictionary = {
        1: a,
        2: b,
        3: c,
    }
    dictionary.get(option, default)()


if __name__ == '__main__':
    print("Um das Programm zu beenden und die Liste zu speichern drücken Sie die Taste Ü!")
    seriennummer()
