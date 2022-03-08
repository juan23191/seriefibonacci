from flask import Flask, jsonify
from datetime import datetime
import smtplib
from decouple import config

app = Flask(__name__)

def sendMail(remitente, destinatario, cuerpoCorreo, asunto):

    mensaje = 'Subject: {}\n\n{}'.format(asunto,cuerpoCorreo)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('juan_soto23191@elpoli.edu.co', config['PASS_EMAIL'])
    server.sendmail(remitente, destinatario, mensaje)
    server.quit()

@app.route('/', methods=['GET'])
def get_users():
    horaActual = datetime.now()
    minutos = horaActual.minute
    segundos = horaActual.second

    x = [int(a) for a in str(minutos)]
    valor1 = x[0]
    valor2 = x[1]
    serieFibonacci = [valor1, valor2]

    formatDate = horaActual.strftime(('%H:%M:%S'))

    for i in range(0,segundos):
        primerNumero = serieFibonacci[-2]
        segundoNumero = serieFibonacci[-1]
        serieFibonacci.append(primerNumero+segundoNumero)
    #print(serieFibonacci)
    response = {'message': 'success', 'minutos': minutos , 'segundos':segundos, 'SerieFibonacci':serieFibonacci}
    sendMail('juan_soto23191@elpoli.edu.co','juanpablos747@gmail.com',
             'Minutos  {}\nSegundos  {}\nSerie fibonacci\n{}'.format(minutos,segundos,serieFibonacci),
             'Prueba Tecnica Fibonacci Hora {}'.format(formatDate))
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
