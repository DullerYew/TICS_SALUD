"""
Universidad del Caribe
Ingenieria en Datos e Inteligencia Organizacional
TICS para la salud
Ivan Antonio Martinez Robledo

Programa: Clase para generar el calculo del RFC de una persona
"""

# ===================== IMPORTACIÖN DE LIBRERIAS ================
from base import BaseGenerator    #Clase de soporte para generar el RFC (Vease el archivo base.py para mas detalles)
import unicodedata


#Clase para calcular el RFC
class CalculeRFC(BaseGenerator):
	
	key_value = 'rfc'
	DATOS_REQUERIDOS = ( 'nombres','paterno', 'materno','fecha')
	_dato_parcial = None

	def __init__(self, **kargs):

		self.nombres = kargs['nombres']
		self.paterno = kargs['paterno']
		self.materno = kargs['materno']
		self.fecha = kargs['fecha']
		"""self.parse(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno
		)"""
		self._dato_parcial = self.baseDatoFiscal(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno,
			fecha=self.fecha
		)

	#Metodo para generar el nombre completo en caso de que se reciba en un formato diferente
	def genera(self):
		if self.materno is not None:
			nombrecompleto = u"%s %s %s" % (self.paterno, self.materno, self.nombres)
		else:
			nombrecompleto = u"%s %s" % (self.paterno, self.nombres)


		# Cálcula y agrega homoclave al RFC
		rfc = self._dato_parcial
		homoclave = self.generarClaveRFC(self._dato_parcial, nombrecompleto)
		rfc +=  homoclave
		# Cálcula y agrega digito verificador al RFC
		digito = self.generarNumeroVerificador(rfc)
		rfc += digito

		return rfc

	#Metodo para eliminar los acentos de las letras en los nombres
	def removerAccentos(self, s):
		if type(s) is str:
			s = u"%s" % s

		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


	#Metodo principal para generar generar la homoclave del RFC
	def generarClaveRFC(self, rfc, nombrecompleto):
		nombre_numero = "0"
		suma_valor = 0 
		div = 0 
		mod = 0

		rfc1 = {
			" ":00, "&":10, "Ñ":10, "A":11, "B":12, "C":13, "D":14, "E":15, "F":16,
			"G":17, "H":18, "I":19, "J":21, "K":22, "L":23, "M":24, "N":25, "O":26,
			"P":27, "Q":28, "R":29, "S":32, "T":33, "U":34, "V":35, "W":36, "X":37,
			"Y":38, "Z":39, "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
			"8":8,"9":9,"!":10,"¿":10,"Ð":10,"½":10,"¤":10,"¶":10,"?":10,"É":15,".":0,
			"n":25,"a":11,"b":12,"c":13,"d":14,"e":15,
		}
		rfc2 = {
			0:"1", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6", 6:"7", 7:"8", 8:"9", 9:"A", 10:"B",
			11:"C", 12:"D", 13:"E", 14:"F", 15:"G", 16:"H", 17:"I", 18:"J", 19:"K",
			20:"L", 21:"M", 22:"N", 23:"P", 24:"Q", 25:"R", 26:"S", 27:"T", 28:"U",
			29:"V", 30:"W", 31:"X", 32:"Y",
		}

		# Recorrer el nombre y convertir las letras en su valor numérico.
		for count in range(0, len(nombrecompleto)):
			letra = self.removerAccentos(nombrecompleto[count])

			nombre_numero += self.setRFC(str(rfc1[letra]),"00")
		# La formula es:
            # El caracter actual multiplicado por diez mas el valor del caracter
            # siguiente y lo anterior multiplicado por el valor del caracter siguiente.
		for count in range(0,len(nombre_numero)-1):
			count2 = count+1
			suma_valor += ((int(nombre_numero[count])*10) + int(nombre_numero[count2])) * int(nombre_numero[count2])
		
		div = suma_valor % 1000
		mod = div % 34
		div = (div-mod)/34
		if mod >32:
			mod -=1
		homoclave = ""
		homoclave += self.setRFC(rfc2[int(div)],"Z")
		homoclave += self.setRFC(rfc2[int(mod)],"Z")
		return homoclave

	def generarNumeroVerificador(self, rfc):
		suma_numero = 0 
		suma_parcial = 0
		digito = None 

		rfc3 = {
			"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18,
			"J":19, "K":20, "L":21, "M":22, "N":23, "O":25, "P":26, "Q":27, "R":28,
			"S":29, "T":30, "U":31, "V":32, "W":33, "X":34, "Y":35, "Z":36, "0":0,
			"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "":24,
			" ":37,"É":14,"Ó":25,"Á":10,"n":23
		}

		for count in range(0,len(rfc)):
			letra = rfc[count]
			if rfc3[letra]:
				suma_numero = rfc3[letra]
				suma_parcial += (suma_numero*(14-(count+1)))

		modulo = suma_parcial % 11
		digito_parcial = (11-modulo)
		
		if modulo == 0:
			digito = "0"
		if digito_parcial == 10:
			digito = "A"
		else:
			digito = str(digito_parcial)

		return  digito

	def setRFC(self, a, b):
		if a == b:
			return b
		else:
			return a


	@property
	def data(self):
		return self.genera()