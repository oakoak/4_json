# Prettify JSON

---
The script reads the json file and prints in a pretty form
---

### Description 
+ Script takes the path to the files as a parameters
+ Script checks the path, if there is no file - prints an error
+ Script prints an error if the file is not json
+ If you add second parameter, the script will output the data to a file with this path

Example of script launch on Linux, Python 3.5:

### Example using
```#!bash
$ python pprint_json.py <path to input file> <path to output file> 
```

### Example output information from a file
```bash
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "улица Академика Павлова, дом 10",
                    "AdmArea": "Западный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Кунцево",
                    "IsNetObject": "да",
                    "Name": "Ароматный Мир",
                    "OperatingCompany": "Ароматный Мир",
                    "PublicPhone": [
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
