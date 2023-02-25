class Phonebook:
    def __init__(self):
        self.entries = {'POLICIA': '190'}
        self.tamanho_minimo_numero = 3
        self.caracteres_invalidos = ['#', '@', '!', '$', '%']

    def verify_valid_name(self, name):  #Refatoração
        for item in self.caracteres_invalidos:
            if item in name or name == "":
                return False
        return True

    def verify_valid_number(self, number):  #Refatoração
        if len(number) >= self.tamanho_minimo_numero:
            return True
        else:
            return False

    def add(self, name, number): #Refatorado
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if self.verify_valid_name(name):
            pass
        else:
            return "Nome invalido"

        if self.verify_valid_number(number):
            pass
        else:
            return "Numero invalido"

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

    def lookup(self, name): #Refatorado
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if self.verify_valid_name(name):
            pass
        else:
            return "Nome invalido"

        return self.entries[name]

    #Change Number
    def change_number(self, name, new_number):#BDD
        if self.verify_valid_name(name) and self.verify_valid_number(new_number):
            if name in self.entries:
                self.entries[name] = new_number
                return "Numero atualizado"
            else:
                return "Nome invalido"
        else:
            return "Nome ou numero invalido"

    #Bugado
    def search(self, search_name):#corrigido
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def get_phonebook_sorted(self):#corrigido
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items(), key=lambda item:item[1])

    def get_phonebook_reverse(self):#corrigido
        """

        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(), key=lambda item:item[1], reverse=True)

    def get_name_by_number(self, number):#BDD
        for key, value in self.entries.items():
            if value == number:
                return key
        return "Nome não encontrado"

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def clear(self): #Refatorado
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries.clear()
        return 'phonebook limpado'
