class Adresse:
    def __init__(self, strasse, hausnummer, plz, ort):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort

    def __str__(self):
        return self.strasse + ", " + self.hausnummer + ", " + self.plz + " " + self.ort

    def csv_format(self):
        return f"{self.strasse},{self.hausnummer},{self.plz},{self.ort}"
