from ics import Calendar, Event
import json

#Задание не завершено



#'C:/Users/samox/Downloads/А82-6711-2023.ics'
path = 'C:/Users/samox/Downloads/А82-6711-2023.ics'






def parseCrt(pth):
    with open(pth, 'r', encoding="utf8") as mf:
        fm = mf.read()

    c = Calendar(fm)

    json_string = {}
    dict(json_string)

    for e in c.events:
        json_string["case_number"] = e.name
        json_string["start"] = str(e.begin)
        json_string["end"] = str(e.end)
        json_string["location"] = e.location
        json_string["description"] = e.description

    print(type(json_string))

    for i in json_string:
        print(json_string)

    with open('json_data.json', 'w', encoding="utf8") as outfile:
        json.dump(json_string, outfile)


parseCrt(path)