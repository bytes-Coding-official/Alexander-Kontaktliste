from Adresse import Adresse
class Kontakt:
    def __init__(self, vorname: str, nachname: str, email: str, adresse: Adresse) -> None:
        self.vorname: str = vorname
        self.nachname: str = nachname
        self.email: str = email
        self.adresse: Adresse = adresse


    def __str__(self) -> str:
        return f"{self.vorname} {self.nachname}, {self.email}, {self.adresse.__str__()}"

    def csv_format(self) -> str:
        return f"{self.vorname},{self.nachname},{self.email},{self.adresse.csv_format()}"
