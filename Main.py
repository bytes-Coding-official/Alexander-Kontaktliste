import Datenbank
from Adresse import Adresse
from Kontakt import Kontakt
import tkinter as tk
from tkinter import messagebox
# required modules
# import Datenbank
# from Adresse import Adresse
# from Kontakt import Kontakt

# Building the GUI 
class Application(tk.Frame):
    def __init__(self, adress_liste, master=None):
        super().__init__(master)
        self.master = master
        self.adress_liste = adress_liste
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_1 = tk.Label(self, text="Willkommen im Adressbuch")
        self.label_1.pack(side="top")

        self.zeigen = tk.Button(self)
        self.zeigen["text"] = "1. Zeigen"
        self.zeigen["command"] = self.show
        self.zeigen.pack(side="top")

        self.hinzufuegen = tk.Button(self)
        self.hinzufuegen["text"] = "2. Hinzufügen"
        self.hinzufuegen["command"] = self.add
        self.hinzufuegen.pack(side="top")

        self.loeschen = tk.Button(self)
        self.loeschen["text"] = "3. Löschen"
        self.loeschen["command"] = self.delete
        self.loeschen.pack(side="top")

        self.suchen = tk.Button(self)
        self.suchen["text"] = "4. Suchen"
        self.suchen["command"] = self.search
        self.suchen.pack(side="top")

        self.speichern = tk.Button(self)
        self.speichern["text"] = "5. Speichern"
        self.speichern["command"] = self.save
        self.speichern.pack(side="top")

        self.quit = tk.Button(self, text="9. Beenden", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # Implement the following methods based on your Adressbuch methods
    def show(self):
        # create toplevel window for showing
        self.showframe = tk.Toplevel(self)
        self.showframe.geometry("400x300")
        self.showframe.title("Show contacts")

        # Text box
        self.text_box = tk.Text(self.showframe, wrap="word", font=("Arial", 12))
        self.text_box.pack(fill="both", expand=True)

        for kontakt in self.adress_liste:
            self.text_box.insert("end", str(kontakt) + "\n")
            self.text_box.insert("end", "-----------------\n")

        # Close button 
        self.close_button = tk.Button(self.showframe, text="Close", command=self.showframe.destroy)
        self.close_button.pack(side="bottom")

    def add(self):
        # create toplevel window for adding
        self.addframe = tk.Toplevel(self)
        self.addframe.geometry("200x200")
        self.addframe.title("Add Kontakt")

        # Add Kontakt entries
        self.vorname_label = tk.Label(self.addframe, text="Vorname: ")
        self.vorname_label.pack(side="top")
        self.vorname_entry = tk.Entry(self.addframe)
        self.vorname_entry.pack(side="top")

        self.nachname_label = tk.Label(self.addframe, text="Nachname: ")
        self.nachname_label.pack(side="top")
        self.nachname_entry = tk.Entry(self.addframe)
        self.nachname_entry.pack(side="top")

        self.email_label = tk.Label(self.addframe, text="Email: ")
        self.email_label.pack(side="top")
        self.email_entry = tk.Entry(self.addframe)
        self.email_entry.pack(side="top")

        self.strasse_label = tk.Label(self.addframe, text="Strasse: ")
        self.strasse_label.pack(side="top")
        self.strasse_entry = tk.Entry(self.addframe)
        self.strasse_entry.pack(side="top")

        self.hausnummer_label = tk.Label(self.addframe, text="Hausnummer: ")
        self.hausnummer_label.pack(side="top")
        self.hausnummer_entry = tk.Entry(self.addframe)
        self.hausnummer_entry.pack(side="top")

        self.plz_label = tk.Label(self.addframe, text="PLZ: ")
        self.plz_label.pack(side="top")
        self.plz_entry = tk.Entry(self.addframe)
        self.plz_entry.pack(side="top")

        self.ort_label = tk.Label(self.addframe, text="Ort: ")
        self.ort_label.pack(side="top")
        self.ort_entry = tk.Entry(self.addframe)
        self.ort_entry.pack(side="top")

        # Add button
        self.add_kontakt_button = tk.Button(self.addframe, text="Add Kontakt", command=self.add_kontakt)
        self.add_kontakt_button.pack(side="top")

    def add_kontakt(self):
        vorname = self.vorname_entry.get()
        nachname = self.nachname_entry.get()
        email = self.email_entry.get()
        strasse = self.strasse_entry.get()
        hausnummer = self.hausnummer_entry.get()
        plz = self.plz_entry.get()
        ort = self.ort_entry.get()

        adresse = Adresse(strasse, hausnummer, plz, ort)
        kontakt = Kontakt(vorname, nachname, email, adresse)
        self.adress_liste.append(kontakt)
        print("Kontakt wurde hinzugefügt")  # substitute with some notification to user, or whatever you want to do

        # Clear the fields for next addition
        self.vorname_entry.delete(0, 'end')
        self.nachname_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.strasse_entry.delete(0, 'end')
        self.hausnummer_entry.delete(0, 'end')
        self.plz_entry.delete(0, 'end')
        self.ort_entry.delete(0, 'end')

    def delete(self):
        # create toplevel window for deletion
        self.deleteframe = tk.Toplevel(self)
        self.deleteframe.geometry("200x100")
        self.deleteframe.title("Delete Kontakt")

        # Delete entries
        self.vorname_label = tk.Label(self.deleteframe, text="Vorname: ")
        self.vorname_label.pack(side="top")
        self.vorname_delete = tk.Entry(self.deleteframe)
        self.vorname_delete.pack(side="top")

        self.nachname_label = tk.Label(self.deleteframe, text="Nachname: ")
        self.nachname_label.pack(side="top")
        self.nachname_delete = tk.Entry(self.deleteframe)
        self.nachname_delete.pack(side="top")

        # Delete button
        self.delete_button = tk.Button(self.deleteframe, text="Delete Kontakt", command=self.delete_kontakt)
        self.delete_button.pack(side="top")

    def delete_kontakt(self):
        vorname = self.vorname_delete.get()
        nachname = self.nachname_delete.get()

        for kontakt in self.adress_liste:
            if kontakt.vorname == vorname and kontakt.nachname == nachname:
                self.adress_liste.remove(kontakt)
                print("Kontakt wurde gelöscht")  # substitute with some notification to user, or whatever you want to do
                break

        # Clear the fields for next deletion
        self.vorname_delete.delete(0, 'end')
        self.nachname_delete.delete(0, 'end')

    def search(self):
        #create toplevel window for search
        self.searchframe = tk.Toplevel(self)
        self.searchframe.geometry("200x100")
        self.searchframe.title("Search Window")

        # Search entries
        self.vorname_label = tk.Label(self.searchframe, text="Vorname: ")
        self.vorname_label.pack(side="top")
        self.vorname_search = tk.Entry(self.searchframe)
        self.vorname_search.pack(side="top")

        self.nachname_label = tk.Label(self.searchframe, text="Nachname: ")
        self.nachname_label.pack(side="top")
        self.nachname_search = tk.Entry(self.searchframe)
        self.nachname_search.pack(side="top")

        # Add search button
        self.search_button = tk.Button(self.searchframe, text="Search", command=self.do_search)
        self.search_button.pack(side="top")

    def do_search(self):
        vorname = self.vorname_search.get()
        nachname = self.nachname_search.get()
        for kontakt in self.adress_liste:
            if kontakt.vorname == vorname and kontakt.nachname == nachname:
                print(kontakt)  # or whatever you want to do with the match
                break

        # clear the search fields for next search
        self.vorname_search.delete(0, 'end')
        self.nachname_search.delete(0, 'end')

    def save(self):
        kontakte = []
        for kontakt in self.adress_liste:
            kontakte.append(kontakt.csv_format())
        Datenbank.speichere_datei("adressbuch", kontakte)

        #erstelle grafiktext der der sagt das die kontakte gespeichert wurden
        self.saveframe = tk.Toplevel(self)
        self.saveframe.geometry("200x100")
        self.saveframe.title("Save Window")

        self.save_label = tk.Label(self.saveframe, text="Kontakte wurden gespeichert")
        self.save_label.pack(side="top")

        self.close_button = tk.Button(self.saveframe, text="Close", command=self.saveframe.destroy)
        self.close_button.pack(side="bottom")

        print("Kontakte wurden gespeichert")



def main():
    adress_liste = []
    datei_name = input("Bitte geben Sie den Dateinamen an: ")+".csv"
    try:
        daten = Datenbank.lade_datei(datei_name)
        for datensatz in daten:
            adresse = Adresse(datensatz[3], datensatz[4], datensatz[5], datensatz[6])
            kontakt = Kontakt(datensatz[0], datensatz[1], datensatz[2], adresse)
            adress_liste.append(kontakt)
    except Exception:
        print("Datei konnte nicht geladen werden")
    root = tk.Tk()
    app = Application(master=root, adress_liste=adress_liste)
    app.mainloop()

    def console():
        print("Willkommen im Adressbuch")
        print("""1. Anzeigen
        2. Hinzufügen
        3. Löschen
        4. Suchen
        5. Speichern
        9. Beenden
        """)
        while (nutzer_eingabe:= input("Deine Eingabe")) != "9":
            if nutzer_eingabe == "1":
                print("Anzeigen")
                for kontakt in adress_liste:
                    print(kontakt)
            elif nutzer_eingabe == "2":
                print("Hinzufügen")
                vorname = input("Vorname: ")
                nachname = input("Nachname: ")
                email = input("Email: ")
                strasse = input("Strasse: ")
                hausnummer = input("Hausnummer: ")
                plz = input("PLZ: ")
                ort = input("Ort: ")
                adresse = Adresse(strasse, hausnummer, plz, ort)
                kontakt = Kontakt(vorname, nachname, email, adresse)
                adress_liste.append(kontakt)
                print("Kontakt wurde hinzugefügt")
            elif nutzer_eingabe == "3":
                print("Löschen")
                vorname,nachname = input("Welchen Kontakt möchtest du löschen?").split(", ")
                for kontakt in adress_liste:
                    if kontakt.vorname == vorname and kontakt.nachname == nachname:
                        adress_liste.remove(kontakt)
                        print("Kontakt wurde gelöscht")
                        break

            elif nutzer_eingabe == "4":
                vorname,nachname = input("Welchen Kontakt möchtest du suchen?").split(", ")
                for kontakt in adress_liste:
                    if kontakt.vorname == vorname and kontakt.nachname == nachname:
                        print(kontakt)
                        break
            elif nutzer_eingabe == "5":
                print("Speichern")
                kontakte = []
                for kontakt in adress_liste:
                    kontakte.append(kontakt.csv_format())
                Datenbank.speichere_datei(datei_name, kontakte)
                print("Kontakte wurden gespeichert")

            else:
                print("Ungültige Eingabe")

if __name__ == "__main__":
    main()
