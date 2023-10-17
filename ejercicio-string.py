'''
Mostrar todos lo métodos disponibles para la clase string
'''

string = "Este es un string de prueba"

string_uppercase = string.upper()
string_lowercase = string.lower()
string_title = string.title()
string_replace = string.replace('string', 'cadena')
string_split = string.split()
string_strip = string.strip()
string_find = string.find('string')
string_count = string.count('e')
string_startswith = string.startswith('E')
string_endswith = string.endswith('a')
string_isalnum = string.isalnum()
string_isalpha = string.isalpha()
string_isdigit = string.isdigit()
string_islower = string.islower()
string_isupper = string.isupper()
string_isspace = string.isspace()
string_istitle = string.istitle()
string_isnumeric = string.isnumeric()
string_isprintable = string.isprintable()

print(".upper() -> convierte a mayúsculas")
print(string_uppercase) # ESTE ES UN STRING DE PRUEBA
print(".lower() -> convierte a minúsculas")
print(string_lowercase) # este es un string de prueba
print(".title() -> convierte a título, primera letra de cada palabra en mayúscula")
print(string_title) # Este Es Un String De Prueba
print(".replace() -> reemplaza una cadena por otra")
print(string_replace) # Este es un cadena de prueba
print(".split() -> separa una cadena en un array de cadenas")
print(string_split) # ['Este', 'es', 'un', 'string', 'de', 'prueba']
print(".strip() -> elimina espacios en blanco al inicio y al final de una cadena")
print(string_strip) # Este es un string de prueba
print(".find() -> busca una cadena dentro de otra y devuelve la posición de la primera aparición")
print(string_find) # 11
print(".count() -> cuenta la cantidad de veces que aparece una cadena dentro de otra")
print(string_count) # 4
print(".startswith() -> devuelve True si la cadena comienza con la cadena especificada")
print(string_startswith) # False
print(".endswith() -> devuelve True si la cadena termina con la cadena especificada")
print(string_endswith) # False
print(".isalnum() -> devuelve True si todos los caracteres de la cadena son alfanuméricos")
print(string_isalnum) # False
print(".isalpha() -> devuelve True si todos los caracteres de la cadena son alfabéticos")
print(string_isalpha) # False
print(".isdigit() -> devuelve True si todos los caracteres de la cadena son dígitos")
print(string_isdigit) # False
print(".islower() -> devuelve True si todos los caracteres de la cadena están en minúsculas")
print(string_islower) # False
print(".isupper() -> devuelve True si todos los caracteres de la cadena están en mayúsculas")
print(string_isupper)  # False
print(".isspace() -> devuelve True si todos los caracteres de la cadena son espacios en blanco")
print(string_isspace) # False
print(".istitle() -> devuelve True si la cadena sigue las reglas de un título")
print(string_istitle) # False
print(".isnumeric() -> devuelve True si todos los caracteres de la cadena son numéricos")
print(string_isnumeric) # False
print(".isprintable() -> devuelve True si todos los caracteres de la cadena son imprimibles")
print(string_isprintable)  # True