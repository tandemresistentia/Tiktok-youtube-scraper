import Browser as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common
import time
from selenium.webdriver.common.keys import Keys
import sqlite3
import os 
class tiktokScraper:
    def __init__(self,url):
        self.url = url
        self.data = uc.Browser().getBot()

    def databot(self):
        self.data.get(self.url)
        time.sleep(1)
        i = 0
        n = 0
        '''TODO Abrir excels y guardar info en ellos para comprobar si existen los links alli 
        para no descargarlos y pasar al siguiente link y asi hasta que encuentre links no guardados'''
        groupLink = []
        groupCleaned = []
        while i < 8:
            try:
                group = self.data.find_elements(By.CLASS_NAME, "tiktok-x6y88p-DivItemContainerV2.e19c29qe7")[n]
                groupLink.append(group.find_elements(By.TAG_NAME, "a")[0].get_attribute('href'))
                
                #------------DATA HANDLING-----------------------
                        #create a data structure
                conn = sqlite3.connect('urlchecker.db')
                c = conn.cursor()

                #Create table
                c.execute('''Create TABLE if not exists server("urls")''')
                
                #Insert links into table
                for item in groupLink:
                    answer = c.execute("SELECT EXISTS(SELECT 1 AS bool FROM server WHERE urls='"+item+"')").fetchone()
                    if answer == (1,):
                        pass
                    else:
                        print("Download")
                        c.execute("INSERT INTO server(urls) VALUES(?)", (item,))
                        groupCleaned.append(item)
                        print(item)
                        os.system('python -m tiktok_downloader --url '+item+' --snaptik --save '+str(i)+'tiktok.mp4')
                        print(n)
                        i+=1
                        

                        
                conn.commit()
                n+=1
            except:
                self.data.maximize_window()
                time.sleep(5)
                from selenium.webdriver.common.keys import Keys
                self.data.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
                self.data.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
                self.data.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
                self.data.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
                self.data.find_element(By.TAG_NAME, "body").send_keys(Keys.DOWN)
                


        #query database
        c.execute("SELECT * FROM server")
        rows = c.fetchall() 
        print(groupCleaned)
        conn.close()
        #------------DATA HANDLING-----------------------
        print('Finished loading')




