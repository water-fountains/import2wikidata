import json

with open("brunnen_daten_dicts", "r") as file:
    data = file.readlines()
    for line in data:
        if line != '':
            fountain_dict = json.loads(line)
            if fountain_dict['Nr'] != 69:
                name = "Brunnen_" + fountain_dict['Ort'].split(",")[0].replace(" ", "") + "_" + fountain_dict['Name'].replace("Brunnen ", "") + "(Nidwalden)"
                name = name.replace(" ", "_")
                print('CREATE')
                print('LAST\tP31\tQ483453\tS248\tQ76808959')
                print('LAST\tLde\t'+fountain_dict['Name'])
                if fountain_dict['Baujahr'] != "-":
                    print('LAST\tP571\t+'+fountain_dict['Baujahr']+'-01-01T00:00:00Z'+'\tS248\tQ76808959')
                print('LAST\tP18\t'+name+'.jpg\tS248\tQ76808959')
                print('LAST\tP625\t@'+fountain_dict['Koordinaten'].split(",")[0]+"/"+fountain_dict['Koordinaten'].split(",")[1]+'\tS248\tQ76808959')
