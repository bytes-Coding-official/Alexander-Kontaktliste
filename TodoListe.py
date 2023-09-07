from datetime import datetime

class TodoElement:
    def __init__(self, name, erstellt_datum=datetime.now(), fällig_datum = datetime.now(), priorität=1, erledigt=False):
        self.name = name
        self.erstellt_datum = erstellt_datum
        self.priorität = priorität
        self.erledigt = erledigt
        self.fällig_datum = fällig_datum
    
    
    def __str__(self):
        return f"Name: {self.name}, Erstellt: {self.erstellt_datum}, Fällig: {self.fällig_datum}, Priorität: {self.priorität}, Erledigt: {self.erledigt}"
    

    
class Todoliste:
    
    def __init__(self):
        self.__liste = []
    
    def add_element(self, element: TodoElement):
        self.__liste.append(element)
        
    def remove_element(self, element: TodoElement):
        self.__liste.remove(element)
        
    def get_element(self, index: int):
        return self.__liste[index]
    
    def __str__(self):
        return "\n".join([element.__str__() for element in self.__liste])
    
    def noch_zu_machen(self):
        return [element for element in self.__liste if not element.erledigt]
    
    def erledigt(self):
        return [element for element in self.__liste if element.erledigt]
    
    def suche(self, name):
        return [element for element in self.__liste if element.name == name]
    
    def sortiere(self):
        #sortiere erst alle elemente nach fälligkeitsdatum (welches am nächsten ist zuerst und dann nach priorität)
        self.__liste.sort(key=lambda element: (element.fällig_datum, element.priorität))

    def filter(self, datum):
        return [element for element in self.__liste if element.fällig_datum == datum or element.erstellt_datum == datum]

    def all(self):
        return self.__liste

Todoliste = Todoliste()
while (int(user_eingabe:=input("""Wähle eine Zahl:
1: Element hinzufügen
2: Element entfernen
3: Element bestanden oder nicht bestanden
4: Elemente sortieren
5: Elemente filtern
6: Elemente suchen
7: Elemente anzeigen

9: Beenden
""")) != 9):
    match user_eingabe:
        case 1:
            name = input("Name: ")
            erstellt_datum = datetime.strptime(input("Erstellt am (dd.mm.yyyy): "), "%d.%m.%Y")
            fällig_datum = datetime.strptime(input("Fällig am (dd.mm.yyyy): "), "%d.%m.%Y")
            priorität = int(input("Priorität: "))
            erledigt = bool(input("Erledigt (True/False): "))
            Todoliste.add_element(TodoElement(name, erstellt_datum, fällig_datum, priorität, erledigt))
        case 2:
            name = input("Name: ")
            erstellt_datum = datetime.strptime(input("Erstellt am (dd.mm.yyyy): "), "%d.%m.%Y")
            fällig_datum = datetime.strptime(input("Fällig am (dd.mm.yyyy): "), "%d.%m.%Y")
            priorität = int(input("Priorität: "))
            erledigt = bool(input("Erledigt (True/False): "))
            #get element with these values
            for element in Todoliste.all():
                if element.name == name and element.erstellt_datum == erstellt_datum and element.fällig_datum == fällig_datum and element.priorität == priorität and element.erledigt == erledigt:
                    Todoliste.remove_element(element)
        case 3:
            name = input("Name: ")
            erstellt_datum = datetime.strptime(input("Erstellt am (dd.mm.yyyy): "), "%d.%m.%Y")
            fällig_datum = datetime.strptime(input("Fällig am (dd.mm.yyyy): "), "%d.%m.%Y")
            priorität = int(input("Priorität: "))
            erledigt = bool(input("Erledigt (True/False): "))
            #get element with these values
            for element in Todoliste.all():
                if element.name == name and element.erstellt_datum == erstellt_datum and element.fällig_datum == fällig_datum and element.priorität == priorität :
                    element.erledigt = erledigt
        case 4:
            Todoliste.sortiere()
        case 5:
            datum = datetime.strptime(input("Datum (dd.mm.yyyy): "), "%d.%m.%Y")
            print("\n".join([element.__str__() for element in Todoliste.filter(datum)]))
        case 6:
            name = input("Name: ")
            print("\n".join([element.__str__() for element in Todoliste.suche(name)]))
        case 7:
            print(Todoliste.__str__())
        case _:
            print("Falsche Eingabe")
