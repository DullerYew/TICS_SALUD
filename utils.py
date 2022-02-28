"""
Universidad del caribe
Ingenieria en datos e Inteligencia Organizacional
TICS para la salud
Ivan Antonio Martinez Robledo
Programa: Clase de utilidades generales
"""

#Clase de soporte que brinda funciones de utilidad para la generacion del RFC
import datetime
    
class Utils(object):
    
    #Función para remover los articulos de los nombres y/oapellidos generados
    def removerArticulo(self,articulo):
        articulos = (
            'DE ',
            'DEL ',
            'LA ',
            'LOS ',
            'LAS ',
            'Y ',
            'MC ',
            'MAC ',
            'VON ',
            'VAN '   
        )
        
        for art in articulos:
            data = articulo.replace(art,'')
        return data;
    
    #Función para remover algunas abreviaciones de los nombres 
    def removerNombre(self,nombre):
        nombres = (
            'JOSE ',
            'J ',
            'MARIA ',
            'MA. ',
            'DE ',
            ' DE ',
            'DEL ',
            'LA ',
            ' LA ',
            'LAS ',
            ' LAS ',
            'LOS ',
            ' LOS ',
            'MC ',
            'MC ',
            'MAC ',
            'VON ',
            'VAN ',
            ' Y '
        )
        
        for nombre in nombres:
            data = nombre.replace(nombre,'')
        return data
    
    #Función para remover y remplazar las letras CH y LL de los nombres y apellidos 
    def removerCHLL(self,texto):
        letras = texto[0:2]
        concatenarLetras = texto[2:len(texto)]
        
        if letras == 'CH':
            texto = 'C%s' % concatenarLetras
        elif letras == 'LL':
            texto = 'L%s' % concatenarLetras
        return texto
    
    #Función para buscar una consonante en una palabra
    def buscarConsonante(self,palabra):
        valor = ''
        consonante = ''
        longitud = 0
        
        #Se valida si la palabra no esta vacia o no se le esta pasando nada
        if palabra is not None:
            longitud = len(palabra)
            longitud = longitud-1
            valor = palabra[1:longitud]
        else:
            valor = 'X'
            
        for letra in valor:
            if letra == 'Ñ':
                consonante = "X"
                break
            elif self.consonante(letra):
                consonante = letra
                break
        return consonante
    
    #Funcion para evaluar si una letra es consonante
    def consonante(self,consonante):
        consonantes = (
            'B',
            'C',
            'D',
            'F',
            'G',
            'H',
            'J',
            'K',
            'L',
            'M',
            'N',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'V',
            'W',
            'X',
            'Y',
            'Z'
        )
        
        for cons in consonantes:
            if cons == consonante:
                return True
                break
        return False
    
    #Función para buscar y devolver la primera vocal del apellido paterno
    def buscarVocal(self,paterno):
        size = len(paterno) - 1
        data = ''
        paterno = paterno[1:size]
        
        for letra in paterno:
            if self.vocal(vocal=letra):
                data = letra
                break
        return data 
    
    #Función para evaluar si la letra es una vocal
    def vocal(self,vocal):
        vocales = (
            'A',
            'E',
            'I',
            'O',
            'U',
            'Á',
            'É',
            'Í',
            'Ó',
            'Ú'
        )
        
        for voc in vocales:
            if voc == vocal:
                return True
                break
        return False
        
    #Función para convertir una palabra en mayusculas
    def upper(self,texto):
        palabra = texto.upper()
        return palabra.strip()
    
    #Función para obtener el año de la fecha de nacimiento del 
    def getAnio(self,fechaNac):
        try:
            fecha = datetime.datetime.strptime(fechaNac,'%d-%m-%Y').date()
            return fecha.year
        except Exception as e:
            raise str(e)
    
    #Función para cambiar las vocales de las palabras prohibidas del dato fiscal
    def cambiarVocales(self,palabra):
        tmp = ''
        for letra in palabra:
            if self.vocal(vocal=letra):
                tmp += 'X'
            else:
                tmp += letra
        return tmp
        
    
        