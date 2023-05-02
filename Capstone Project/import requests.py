import requests
import json
import re
import random


response = requests.get("https://api.weather.gov/stations/CWDZ/observations")

save_file = open("Data.txt","w")
json.dump(response.json(), save_file, sort_keys=True, indent=4)
save_file.close()


with open("Data.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'relativeHumidity' in line:
            lines = fp.readlines()
            numLine = str(lines[(l_no + 3):(l_no + 4)])

            text=""
            numbers=""
            res=[]
            for i in numLine:
                if(i.isdigit()):
                    numbers+=i
                else:
                    text+=i
            res.append(numbers)


            num = int(res[0])
            print(num)
            # don't look for next lines
            break

rand = float(random.randint(1,10000000))

# 999999999999999
# 100000000000000
# 10000000
num = num / rand
print(num)