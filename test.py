from bs4 import BeautifulSoup
import requests

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

print(headerlist)
print('--------------------------')

data = extracted [124:]

i = 0
while i < 5:
    data = data.replace('  ', ' ')
    i += 1

data = data.splitlines();
for row in data:
    print(row)
    
    








            

            
