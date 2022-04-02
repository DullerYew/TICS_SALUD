import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#### Credenciales de autentificacion para OpenEMR
admin = {'user':"admin",'password':"pass"}
physician = {'user':'physician','password':'physician'}
clinician = {'user':'clinician','password': 'clinician'}
receptionist = {'user':'receptionist','password':'receptionist'}


#Inicializacon del chromedriver
PATH_DRIVER= "./chromedriver"
URL = 'https://demo.openemr.io/openemr/interface/login/login.php?site=default'

driver = webdriver.Chrome(PATH_DRIVER)
driver.maximize_window()
driver.get(URL)

# Acceso al panel del login de la demo
username_text_field = driver.find_element_by_name("authUser")   #Text field para el nombre del usuario
password_text_field = driver.find_element_by_name("clearPass")  #Text field para el password
username_text_field.send_keys(physician['user'])    
password_text_field.send_keys(physician['password'])
username_text_field.send_keys(Keys.ENTER)



#Crear un nuevo paciente
patient_menu = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/div")   #Acceso al menu de "Patient"
patient_menu.click()

time.sleep(5) # Let the user actually see something!
patient_menu_new_search = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/ul/li[1]") #Acceso al sub menu New/search para registrar un nuevo paciente
patient_menu_new_search.click()








time.sleep(5)
#main_menu = driver.find_element_by_id("mainMenu")
#list_elements = main_menu.find_elements_by_tag_name("div")
#menu_patient = 
#login_form = driver.find_element_by_xpath("//*[@id='tabs_div']/div/div[4]").is_displayed()
#login_form.click()





#element = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/nav/div/div/div[6]/div/ul/li[1]")))
#element.click()

#print(list_elements)


#driver.close()   #Cierra la pestaña actual 

driver.quit()  #Cierra el navegador 