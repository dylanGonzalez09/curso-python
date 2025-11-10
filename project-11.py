import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar mic y devolver audio como texto
def transformar_audio_a_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()
    # config microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes habalar")

        # guardar lo que se escucha como audio
        audio = r.listen(origen)

        try:
            # buscar en google lo que escucho
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que se pudo ingresar
            print("dijiste: " + pedido)

            return pedido
        
        except sr.UnknownValueError:
            print("Upss no entendi")

            return "Sigo esperando"
        
        except sr.RequestError:
            print("Upss no hay servicio")

            return "Sigo esperando"
        
        except Exception as e:
            print("Upss algo ha salido mal: ", e)

            return "Sigo esperando" 
        
# asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar dia de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()
    dia_semana = dia.weekday()

    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miercoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sabado', 6: 'Domingo'}
    hablar(f"Hoy es {calendario[dia_semana]}")


def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)

def saludo_inicial():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'


    hablar(f"Hola {momento} soy Helena, tu asistente. Por favor, dime en que te puedo ayudar")

def pedir_cosas():
    saludo_inicial()

    comenzar = True

    while comenzar:
        pedido = transformar_audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es hoy' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ' + resultado)
            continue
        elif 'busca en internet' in pedido:
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar("Voy a eso master")
            pywhatkit.playonyt(pedido)
            
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': "APPL", 'amazon': 'AMZN', 'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("No la he encontrado, triste")
                continue
        elif 'cerrar' in pedido:
            hablar('Hasta la proxima')
            break

pedir_cosas()


