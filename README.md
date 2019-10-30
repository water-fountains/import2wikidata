# import2wikidata
Script to import Open Data Zurich fountains into wikidata without overwriting existing data. The script generates Quickstatement commands to be run in the online interface `https://tools.wmflabs.org/wikidata-todo/quick_statements.php`.

The project is open source under the GNU Affero General Public License, with a profit contribution agreement applying under restricted conditions. See [COPYING](/COPYING) for information.

## Process diagram
![import to wikidata flowchart](https://www.lucidchart.com/publicSegments/view/b253a72e-e909-4505-8d23-69841a54e358/image.png)

## Requirements
- Python 3.3 or higher (https://www.python.org/downloads/release/python-365/) make sure, it is added to your path
    - v3.65 works ; most other were very troublesome as per https://github.com/water-fountains/import2wikidata/wiki/Trouble-Shooting  (v3.53 on debian9 problematic with gastrodon; on win v3.8 with asyncio and win32api DLL, v3.7 with 'GenericMeta' from 'typing')
- Jupyter (http://jupyter.org/install)
- all packages mentioned in the import lines of the Jupyter notebook `zurich_fountains_preprocess.ipynb` (use `pip install [package name]` to install - in debian rather 'pip3')
    - gastrodon , pandas

## How to run
- Clone this repository to your local machine `git clone https://github.com/mmmatthew/import2wikidata.git`
- Start jupyter from a command window in the directory just created `jupyter notebook`
- In your browser, open `http://localhost:8888/notebooks/zurich_fountains_preprocess.ipynb` (the port may be different)
- Run the script. It should create a file `quickstatement_commands.txt`

## How to use the generated commands
- Go to `https://tools.wmflabs.org/wikidata-todo/quick_statements.php`.
- Authenticate yourself with your Wikidata account.
- Copy and paste the contents of `quickstatement_commands.txt` into the blank field, and run the commands

## Field mappings
Open Data Zurich fountain properties are mapped to the following wikidata properties
- bezeichnung -> Lde
- brunnenart_txt -> P31
- wasserart_txt -> P5623
- nummer -> P528
- historisches_baujahr -> P571

Type of water can take several values
- Verteilnetz -> Q53633635
- Quellwasser -> Q1881858
- Eigene Versorgung -> Q53634173
- Grundwasser -> Q161598

## Contributions welcome
Check the project issues to find out where the current dev focus is.

See also https://github.com/water-fountains/import2wikidata/wiki