
"""
Universidad del Caribe
Ingenieria en Dagtos e Inteligencia Organizacional
TICS para la salud
Ivan Antonio Martinez Robledo
Programa: Simulador de datos medicos v1
"""


#=========== IMPORTACIÓN DE LAS LIBRERIAS NECESARIAS =======================00
import random
import argparse
from numpy import diag, floor
import numpy as np
import pandas as pd
from calculerfc import CalculeRFC  #Aqui se extra la clase para generar el rfc (Vease el archivo calcuerfc.py para mas detalles)
import datetime

#================ CONSTANTE ===============================0
currentDateTime = datetime.datetime.now()
dateNow = currentDateTime.date()
global year 
year = dateNow.strftime("%Y")

#============== FUNCIÓN PARA GENERAR PESO Y ALTURA ==============
"""
Descripción: Esta función sirve para generar, de manera aleatoria y 
             considerando los valores de referencia incluidos en la cartilla de salud, los pesos y alturas

Parametros de entrada:
    -> Sexo (String)
    -> Edad (Integer)
Salida:
    -> [Altura,Peso] (Array)
"""
def generarPesoAltura(sex,edad):
    if sex == 'H':
        if edad >= 18 and edad <= 25:
            altura = random.randint(168,184)
            peso = random.uniform(52.2,101.2)
        elif edad >= 26:
            altura = random.randint(164,170)
            peso = random.uniform(49.8,72.0)
        elif edad < 18 and edad >= 10:
            altura = random.randint(135,168)
            peso = random.uniform(30.0,56.7)
        else:
            altura = random.randint(80,120)
            peso = random.uniform(18.0,30.0)
    else:
        if edad >= 18 and edad <= 25:
            altura = random.randint(140,158)
            peso = random.uniform(38.4,62.9)
        elif edad >= 26:
            altura = random.randint(138,155)
            peso = random.uniform(40.4,64.9)
        elif edad < 18 and edad >= 10:
            altura = random.randint(120,145)
            peso = random.uniform(25.0,58.0)
        else:
            altura = random.randint(80,110)
            peso = random.uniform(18.0,30.0)
        
    return [round(altura,2),round(peso,2)]


#============== FUNCIÓN PARA GENERAR UNA FECHA ==============
"""
Descripción: Esta función sirve para generar una fecha tomando en cuenta la
             distribución de la piramide poblacional del INEGI

Parametros de entrada:
    -> Sexo (String)
Salida:
    -> Fecha (Array)
"""
def generarFecha(sex):
    fechaGen = ''
    if sex == 'H':
        probEdad = random.uniform(9,0)
        if probEdad >= 2.67 and probEdad <= 9:
            anioSelect = random.randint(1976,2008)
        else:
            anioSelect = random.randint(1980,1990)
    else:
        probEdad = random.uniform(9,0)
        if probEdad >= 3.7 and probEdad <= 9:
            anioSelect = random.randint(1973,2003)
        else:
            anioSelect = random.randint(1983,1990)
      
    mesSelect = random.randint(1,12)
    if mesSelect == 2:
        diaSelect = random.randint(1,28);
        if diaSelect < 10:
            fechaGen = '0' + str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
            #return fechaGen
        else:
            fechaGen = str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
            #return fechaGen
    elif mesSelect != 2 and mesSelect < 10:
        mod = mesSelect % 2
        if mod == 1:
            diaSelect = random.randint(1,30)
            if diaSelect < 10:
                fechaGen = '0' + str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen 
            else:
                fechaGen = str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
        else:
            diaSelect = random.randint(1,30)
            if diaSelect < 10:
                fechaGen = '0' + str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
            else:
                fechaGen = str(diaSelect) + '-' + '0' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
    else:
        mod = mesSelect % 2
        if mod == 1:
            diaSelect = random.randint(1,30)
            if diaSelect < 10:
                fechaGen = fechaGen = '0' + str(diaSelect) + '-' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
            else:
                fechaGen = str(diaSelect) + '-' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
                
        else: 
            diaSelect = random.randint(1,30)
            if diaSelect < 10:
                fechaGen ='0' + str(diaSelect) + '-' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
            else:
                fechaGen = str(diaSelect) + '-' + str(mesSelect) + '-' + str(anioSelect)
                #return fechaGen
            
    tmp = datetime.datetime.strptime(fechaGen,'%d-%m-%Y').date()
    anio = int(tmp.year)
    edad = int(year) - anio
    return [fechaGen,edad]
   
 #============== FUNCIÓN PARA GENERAR LA PRESION ARTERIAL ==============
"""
Descripción: Esta función sirve para generar la presione PAS y PAD de acuerdo a la edad

Parametros de entrada:
    -> Edad (Integer)
Salida:
    -> [PAS,PAD] (Array)
"""               
def generarPresion(edad):
    PAS = 0
    PAD = 0
    if edad >= 18:
        PAS = random.randrange(110,140,10)
        PAD = random.randrange(60,90,10)
    else:
        PAS = random.randrange(80,100,10)
        PAD = random.randrange(60,90,10)  
    return[PAS,PAD]
     
  #============== FUNCIÓN PARA GENERAR EL PULSO CARDIACO ==============
"""
Descripción: Esta función sirve para generar las pulsaciones de la persona respecto a su edad

Parametros de entrada:
    -> Edad (Integer)
Salida:
    -> Latidos (Integer)
"""            
def generarPulso(edad):
    latidos = 0
    if edad >= 18:
        latidos = random.randint(60,100)
    else:
         latidos = random.randint(60,90)
    return latidos   

  #============== FUNCIÓN PARA GENERAR LA TEMPERATURA CORPORAL ==============
"""
Descripción: Esta función sirve para generar las pulsaciones de la persona respecto a su edad

Parametros de entrada:
    -> Edad (Integer)
Salida:
    -> Temperatura (Float)
""" 
def generarTemperatura(edad):
    temp = 0.0
    if edad >= 18:
        temp = random.uniform(36.2,37.2)
    else:
        temp = random.uniform(36.8,37.5)
    return round(temp,1)

  #============== FUNCIÓN PARA GENERAR LOS DATOS DE LABORATORIO ==============
"""
Descripción: Esta función sirve para generar los datos de laboratorio de la persona de acuerdo a su edad y sexo

Parametros de entrada:
    -> Sexo (String)
    -> Edad (Integer)
Salida:
    -> [
        leucocitos,
        eritrocitos,
        plaquetas,
        glucosa,
        urea,
        creatinina,
        acidoUrico,
        colesterol_total
        ] (Array)
""" 
def generarLabQuimica(sex,edad):
    leucocitos = 0.0
    eritrocitos = 0.0
    plaquetas = 0
    glucosa = 0
    
    if edad >= 10 and edad <=50:
        leucocitos = random.uniform(5.30,9.70)
    elif edad > 50:
        leucocitos =random.uniform(4.65,5.20)
        
    if edad >= 15 and sex == 'H':
        eritrocitos = random.uniform(4.35,5.65)
    elif edad >= 15 and sex == 'M':
        eritrocitos = random.uniform(3.92,5.13)
        
    if sex == 'H':
        plaquetas = random.randint(135,317)
    else:
        plaquetas = random.randint(157,371)
        
    glucosa = random.randint(60,160)
    urea = random.uniform(14.60,52.50)
    creatinina =random.uniform(0.20,1.90)
    acidoU = random.uniform(2.0,9.20)
    col = random.uniform(0,210)
    
    return [round(leucocitos,2),round(eritrocitos,2),plaquetas,glucosa,round(urea,2),round(creatinina,2),round(acidoU,2),round(col,1)]



#============= ESPECIFICACIONES DE PARAMETROS EN TERMINAL

parser = argparse.ArgumentParser('Manual del Simulador de Datos Medicos v1')
parser.add_argument("-n", "--numero", help="Numero de datos a generar")
parser.add_argument("-c", "--csv", help="Nombre del archivo de salida en formato .csv")
args = parser.parse_args()
   
#=================== PROGRAMA PRINCIPAL =====================   
        
#Inicialización del dataFrame
df = pd.DataFrame()

#Columnas de datos personales
df['RFC'] = None
df['SEXO'] = None
df['EDAD'] = None
df['PESO'] = None
df['ALTURA'] = None

#Columnas de signos vitales
df['PULSO'] = None
df['PRESION_ART_PAS'] = None
df['PRESION_ART_PAD'] = None
df['TEMP_CORPORAL'] = None

#Columnas con datos de laboratorio (Quimica sanguinia, Hematologia)
df['ERITROCITOS'] = None
df['LEUCOCITOS'] = None
df['PLAQUETAS'] = None
df['GLUCOSA'] = None
df['UREA'] = None
df['CREATININA'] = None
df['ACIDO_URICO'] = None
df['COLESTEROL_TOT'] = None


# ============== LECTURA DE DATASETS DE APOYO ==================
apellidosFrec_data = pd.read_excel('./datasets/apellidos.xlsx') #Dataset que contiene los apellidos más comunes en México
nombresHombreFrec_data = pd.read_csv('./datasets/nombreshombre3.csv', encoding='latin1')   #Dataset que contiene los nombres para hombre mas frecuentes en México
nombresMujerFrec_data = pd.read_csv('./datasets/nombresmujer3.csv', encoding='latin1')     #Dataset que contiene los nombres para mujer mas freceuntes en México

cantNombresHombres = len(nombresHombreFrec_data)
cantNombresMujeres = len(nombresMujerFrec_data)
cantApellidos = len(apellidosFrec_data)

num = int(args.numero)
nH = int(round(49*num/100,0))
nM = int(num - nH)

rfcs = []
sexos = []
edades = []
alturas = []
pesos = []

presiones_PAS = []
presiones_PAD = []
pulsaciones = []
temperaturas = []

leucos = []
eris = []
plaquets = []
glucos = []
ureas = []
creatis = []
acids = []
colest = []

for h in range(0,nH):
    ran_nombreH_1 = random.randint(0,cantNombresHombres-1)
    ran_nombreH_2 = random.randint(0,cantNombresHombres-1)
    ran_apellidoH_pat = random.randint(0,cantApellidos-1)
    ran_apellidoH_mat = random.randint(0,cantApellidos-1)
    
    date = generarFecha('H')
    varPA = generarPesoAltura('H',date[1])
    rfc = CalculeRFC(nombres=nombresHombreFrec_data['NOMBRE'][ran_nombreH_1] + ' ' + nombresHombreFrec_data['NOMBRE'][ran_nombreH_2],paterno=apellidosFrec_data['apellido'][ran_apellidoH_pat],materno=apellidosFrec_data['apellido'][ran_apellidoH_mat],fecha=date[0]).data
    
    rfcs.append(rfc)
    alturas.append(varPA[0])
    pesos.append(varPA[1])
    sexos.append('Masculino')
    edades.append(date[1])
    
    presion = generarPresion(date[1])
    presiones_PAS.append(presion[0])
    presiones_PAD.append(presion[1])
    pulsaciones.append(generarPulso(date[1]))
    temperaturas.append(generarTemperatura(date[1]))
    
    labData = generarLabQuimica('H',date[1])
    leucos.append(labData[0])
    eris.append(labData[1])
    plaquets.append(labData[2])
    glucos.append(labData[3])
    ureas.append(labData[4])
    creatis.append(labData[5])
    acids.append(labData[6])
    colest.append(labData[7])
    
    
    
    

for m in range(0,nM):
    ran_nombreM_1 = random.randint(0,cantNombresMujeres-1)
    ran_nombreM_2 = random.randint(0,cantNombresMujeres-1)
    ran_apellidoM_pat = random.randint(0,cantApellidos-1)
    ran_apellidoM_mat = random.randint(0,cantApellidos-1)
    date = generarFecha('M')
    varPA = generarPesoAltura('M',date[1])
    
    rfc = CalculeRFC(nombres=nombresMujerFrec_data['NOMBRE'][ran_nombreM_1] + ' ' + nombresMujerFrec_data['NOMBRE'][ran_nombreM_2],paterno=apellidosFrec_data['apellido'][ran_apellidoM_pat],materno=apellidosFrec_data['apellido'][ran_apellidoM_mat],fecha=date[0]).data
    rfcs.append(rfc)
    alturas.append(varPA[0])
    pesos.append(varPA[1])
    sexos.append('Femenino')
    edades.append(date[1])
    
    presion = generarPresion(date[1])
    presiones_PAS.append(presion[0])
    presiones_PAD.append(presion[1])
    pulsaciones.append(generarPulso(date[1]))
    temperaturas.append(generarTemperatura(date[1]))
    
    labData = generarLabQuimica('M',date[1])
    leucos.append(labData[0])
    eris.append(labData[1])
    plaquets.append(labData[2])
    glucos.append(labData[3])
    ureas.append(labData[4])
    creatis.append(labData[5])
    acids.append(labData[6])
    colest.append(labData[7])
    
    
# ================= ASIGNACIÓN DE LOS VALRES GENERADOS AL DATAFRAME
df['RFC'] = rfcs
df['SEXO'] = sexos
df['EDAD'] = edades
df['ALTURA'] = alturas
df['PESO'] =pesos

df['PRESION_ART_PAS'] = presiones_PAS
df['PRESION_ART_PAD'] = presiones_PAD
df['PULSO'] = pulsaciones
df['TEMP_CORPORAL'] = temperaturas

df['LEUCOCITOS'] = leucos
df['ERITROCITOS'] = eris
df['PLAQUETAS'] = plaquets
df['GLUCOSA'] = glucos
df['UREA'] = ureas
df['CREATININA'] = creatis
df['ACIDO_URICO'] = acids
df['COLESTEROL_TOT'] = colest


#pd.set_option('display.max_columns', None) 
#print(df)
df = df.sample(frac=1).reset_index(drop=True)
#print(df)

print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format("RFC","SEXO","EDAD","ALTURA","PESO","PRESION_ART_PAS","PRESION_ART_PAD","PULSO","TEMP_CORPORAL","LEUCOCITOS","ERITROCITOS","PLAQUETAS","GLUCOSA","UREA","CREATININA","ACIDO_URICO","COLESTEROL_TOT"))

for i in range(0,num):
    print("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(df['RFC'][i],df['SEXO'][i],df['EDAD'][i],df['ALTURA'][i],df['PESO'][i],df['PRESION_ART_PAS'][i],df['PRESION_ART_PAD'][i],df['PULSO'][i],df['TEMP_CORPORAL'][i],df['LEUCOCITOS'][i],df['ERITROCITOS'][i],df['PLAQUETAS'][i],df['GLUCOSA'][i],df['UREA'][i],df['CREATININA'][i],df['ACIDO_URICO'][i],df['COLESTEROL_TOT'][i]))


if args.csv != None:
    filename = str(args.csv)
    df.to_csv(filename)





            
        

