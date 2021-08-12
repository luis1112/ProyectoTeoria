# importamos el paquete y le ponemos un nombre mas corto
import speech_recognition as sr
import pyttsx3
import pywhatkit


name = 'barto'
#  creamos una variable, esto nos permitira reconocer la voz
listener = sr.Recognizer()


#inicializamos
engine= pyttsx3.init()

#obtenemso los tipo de voces que hay
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#presentar todo los tipos de voces
#for voice in voices
#print(voice)

#creamos las funcionalidades
def talk(text):

#se envia el texto que se desea que diga 
    engine.say(text)
    engine.runAndWait()

def listen():
    try:  
        # llamamos el metodo microphone y le ponemos  con el nombre de source
        # lo ponemos dentro del try por que pueda que haya un error con el microfono 
        with sr.Microphone() as source:
            print("Escuchando..")
            #creamos una variable y del listener  vamos a obtener el metodo listen y le damos que cree el source
            voice = listener.listen(source)
            #de listener vamos a obtener el api de google y le enviamos voice
            rec = listener.recognize_google(voice, language='es-ES')
            # validamos
            # en la variable rec se va a guardar toda la informacion que se le dice pero la va a entender todo como minuscula
            rec = rec.lower()
            # para que barto nos conteste tenemos que decir su nombre primero
            if  name in rec:
                # remplamos el nombre de barto al momento que nos contesta
                rec = rec.replace(name,'')
                print('Usted dijo: '+ rec)
        
    except: 
        pass
    return rec

def run(): 
    #Asignamos a la variable rec lo que salga de listen
    rec = listen()
    #Comprobamos si se encuentra la palabra reproduce
    if 'reproduce' in rec:
        # Lequitamos la palabra reproduce 
        music = rec.replace('reproduce', '')
        talk('Reproduciendo: '+ music)
        #llamamos al metodo playonyt, este metodo bucara automaticamente en youtube y presentara
        pywhatkit.playonyt(music)

run()