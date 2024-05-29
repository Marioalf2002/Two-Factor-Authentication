<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/Marioalf2002)
![GitHub Followers](https://img.shields.io/github/followers/Marioalf2002?style=social)
![GitHub Followers](https://img.shields.io/github/stars/Marioalf2002?style=social)

<br>

[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=flat&logo=whatsapp)](https://wa.me/message/MC62R3PTOHVDN1)
[![Gmail](https://img.shields.io/badge/Gmail-Email-red?style=flat&logo=gmail)](https://mail.google.com/mail/?view=cm&fs=1&to=contacto@mariowebdesigns.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/mariowebdesign)
[![Discord](https://img.shields.io/badge/Discord-Chat-blue?style=flat&logo=discord)](https://discordapp.com/users/744348258893168680)

</div>

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
