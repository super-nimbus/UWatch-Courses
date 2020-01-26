from bs4 import BeautifulSoup
import requests
import json
import re

term = '1201'
subject = 'CS'
course_num = '136'

url = f'http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess={term}&subject={subject}&cournum={course_num}'

content = requests.get(url)


soup = BeautifulSoup(content.text, 'html.parser')

table = soup.select('tr table')

extracted = "".join([td.text for td in table])


headers = extracted[0:122]
headers = headers.replace('\n', ' ')
headers = headers.strip()
headerlist = headers.split(' ')
temp = headerlist.pop(0)

si = iter(headerlist)
headerlist = [c+next(si, '') for c in si]

headerlist.insert(0, temp)
headerlist.pop(3)

print(headerlist)
print(len(headerlist))
print('--------------------------')

data = extracted [124:]

i = 0

data = data.strip()
while i < 5:
    data = data.replace('  ', ' ')
    i += 1

data = data.splitlines()


#for row in data:
#    print(row)

datalist = []
for rows in data:
    innerlist = []
    for cols in rows.split(' '):
        innerlist.append(cols)
    datalist.append(innerlist)

#print(datalist)

for rows in datalist: #fixing formating

    
    if rows[1] == 'LEC':
        rows.pop(-1)
        rows.pop(5)
        temp = rows.pop(2)
        rows[1] = rows[1] + temp
        rows[2] = rows[2] + ' ' + rows[3]

        count = 0
        index = count - 1
        
        for char in rows[10]:
            if rows[10][count].isalpha():
                rows[10] = rows[10][:count] + ' ' + rows[10][count:]
                temp = rows.pop(-1)
                temp = temp.split(' ')
               # print(temp)
                if len(temp) > 1:
                    temp1 = temp[0]
                    temp2 = temp[1]
                    rows.append(temp1)
                    rows.append(temp2)
                break
            count += 1
            index += 1
                
    else:
        rows[1] = rows[1] + rows[2]
        rows [3] = rows[3] + ' ' + rows [4]
        rows.pop(2)

    count = 0

   # for char in rows[-1]:
        

    
    rows[5] = rows[5].replace(u'\xa0', u' ')
    #rows[5] = rows[5].replace('b', '')

    



#print(datalist[1])
#print(datalist[10])
#print(len(datalist[0]))

master = {}

for rows in datalist:
    dictionary = dict(zip(headerlist, rows))
    master[rows[0]] = dictionary

print(master)
    








            

            
