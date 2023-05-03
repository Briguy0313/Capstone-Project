# import module
import requests
import json
import re
import random
import webbrowser
import codecs

response = requests.get("https://api.weather.gov/stations/CWDZ/observations")

save_file = open("Data.txt","w")
json.dump(response.json(), save_file, sort_keys=True, indent=4)
save_file.close()


with open("G:\Weather API\Data.txt", 'r') as fp:
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

            num = res

            print(num)




            class Main:
                first_header = num

            # Read the HTML file
            HTML_File=open('index.html','r')
            CiteCode = HTML_File.read().format(p=Main())
            

            
            # to open/create a new html file in the write mode
            f = open('Webpage.html', 'w')
            
            # the html code which is read from the index.html file
            html_template = CiteCode
            
            # writing the code into the file
            f.write(html_template)
            
            # close the file
            f.close()
            
            # viewing html files
            # below code creates a 
            # codecs.StreamReaderWriter object
            file = codecs.open("Webpage.html", 'r')


            webbrowser.open('Webpage.html')





            # don't look for next lines
            break

            


# print(random.randint(0,9))
#num = num / random 1-999999999999999