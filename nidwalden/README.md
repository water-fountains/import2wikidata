## Daten:
Im Ordner "preparedData" können die aufbereiteten Daten gefunden werden, die aus der Maturaarbeit(siehe rawData) gewonnen wurden.

Im File "brunnen_daten_dicts" findet man 103 Brunnen.
Jede Zeile ist ein dict, welches die Daten zu diesem Brunnen enthält.
Jedes dict hat die Kategorien:
* Nr, Brunnen Nr im docx
* Name, Name vom Brunnen
* Ort, Ort + Strasse
* Baujahr, Baujahr
* Dimensionen, Dimensionen vom Brunnen (noch nicht vereinheitlicht)
* Fassungsvermoegen, Fassungsvermoegen in Liter (wenn 0 fliesst das Wasser sofort ab)
* Quelle, Von wo das Wasser kommt
* Trinkwasser, ist das Wasser trinkbar
* Kuenstler, wer steckt hinter dem Design
* Beschreibung, weiteres zu dem Brunnen
* Koordinaten, Koordinaten auf 5 stellen genau nach dem Punkt

## Scripts:
##### to_wikidata.py:
Dieses Script liest die Daten ein und gibt sie als wikidata-quickstatements aus. Diese kann man nun auf dieser [Seite](https://tools.wmflabs.org/wikidata-todo/quick_statements.php) ausführen lassen, um neue Wikidata Objekte zu erstellen.

##### to_xml.py:
Dieses Script liest die Daten ein und gibt sie als xml aus. Dieses XML kann mit JOSM geöffnet und dann nach OSM hochgeladen werden.

#### Wichtig:
* JOSM: um die OSM Daten hochzuladen muss man die version 15322 haben. Mit neueren Versionen ist dies eventuell nicht möglich.
* Vor dem ausführen der beiden Scripts wurde nach Duplikaten mit Hilfe von QGIS (mit dem QuickOSM Plugin) gesucht (hierbei kann man die Daten in QGIS laden und mit hilfe von dem Plugin eine Abfrage erstellen, die alle Momentan eingetragenen in ein neues Layer lädt. Danach reicht eine weitere Abfrage um die überlappenden Einträge zu finden) und die Scripts entsprechend angepasst. Diese Filter wurden wieder entfernt.


#### Sonstiges:
Die Daten: Dimensionen, Fassungsvermoegen, Quelle und Beschreibung wurden noch nicht benutzt.