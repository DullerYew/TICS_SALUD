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

time.sleep(1) # Let the user actually see something!
patient_menu_new_search = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/ul/li[1]/div") #Acceso al sub menu New/search para registrar un nuevo paciente
patient_menu_new_search.click()

#Cambia de frame a Nuevo Paciente
frame_0 = driver.find_element_by_xpath("//*[@id='framesDisplay']/div[3]/iframe")
driver.switch_to.frame(frame_0)

#INGRESAR VARIABLE NOMBRE
name = driver.find_element_by_name('form_fname')
name.send_keys('Alexis')
time.sleep(1) 

#INGRESAR VARIABLE APELLIDO
apellido = driver.find_element_by_name('form_lname')
apellido.send_keys('Ortega')
time.sleep(1) 

#INGRESAR VARIABLE RFC
rfc = driver.find_element_by_name('form_pubpid')
rfc.send_keys('323232')
time.sleep(1)

#INGRESAR VARIABLE SEXO, CAMBIAR POR MALE O FEMALE
sexo = driver.find_element_by_name('form_sex')
sexo.send_keys('Male')
time.sleep(1) 

#INGRESAR VARIABLE FECHA DE NACIMIENTO FORMATO DIA, MES AÑO
fecha = driver.find_element_by_name('form_DOB')
fecha.send_keys('1997-11-19')
time.sleep(1) 

#Crear nuevo paciente
boton = driver.find_element_by_name('create')
boton.click()
time.sleep(1)

#Vuelve al frame original e ingresa al popup
driver.switch_to.default_content()
frame_1 = driver.find_element_by_id('modalframe')
driver.switch_to.frame(frame_1)

#Confirma el nuevo paciente
boton1 = driver.find_element_by_xpath("//*[@id='searchResultsHeader']/center/input")
boton1.click()
time.sleep(1) 

#Espera a que aparezca la alerta y la acepta
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

#Regresa al frame principal y selecciona paciente de nuevo
driver.switch_to.default_content()
el = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/div")
el.click()
time.sleep(1) 

#Selecciona Visits
el = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/ul/li[3]/div/div")
el.click()
time.sleep(1) 

#Selecciona Create Visit
el = driver.find_element_by_xpath("//*[@id='mainMenu']/div/div[6]/div/ul/li[3]/div/ul/li[1]/div")
el.click()
time.sleep(1) 

#Ingresa al frame de Create Visit
frame = driver.find_element_by_xpath("//*[@id='framesDisplay']/div[4]/iframe")
driver.switch_to.frame(frame)

#Selecciona Categoria Nuevo paciente
new = driver.find_element_by_name('pc_catid')
new.send_keys('New Patient')
time.sleep(1) 

#Guarda la visita
el = driver.find_element_by_xpath("//*[@id='new-encounter-form']/div/div/div/button[1]")
el.click()
time.sleep(1)

#Cambia a el nuevo path
frame = driver.find_element_by_xpath("//*[@id='enctabs-1']/iframe")
driver.switch_to.frame(frame)

#Selecciona Categoria Clinical
el = driver.find_element_by_xpath("//*[@id='category_Clinical']")
el.click()
time.sleep(1) 

#Selecciona Vitals
el = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul[1]/li[2]/div/a[11]")
el.click()
time.sleep(1) 

#Se cambia al frame de vitals
driver.switch_to.default_content()
frame_1 = driver.find_element_by_xpath("//*[@id='framesDisplay']/div[4]/iframe")
driver.switch_to.frame(frame_1)
frame_1 = driver.find_element_by_xpath("//*[@id='enctabs-1001']/iframe")
driver.switch_to.frame(frame_1)

#Escribe el campo de peso INGRESAR LA VARIABLE PESO
peso = driver.find_element_by_xpath("//*[@id='weight_input_metric']")
peso.send_keys('80')
time.sleep(1)

#Escribir los demas vitales

driver.quit()

