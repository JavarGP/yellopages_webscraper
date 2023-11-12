from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()

test_list_names = ["https://www.detelefoongids.nl/result?who=john&where=Amsterdam", "https://www.detelefoongids.nl/result?who=james&where=Amsterdam", "https://www.detelefoongids.nl/result?who=sam&where=Amsterdam"]
test_list_names2 = ["https://www.detelefoongids.nl/result?who=sam&where=Amsterdam"]

new_list = []
i = 1
for sites in test_list_names:
    driver.get(sites)
    if i == 1 :
        driver.find_element(By.XPATH,'//*[@id="cookiescript_accept"]').click()

    people = driver.find_elements(By.CLASS_NAME,'card-body')
    person_num = driver.find_elements(By.CLASS_NAME,'button__yellow')
    driver.implicitly_wait(20)

    person_stat= []
    for get_num in person_num:
            get_num.click()

    for ppl in people:
        person_stat.append(ppl.text)
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
input = shadow_root.find_element(By.ID, "search_input")
action.click(input).send_keys(sheet[str_getVal].value).perform()
button = shadow_root.find_element(By.ID, "search_button")
action.move_to_element(button).click().perform()


# list1 = ["john\n123street, 1053DX Amsterdam\n2341575","sam\n43street, 1056GH Amsterdam\n2341525", "duncan\ntunastreet, 9956zz Amsterdam\n5551525"]
# new_list = []
# i = 0
# for v in list1:
#     list_logic = list1[q].split("\n")
#     i += 1
#     list_logic_convert = dict(enumerate(list_logic))
#     list_logic_convert["name"] = list_logic_convert[0]
#     list_logic_convert["address"] = list_logic_convert[1]
#     list_logic_convert["phone_number"] = list_logic_convert[2]
#     del list_logic_convert[0], list_logic_convert[1], list_logic_convert[2] 
#     new_list.append(list_logic_convert)
# print(new_list)


