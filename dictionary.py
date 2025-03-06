class Dictionary:
    def __init__(self, dizionario={}):
        self.dizionario = dizionario

    def addWord(self, parolaAliena, parolaItaliana, dict):
        existing = False
        for key in self.dizionario:
            if key == parolaAliena:
                existing = True
                print("Parola già inserita")
        if not existing:
            self.dizionario[parolaAliena] = parolaItaliana
            with open(dict, "a+") as file:
                file.write(f"{parolaAliena} {parolaItaliana}\n")
            print(f"['{parolaAliena}', '{parolaItaliana}']")
            print("Aggiunta!")
    def translate(self, parolaAliena):
        for key in self.dizionario:
            if key == parolaAliena:
                print(f"{self.dizionario[parolaAliena]}")
                break

    def translateWordWildCard(self, parte1, parte2, indice):
        lista = []
        for key in self.dizionario:
            str1 = key[0:indice]
            str2 = key[indice + 1::]
            if str1 == parte1 and str2 == parte2:
                lista.append(self.dizionario[key])
        print(lista)
