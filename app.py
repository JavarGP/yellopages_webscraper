import asyncio
import aiohttp
import bs4
import requests


async def parse_html(html_content):
    # url = "https://forebears.io/england/surnames"
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    f = soup.find_all(class_="sur")

    #response2 = requests.get(url="https://forebears.io/netherlands/surnames", headers=headers)
    soup2 = bs4.BeautifulSoup(html_content, 'html.parser')
    dutch_soup = soup2.find_all(class_="sur")

    names_forebears = soup.select("tr:nth-of-type(2)")
    tables = soup.find("table", "table")
    num_of_name = len(names_forebears)
    q = bs4.BeautifulSoup.prettify(tables)

    list_of_english_names_forbears = []
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

    myObj = {"who": "z4", "where": "Amsterdam", "page": 0}
    myObj2 = {"who": "John", "where": "Amsterdam", "page": 0}


async def get_html_content(url, headers):
    connector = aiohttp.TCPConnector(limit=1, limit_per_host=1, ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    telefoongids_url = "https://www.detelefoongids.nl"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"}
    html_content = await get_html_content(telefoongids_url, headers)
    print("html_content", html_content)


if __name__ == '__main__':
    asyncio.run(main())
