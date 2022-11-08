#Electronyi jurnal

thelist = []

info = input("Type info for journal: ")

def adding(answer):
    pass

def removing(answer):
    pass

def printing(answer):
    pass

def choise():
    ask =input("1.Add; 2.Remove; 3.Print")
    if ask == '1':
        return adding(ask)

    elif ask == '2':
        return removing(ask)

    elif ask == '3':
        return printing(ask)
    else:
        print("ERROR!")