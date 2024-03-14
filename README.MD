# Generador de Código 2FA

Este código genera y verifica códigos TOTP (Time-Based One-Time Password) para autenticación de dos factores.

## Bibliotecas Utilizadas

- `time`: Utilizada para operaciones relacionadas con el tiempo.
- `pyotp`: Utilizada para generar y verificar códigos TOTP.
- `qrcode`: Utilizada para generar códigos QR.
- `urllib.parse`: Utilizada para analizar la URI de aprovisionamiento.

## Explicación del Código

1. Generar una clave base32 segura y única utilizando la función `random_base32()` de `pyotp`.
2. Crear un objeto TOTP con la clave generada.
3. Generar una URI de aprovisionamiento para la clave utilizando el método `provisioning_uri()` del objeto TOTP.
4. Analizar la URI de aprovisionamiento utilizando la función `urlparse()` de `urllib.parse`.
5. Extraer la clave secreta de la URI de aprovisionamiento utilizando la función `parse_qs()` de `urllib.parse`.
6. Imprimir la clave secreta, que se puede ingresar manualmente en una aplicación de autenticación si no es posible escanear el código QR.
7. Generar un código QR a partir de la URI de aprovisionamiento utilizando la función `make()` de `qrcode` y guardarlo como una imagen PNG.
8. Entrar en un bucle infinito donde se solicita al usuario que ingrese un código TOTP y se verifica su validez.
9. Verificar el código TOTP con una ventana de tiempo de 1 minuto utilizando el método `verify()` del objeto TOTP.
10. Imprimir el resultado de la verificación.

## Uso

1. Instalar las bibliotecas requeridas: `pip install pyotp qrcode`.
2. Ejecutar el código.
3. Escanear el código QR generado con una aplicación de autenticación o ingresar manualmente la clave secreta.
4. Ingresar el código TOTP cuando se solicite.
5. El código verificará el código ingresado e imprimirá el resultado.
