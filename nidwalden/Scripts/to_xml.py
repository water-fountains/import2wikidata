import json

print("<?xml version='1.0' encoding='UTF-8'?>")
print('<osm version="0.6" generator="JOSM">')

with open("brunnen_daten_dicts", "r") as file:
    data = file.readlines()
    for nr, line in enumerate(data, 1):
        if line != '':
            fountain_dict = json.loads(line)
            lat = fountain_dict['Koordinaten'].split(",")[0]
            lon = fountain_dict['Koordinaten'].split(",")[1]
            # using negative id because node doesn't exist yet
            print('  <node id="' + str(-nr) + '" version="1" lat="{}" lon="{}">'.format(lat, lon))
            print('    <tag k="amenity" v="fountain"/>')
            print('    <tag k="description" v="' + fountain_dict['Name'] + '"/>')
            if fountain_dict['Baujahr'] != "-":
                print('    <tag k="year" v="' + fountain_dict['Baujahr'] + '"/>')
            if fountain_dict['Trinkwasser'] == 'True':
                print('    <tag k="drinking_water" v="yes"/>')
            if fountain_dict['Trinkwasser'] == 'False':
                print('    <tag k="drinking_water" v="no"/>')
            print('  </node>')
print('</osm>')
