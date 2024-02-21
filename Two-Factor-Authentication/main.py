# Importamos las bibliotecas necesarias:
# - time: para manejar operaciones relacionadas con el tiempo.
# - pyotp: para generar y verificar códigos TOTP.
# - qrcode: para generar códigos QR.
# - urlparse y parse_qs de urllib.parse: para analizar el URI de provisión.
import time
import pyotp
import qrcode
from urllib.parse import urlparse, parse_qs

# Generamos una clave base32 segura y única utilizando la función random_base32() de pyotp. 
# Esta clave se utilizará para generar y verificar los códigos TOTP.
key = pyotp.random_base32()

# Creamos un objeto TOTP con la clave generada. 
# Este objeto tiene métodos para generar y verificar códigos TOTP.
totp = pyotp.TOTP(key)

# Generamos un URI de provisión para la clave utilizando el método provisioning_uri() del objeto TOTP. 
# Este URI contiene la información necesaria para configurar una cuenta en una aplicación de autenticación.
# El nombre y el nombre del emisor se utilizan para identificar la cuenta en la aplicación de autenticación.
uri = totp.provisioning_uri(name="Prueba 2FA", issuer_name="Prueba 2FA")

# Analizamos el URI de provisión utilizando la función urlparse() de urllib.parse.
parsed_uri = urlparse(uri)

# Extraemos el secreto del URI de provisión utilizando la función parse_qs() de urllib.parse. 
# El secreto es la clave base32 que se utilizó para generar el URI de provisión.
secret = parse_qs(parsed_uri.query)['secret'][0]

# Imprimimos el secreto. Este es el secreto que el usuario puede ingresar manualmente en su aplicación de autenticación si no puede o no quiere escanear el código QR.
print("Clave de configuración: " + secret)

# Generamos un código QR a partir del URI de provisión utilizando la función make() de qrcode y lo guardamos como una imagen PNG.
qrcode.make(uri).save("2FA.png")

# Entramos en un bucle infinito. Donde estaremos solicitando al usuario que ingrese un código TOTP y verificando si es válido.
while True:
    # Solicitamos al usuario que ingrese un código TOTP.
    code = input("Ingresar Codigo: ")

    # Verificamos el código TOTP con una ventana de tiempo de 1 minuto utilizando el método verify() del objeto TOTP. 
    # Esto significa que aceptamos códigos que son válidos ahora o que eran válidos hace 1 minuto.
    # Esto puede ayudar a compensar pequeñas diferencias de tiempo entre el servidor y la aplicación de autenticación.
    is_valid = totp.verify(code, valid_window=1)

    # Imprimimos el resultado de la verificación. Si el código es válido, esto imprimirá True. De lo contrario, imprimirá False.
    print(is_valid)