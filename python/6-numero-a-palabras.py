class NumeroEnLetras:
    def __init__(self, numero):
        self.numero = numero
        self.palabras = self.convertir_a_palabras()

    def convertir_a_palabras(self):
        if self.numero < 10:
            return self.unidades(self.numero)
        elif self.numero < 100:
            return self.decenas(self.numero)
        elif self.numero < 1000:
            return self.centenas(self.numero)
        elif self.numero <= 1000:
            return self.miles(self.numero)
        else:
            return "Número fuera de rango"

    def unidades(self, num):
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        return unidades[num]

    def decenas(self, num):
        decenas = ["", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]

        if num < 10:
            return self.unidades(num)
        elif num >= 10 and num < 20:
            return especiales[num - 10]
        else:
            decena = num // 10
            unidad = num % 10
            if unidad == 0:
                return decenas[decena]
            else:
                return f"{decenas[decena]} y {self.unidades(unidad)}"

    def centenas(self, num):
        centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
        if num == 100:
            return "cien"
        else:
            centena = num // 100
            resto = num % 100
            if resto == 0:
                return centenas[centena]
            else:
                return f"{centenas[centena]} {self.decenas(resto)}"

    def miles(self, num):
        if num == 1000:
            return "mil"
        else:
            millar = num // 1000
            resto = num % 1000
            if millar == 1:
                return f"mil {self.centenas(resto)}"
            else:
                return f"{self.unidades(millar)} mil {self.centenas(resto)}"

# Solicitar al usuario que ingrese un número
numero = input("Ingrese un número (0-1000): ")

# Verificar si la entrada es un número válido
if numero.isdigit():
    numero = int(numero)
    # Crear una instancia de la clase y obtener la representación en palabras del número
    numero_en_letras = NumeroEnLetras(numero)
    print(f"{numero} -> {numero_en_letras.palabras}")
else:
    print("Fuera de rango. Ingrese un número entre 0 y 1000")
