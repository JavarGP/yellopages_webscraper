import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests
import urllib
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas

driver = webdriver.Chrome()
url = "https://forebears.io/england/surnames"
headers = {
"User-Agent":
"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
find_surnames1 = soup.find_all(class_="sur")

response2 = requests.get(url="https://forebears.io/netherlands/surnames", headers=headers)
soup2 = BeautifulSoup(response2.content, 'html.parser')
mode_spoken_language_soup = soup2.find_all(class_="sur")

async def parse_html(html_content):
    # url = "https://forebears.io/england/surnames"
    soup = BeautifulSoup(url, 'html.parser')
    find_surnames1 = soup.find_all(class_="sur")

# response2 = requests.get(url="https://forebears.io/netherlands/surnames", headers=headers)
# soup2 = BeautifulSoup(response2.content, 'html.parser')
# mode_spoken_language_soup = soup2.find_all(class_="sur")

list_of_english_names_forbears =[]
list_of_dutch_names_forbears = []
names_forebears = soup.select("tr:nth-of-type(2)")
tables = soup.find("table", "table")
num_of_name = len(names_forebears)
q = BeautifulSoup.prettify(tables)

# make and if statement to make th code D.R.Y
for x in range(len(find_surnames1)):
    test_name_info = find_surnames1[x].text
    list_of_english_names_forbears.append(test_name_info)
for x in range(len(mode_spoken_language_soup)):
    test_name_info_dutch = mode_spoken_language_soup[x].text
    list_of_dutch_names_forbears.append(test_name_info_dutch)

z1 = set(list_of_english_names_forbears)
z2 = set(list_of_dutch_names_forbears)
name_comparison = z1.difference(z2)
name_comparison_list = list(name_comparison)
z4 = sorted(name_comparison_list)


url_list = []
for url_names in z4:
    fstring_url = (f"https://www.detelefoongids.nl/result?who={url_names}&where=Amsterdam")
    url_list.append(fstring_url)
# print(url_list)

new_list = []
i = 1
for sites in url_list:
    driver.get(sites)
    if i == 1 :
        driver.find_element(By.XPATH,'//*[@id="cookiescript_accept"]').click()

    people = driver.find_elements(By.CLASS_NAME,'card-body')
    person_num = driver.find_elements(By.CLASS_NAME,'button__yellow')
    driver.implicitly_wait(5)
    
    person_stat= []
    if person_num == True:
        for get_num in person_num: 
            get_num.click()

        for ppl in people:
            person_stat.append(ppl.text)
    else:
        pass
    # print(person_stat)
    i += 1

   
    q = 0
    for v in person_stat:
        list_logic = person_stat[q].split("\n")
        q += 1

      
        list_logic_convert = dict(enumerate(list_logic))
        list_logic_convert["name"] = list_logic_convert[0]
        list_logic_convert["address"] = list_logic_convert[1]
        list_logic_convert["phone_number"] = list_logic_convert[2]
        del list_logic_convert[0], list_logic_convert[1], list_logic_convert[2] 
        stats = {
            "names":list_logic_convert["name"],
            "place":list_logic_convert["address"],
            "tele_num":list_logic_convert["phone_number"]
        }
        new_list.append(stats)
        print(new_list)
driver.close()
      
action = ActionChains(driver)

closed_shadow_host = driver.find_element(By.CSS_SELECTOR, "aa-dxt-qr-content")
shadow_root = driver.execute_script('return arguments[0].root.querySelector(".container-fluid")', closed_shadow_host)
# input = shadow_root.find_element(By.ID, "search_input")
# action.click(input).send_keys(sheet[str_getVal].value).perform()
button = shadow_root.find_element(By.ID, "search_button")
action.move_to_element(button).click().perform()


# driver.quit()

# for x in range(len(mode_spoken_language_soup)):
#     test_name_info_dutch = mode_spoken_language_soup[x].text
#     list_of_dutch_names_forbears.append(test_name_info_dutch)

#     z1 = set(list_of_english_names_forbears)
#     z2 = set(list_of_dutch_names_forbears)
#     name_comparison = z1.difference(z2)
#     name_comparison_list = list(name_comparison)
#     z4 = sorted(name_comparison_list)
  
# test_url = (f"{telefoongids_input}/result?{next(iter(myObj2))}={myObj2['who']}&{next(iter(myObj2))}={myObj2['where']}")
# requests.get()
# async def get_html_content(url, headers):
#     connector = aiohttp.TCPConnector(limit=1, limit_per_host=1, ssl=False)
#     async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     telefoongids_url = "https://www.detelefoongids.nl"
#     headers = {
#         "User-Agent":
#             "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"}
#     html_content = await get_html_content(telefoongids_url, headers)
#     print("html_content", html_content)

# if __name__ == '__main__':
#     asyncio.run(main())





