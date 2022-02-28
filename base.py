"""
Universidad del Caribe
Ingenieria en Datos e Inteligencia Organizacional
TICS para la salud
Ivan Antonio Martinez Robledo

Programa: Clase de soporte para la generación del RFC
"""

#============== IMPORTACIÓN DE LIBRERIAS ====================
import datetime
from numpy import isin
from utils import Utils

class BaseGenerator(object):
    #Palabras prohibidas para el RFC
    palabras = [ 
			'BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO', 'COGE',
			'COGI', 'COJA', 'COJE', 'COJI', 'COJO', 'COLA', 'CULO', 'FALO', 'FETO',
			'GETA', 'GUEI', 'GUEY', 'JETA', 'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 
			'KAKA', 'KAKO', 'KOGE', 'KOGI', 'KOJA', 'KOJE', 'KOJI', 'KOJO', 'KOLA', 
			'KULO', 'LILO', 'LOCA', 'LOCO', 'LOKA', 'LOKO', 'MAME', 'MAMO', 'MEAR', 
			'MEAS', 'MEON', 'MIAR', 'MION', 'MOCO', 'MOKO', 'MULA', 'MULO', 'NACA', 
			'NACO', 'PEDA', 'PEDO', 'PENE', 'PIPI', 'PITO', 'POPO', 'PUTA', 'PUTO', 
			'QULO', 'RATA', 'ROBA', 'ROBE', 'ROBO', 'RUIN', 'SENO', 'TETA', 'VUEI', 
			'VUEY', 'WUEI', 'WUEY']
    #Abreviaturas de los estados en codigo de dos digitos
    estados = { 
			'':'', 'AGUASCALIENTES':'AS', 'BAJA CALIFORNIA':'BC',
			'BAJA CALIFORNIA SUR':'BS', 'CAMPECHE':'CC', 'CHIAPAS':'CS',
			'CHIHUAHUA':'CH', 'COAHUILA':'CL', 'COLIMA':'CM', 'DISTRITO FEDERAL':'DF',
			'DURANGO':'DG', 'GUANAJUATO':'GT', 'GUERRERO':'GR', 'HIDALGO':'HG',
			'JALISCO':'JC', 'MEXICO':'MC', 'MICHOACAN':'MN', 'MORELOS':'MS',
			'NAYARIT':'NT', 'NUEVO LEON':'NL', 'OAXACA':'OC', 'PUEBLA':'PL',
			'QUERETARO':'QT', 'QUINTANA ROO':'QR', 'SAN LUIS POTOSI':'SP',
			'SINALOA':'SL', 'SONORA':'SR', 'TABASCO':'TC', 'TAMAULIPAS':'TS',
			'TLAXCALA':'TL', 'VERACRUZ':'VZ', 'YUCATÁN':'YN', 'ZACATECAS':'ZS',
			'NACIDO EXTRANJERO':'NE'
		}
    
    
    
    def genera(self):
        raise NotImplementedError("No implementado")
    
    #Metodo para estandarizar los datos de la persona
    def parse(self, nombres, paterno, materno=None, estado=None):
        
        #Verifica que se le pase el estado, en caso de que no este vacio el campo lo convierte a mayusculas
        if estado != None:
            self.estado = Utils().upper(estado)
            
        if materno is not None:
            self.materno = Utils().upper(materno)
            self.materno = Utils().removerArticulo(self.materno)
            self.materno = Utils().removerCHLL(self.materno)
            
        self.nombres = Utils().upper(nombres)
        self.nombres = Utils().removerNombre(self.nombres)
        self.nombres = Utils().removerCHLL(self.nombres)
        
        self.paterno = Utils().upper(paterno)
        self.paterno = Utils().removerNombre(self.paterno)
        self.paterno = Utils().removerCHLL(self.paterno)
        
        
    #Metodo principal para generar el RFC base de la persona
    def baseDatoFiscal(self,nombres,paterno,materno,fecha):
        #Regresa las iniciales del nombre y verifica las palabras
        datoFiscal = self.iniciales(nombres,paterno,materno)
        
        datoFiscal = self.verificarPalabra(datoFiscal)
        
        #Se agrega la fecha de nacimiento
        fechaNacimiento = self.parseFecha(fecha)
        datoFiscal += fechaNacimiento
        return datoFiscal
    
    
    #Metodo para obtener el año de nacimiento en dos digitos de la persona
    def parseFecha(self,fecha):
        fechaNac = ""
        fecha = datetime.datetime.strptime(fecha,'%d-%m-%Y').date()
        anio = str(fecha.year)
        anio = anio[2:4]
        #Se rellena con ceros a la izquierda
        mes = str(fecha.month).zfill(2)
        dia = str(fecha.day).zfill(2)
        fechaNac += anio+mes+dia
        return fechaNac

    #Metodo para obtener las iniciales de la persona
    def iniciales(self,nombres,paterno,materno):
        if isinstance(paterno,float):
            paterno = "DELGADO"
            print(paterno)
            
            
        if isinstance(materno,float):
            materno = "DELGADO"
            print(materno)
        inicial = ''
        inicial = paterno[0:1]
        vocal = Utils().buscarVocal(paterno)
        inicial += vocal
        
        if materno is None:
            inicial +='X'
        else:
            inicial += materno[0:1]
        inicial += nombres[0:1]
        
        return inicial
    
    #Metodo para verificar si el RFC no genera una de las palabras prohibidas
    def verificarPalabra(self,rfc):
        newRFC = ''
        for palabra in self.palabras:
            if palabra == rfc:
                newRFC = Utils().cambiarVocales(rfc)
                break
            else:
                newRFC = rfc
        return newRFC

    #Metodo para cambiar el estado federativo a dos digitos (especifico para el curp)
    def cambiarEstadoFederativo(self,param):
        estado = None
        for key,value in self.estados.items():
            if key == param:
                estado = value
        return estado
    
    #Metodo para conseguir una consonante necesaria del cur (especifico para el curp) 
    def consonanteCURP(self,param):
        consonante = Utils().buscarConsonante(param)
        return consonante
    
    #Metodo para obtener el año de nacimiento
    def anioFecha(self, fecha):
        anio = Utils().getAnio(fecha)
        return anio
