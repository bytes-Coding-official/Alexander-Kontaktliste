import csv

def lade_datei(dateiname):
    strings = []
    with open(dateiname, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            strings.append(row)
    return strings

def speichere_datei(dateiname, kontakte):
    with open(dateiname+".csv", 'w', newline='') as csvfile:
        for kontakt in kontakte:
            csvfile.write(kontakt+"\n")
    return True
