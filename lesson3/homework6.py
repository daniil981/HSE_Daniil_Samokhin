from ics import Calendar, Event
import json
import re



#'C:/Users/samox/Downloads/А82-6711-2023.ics'
path = 'C:/Users/samox/Downloads/А56-32581-2023.ics'






def parseCrt(pth):
    with open(pth, 'r', encoding="utf8") as mf:
        fm = mf.read()
        c = Calendar(fm)

    json_string = {}
    dict(json_string)

    for e in c.events:
        pat = r'(А\d+.*\d)'
        cnm = re.findall(pat,  e.name)
        if str(e.begin) != '0001-01-01T00:00:00+00:00' and str(e.end) != '0001-01-01T00:00:00+00:00' and e.location != 'None':
            json_string["case_number"] = cnm[0]
            json_string["start"] = str(e.begin)
            json_string["end"] = str(e.end)
            json_string["location"] = e.location
            json_string["description"] = e.description

            with open('json_data.json', 'w', encoding="utf8") as outfile:
                json.dump(json_string, outfile)

        else:
            print("Дело не существует, пожалуйста, загрузите другой файл")






parseCrt(path)

