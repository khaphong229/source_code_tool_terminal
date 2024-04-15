from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import os, re
import requests
import os.path
#print(check_file("data.json"))
chrome_options = Options() 
chrome_options.add_argument("--disable-notifications") 

#ck=input("Nhập Cookie Fb : ")
#token=input("Nhập Token TDS : ")
ck="datr=IRNZYvIiJX24hGOB_PRfg3mJ;sb=IRNZYiUa50MpCYnN1RPQd82V;m_pixel_ratio=3;usida=eyJ2ZXIiOjEsImlkIjoiQXJsd2liMHNpcTczYSIsInRpbWUiOjE2NjkzNzU0MDR9;x-referer=eyJyIjoiL25vdGlmaWNhdGlvbnMucGhwP2Vhdj1BZllLVVpwNVhSbHJ6NDNiQXpRQXgxRkZralFsb19yTUszd3lVZ1AzZUR1NWUtdW9lWTZzRGRMb0ZrWGp0QmRCZXZZJnBhaXB2PTAmcmVmPW1fbm90aWYmbm90aWZfdD1ncm91cHNfcHJldmlld19pbnZpdGUiLCJoIjoiL25vdGlmaWNhdGlvbnMucGhwP2Vhdj1BZllLVVpwNVhSbHJ6NDNiQXpRQXgxRkZralFsb19yTUszd3lVZ1AzZUR1NWUtdW9lWTZzRGRMb0ZrWGp0QmRCZXZZJnBhaXB2PTAmcmVmPW1fbm90aWYmbm90aWZfdD1ncm91cHNfcHJldmlld19pbnZpdGUiLCJzIjoibSJ9;vpd=v1%3B618x360x3;wd=360x618;fr=0IPjM1BpFrAmwIh5l.AWWFvF5L1ODaJODTDmqDhvHpRYY.Bi_3Qc._D.GOP.0.0.Bj1LX5.AWWaSMr_75A;c_user=100087595237147;xs=35%3AfpDdeRDIMzDeUQ%3A2%3A1674884601%3A-1%3A7623;locale=vi_VN;fbl_cs=AhCqN5PPbK37aPWdz9mWphtlGEJjZlpJd080YlJrdzhFckpyb1hrMWR3Tw;fbl_ci=1400472807424170;m_page_voice=100087595237147;fbl_st=100424068%3BT%3A27914826"

token="TDS0nI0IXZ2V2ciojIyVmdlNnIsICbv9GduB3aiojIyV2c1Jye"

h=0

driver=webdriver.Chrome(executable_path='chr.exe', chrome_options=chrome_options)
driver.set_window_size(680, 760)
driver.get("https://www.facebook.com/")
sleep(1)
for b in ck.split(";"):
    name=b.split("=")[0]
    print(b)
    value=b.split("=")[1]
    driver.add_cookie({"name": name, "value": value})
driver.get("https://www.facebook.com/")
sleep(5)
while True:

    driver.get("https://traodoisub.com/api/?fields=page&access_token=" + token)
    sleep(2)
    data=driver.page_source.split("</pre></body></html>")[0].split('pre-wrap;">')[1]
    sleep(2)
    for id in data.split(","):
    	h+=1
        id=id.split(': "')[1].split('"')[0]
        print(f"{h} | Job: {id}")
        driver.get("https://www.facebook.com/"+ id)
        sleep(3)
        driver.execute_script('window.scroll(0, 400)')
        sleep(1)
        try:
            a=driver.find_elements(By.XPATH, '//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft"]')
            for b in a:
                if b.text == "Thích" or b.text == "Theo dõi":
                    break
            b.click()
            sleep(2)
            driver.get("https://traodoisub.com/api/coin/?type=PAGE&id="+ id +"&access_token="+ token)
            sleep(6)
        except:
            print("Hết Job",end="    \r")
            break
            #driver.quit()
            #exit()
    sleep(11)

input()
driver.quit()  
 