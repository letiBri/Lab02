import dictionary as diz

class Translator:

    def __init__(self):
        dizFinale = None

    def printMenu(self):
        print("------------------------------")
        print("   Translator Alien-Italian   ")
        print("------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as file:
            y = file.read()
            listaRighe = y.split("\n")
            dizTraduzioni = {}
            for i in listaRighe:
                campi = i.split(" ")
                dizTraduzioni[campi[0]] = campi[1]
        self.dizFinale = diz.Dictionary(dizTraduzioni)
        return self.dizFinale

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parolaAliena = entry.split(" ")[0]
        parolaItaliane = entry.split(" ")[1::]
        self.dizFinale.addWord(parolaAliena, parolaItaliane)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query.lower()
        self.dizFinale.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        indice = query.index("?")
        parte1 = query.split("?")[0]
        parte2 = query.split("?")[1]
        self.dizFinale.translateWordWildCard(parte1, parte2, indice)

