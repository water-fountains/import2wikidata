1) Check osm fountains with wikidata entries (noCoordianteWikidata_fountainsRome.ipynb found 11)
2) check whether these wikidata entries have coordinates (OSM2Pandas-Fountains-withWikiDataRome.ipynb found 3)
3) set the coordinates from osm to 3 wikidata fontais (quickstatement_commands_locOrphan_fountainRome_191201_081205.txt)
4) Get all fountains out of OSM (OSM2Pandas-Fountains-Rome.ipynb ==> 1645 fountain)
5) import them as quickstatements into wikidata (itRome_fountains_preprocess.ipynb - 8191 lines)
6) make short URLs as per itRome_fountains_shortUrls.ipynb (first 181)


TODO:
=====
Re 5)
a) make all nasoni instanceof Q3336209
b) work on all the other interesting columns