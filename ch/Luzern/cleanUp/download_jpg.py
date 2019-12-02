all_lines = []
import urllib.request

with open("download.txt", "r",encoding='utf8') as file:
    daten = file.readlines()
    for line in daten:
        if "url" in line:
            line = line.replace('"url" : ', '')
            line = line.replace('"', '')
            line = line.replace('      ','')
            line = line.replace('\n','')
            all_lines.append(line)

print(all_lines)
for link in all_lines:
    urllib.request.urlretrieve(link, "bilder/"+link.split('/')[-1])
