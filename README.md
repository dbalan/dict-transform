# Dictionary transformation for numbers

This is a sample code to convert a long hex string to english words (or any words if you replace the ones in en.csv)

The db for wordlists is from https://pep.foundation/ codebase. (GPLv3/CC-BY-SA) https://pep.foundation/dev/repos/pEpEngine/file/86b78a45d1e9

## Running
```
# populate sqlite db
python todb.py

# run the map
python dictmap.py
HEXSTR: 7950f5369c531e869dfac8c9642eba945532715bb638936b8a80b605b2f1090e
WORDS:  MOISTURIZE CONVERT ROMONA CASBAH RUTLAND WOLFER JULIE TOYODA HAVE MAMBO TEQUILA PURIFY PERSUASIVE TENDS SWITCHBACK APIARIST 
```
