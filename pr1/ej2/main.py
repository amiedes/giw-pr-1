# -*- coding: utf-8 -*-

'''
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
'''

'''
Considerar la función SMTP del módulo smtplib que permite la conexión con un
servidor. Se pide implementar una aplicación que simule un correo electrónico
básico. El programa solicitará por pantalla los siguientes datos:
    * Servidor de correo electrónico.
    * Correo electrónico del remitente.
    * Correo electrónico del destinatario.
    * Mensaje que desea enviar.
A continuación, le preguntará si envía el mensaje. Si responde “Sí”, se enviará
y como resultado el programa mostrará por pantalla el mensaje “Mensaje enviado
correctamente” o bien mostrará un mensaje de error. Si responde “No”, le
preguntará si quiere intentar enviar otro mensaje o salir.

La estructura del programa debe ser:

    from smtpib import SMTP

    # Capturar servidor y puerto de entrada. Por ejemplo en Gmail es: # smtp.gmail.com y puerto 587
    servidor = SMTP(servidor smtp, puerto)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Solicitar cuenta de correo remitente y password para autenticarse ante el #servidor
    server.login(cuenta de correo, password)

    # Capturar destinatario
    # Capturar mensaje
    servidor.sendmail(remitente, destinatario, mensaje)
    server.quit()
'''

from smtplib import SMTP

#Capturar servidor
def leer_mensaje():
    msg = dict()
    # leer y crear el servidor de correo electrónico
    server_url = 'smtp.gmail.com:587'   # server_url = raw_input("URL del servidor: ")
    msg['servidor'] = SMTP(server_url)
    # ask for user and password
    usr = 'grupo1giw@gmail.com'         # usr = raw_input("User: ")
    pwd = '123-abc-cba-321'             # pwd = raw_input("Password: ")
    # start tls and login
    msg['servidor'].ehlo()
    msg['servidor'].starttls()
    msg['servidor'].ehlo()
    msg['servidor'].login(usr, pwd)
    # leer remitente, destinatario y mensaje
    msg['remitente']    = raw_input("From: ")
    msg['destinatario'] = raw_input("To: ")
    msg['content']      = raw_input("Message (end with ^D): ")
    # devolver un objeto con toda la información necearia para enviar el mensaje
    return msg

def pedir_mensaje():
    message_ok = False
    while (not message_ok):
        try:
            msg = leer_mensaje()
            message_ok = True
        except:
            print "ERROR: Ha ocurrido un problema leyendo el mensaje"
    return msg

def enviar_mensaje(msg):
    msg['servidor'].sendmail(msg['remitente'], msg['destinatario'], msg['content'])
    msg['servidor'].close()

def main():
    exit = False
    while (not exit):
        msg = pedir_mensaje()
        opcion = raw_input("Quieres enviar el mensaje? (Si/No): ")
        if (opcion == "Si"):
            try:
                enviar_mensaje(msg)
                print "SUCCESS: Mensaje enviado correctamente"
            except:
                print "ERROR: No se ha podido enviar el mensaje"
        elif (opcion == "No"):
            opcion = raw_input("Quieres enviar otro mensaje o salir? (Enviar/Salir): ")
            exit = (opcion == "Salir")
        else:
            print "ERROR: Opción no reconocida"

main()
