import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    if int(txtIn) > 4:
        print("Errore: non esiste questa opzione!")
        break
    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        txtIn.lower()
        t.handleAdd(txtIn)
        continue
    if int(txtIn) == 2:
        print("Ok, quale parola vuoi tradurre?")
        txtIn = input()
        txtIn.lower()
        t.handleTranslate(txtIn)
        continue
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        t.handleWildCard(txtIn)
        continue
    if int(txtIn) == 4:
        break

