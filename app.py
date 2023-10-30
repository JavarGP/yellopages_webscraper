import bs4
import requests
import urllib

url = "https://forebears.io/england/surnames"
headers = {
"User-Agent":
"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"}
response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.content, 'html.parser')
f = soup.find_all(class_="sur")

response2 = requests.get(url="https://forebears.io/netherlands/surnames", headers=headers)
soup2 = bs4.BeautifulSoup(response2.content, 'html.parser')
dutch_soup = soup2.find_all(class_="sur")

names_forebears = soup.select("tr:nth-of-type(2)")
tables = soup.find("table","table")
num_of_name = len(names_forebears)
q = bs4.BeautifulSoup.prettify(tables)

list_of_english_names_forbears =[]
list_of_dutch_names_forbears = []

# make and if statement to make th code D.R.Y
for x in range(len(f)):
    test_name_info = f[x].text
    list_of_english_names_forbears.append(test_name_info)

for x in range(len(dutch_soup)):
    test_name_info_dutch = dutch_soup[x].text
    list_of_dutch_names_forbears.append(test_name_info_dutch)

z1 = set(list_of_english_names_forbears)
z2 = set(list_of_dutch_names_forbears)
name_comparison = z1.difference(z2)
name_comparison_list = list(name_comparison)
z4 = sorted(name_comparison_list)
# print(len(name_comparison_list), len(list_of_english_names_forbears))
# print(sorted(list_of_english_names_forbears))

# https://www.detelefoongids.nl/api/search/index
# https://www.detelefoongids.nl/result?


telefoongids_input = "https://www.detelefoongids.nl"
session = requests.session()

myObj = {"who" : "z4", "where": "Amsterdam", "page": 0}
myObj2 = {"who": "John", "where": "Amsterdam", "page": 0}
res2 = session.post(url=telefoongids_input, data="myObj2", headers=headers, verify=False)

print(res2.text, res2)



