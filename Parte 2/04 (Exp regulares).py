import re

# Buscar expresiones regulares

# regex = r"[0-9]+"

# text = "Hoy es 3 de febrero del 2025"

# [0-9] o "\d" que es un carácter reservado para todos los número 


def encontrar(text: str)->list:
    return re.findall(r"[0-9]+", text)

print(encontrar("Hoy es 3 de febrero del 2025"))

# EXTRA 
# Es para a-z, A-Z y 0-9
# Regex.com ayuda para las expresiones regulares

def email(email: str) ->bool:
    return bool (re.match (r"[\w\.+-]+@[\w]+\.[a-zA-Z]+", email))

print(email("andresfelipefrancomesa@gmail.com"))

def phone (phone: str) ->bool:
    return bool (re.match(r"^\+?[\d\s]{3,}$", phone))

print(phone("+57 312880000567"))

def url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(url("http://www.moure.dev"))
