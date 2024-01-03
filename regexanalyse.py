import re

zeilen = []


with open("dateiname.txt", "r") as file:
    for line in file:
        zeilen.append(line.strip())


#von a-Z
#.de .com .net .org .info
regex = (r"[a-zA-Z]+@\[a-zA-Z]+.([a-z]{2,4})")

#nach definition des Regex und der Liste sowie dem einlesen der zeilen aus der datei in die liste

for zeile in zeilen:
    if re.match(regex, zeile):
        print(zeile)
    else:
        print("Kein Match")

import requests
import re

# URL der Webseite
url = "https://bytes-coding.de"

# Anfrage an die Webseite senden und den HTML-Code erhalten
response = requests.get(url)

# Den HTML-Code als Text erhalten
html_code = response.text
# Regex-Muster erstellen
regex_pattern = r'elementor-button-text>(.+?)</span>'

# Alle Übereinstimmungen mit dem Muster im HTML-Code finden
matches = re.findall(regex_pattern, html_code, re.DOTALL)

# Die gefundenen Übereinstimmungen ausgeben
for match in matches:
    print(match)
