# importamos las librerias Natural Language Toolkit, chat para el chatbot y reflections para pronombres 
import nltk 
from nltk.chat.util import Chat, reflections 
from colorama import Fore, Style  # Importa los estilos de color de colorama

# Agregamos las preguntas o palabras claves y sus respuestas como pares en una lista [r"",[]],
pairs = [
    [
        r"(Hola|hola|optica)",
        ["Hola, esta es la optica Flores, tienen dudas con el horario semanal, ubicacion, numero, precio de los lentes o tipos de lentes?",]
    ],
    [
        r"(.*)(horario|semana|semanal|atienden|atender|cierran|Cierran|Hora|hora|Abren|abren)",
        ["Nuestro horario de atención es de lunes a domingo de 10:30 am a 6:30 pm",]
    ],
    [
        r"(.*)(cuestan|Cuestan|Costo|costo|precio|Precio|Precios|precios)",
        ["El costo de los lentes en Mica Blanca:$1200, Mica Antirreflejante:$1700, Mica Fotocromatica:$2200, Mica Blue Ray:$2500 y se hace descuento de $500 si trare un armazón",]
    ],[
        r"(.*)(Tipo|tipo|Tipos|tipos)",
        ["Los tipos de lentes son de Mica Blanca, Mica Antirreflejante (evita reflejos de luz artificial), Mica Fotocromatica (luz solar), Mica Blue Ray (evita luz azul) y pupilentes",]
    ],
    [
        r"(.*)(tiempo|Tiempo|tardan|Tardan|Tardarían|tardarían|tarda|Tarda)",
        ["Por lo general, lo tenemos entre 3 y 7 días hábiles en fabricar los lentes una vez que se haya realizado la orden y se envía mensaje por Whatsapp.",]
    ],
    [
        r"(.*)(Contacto|contacto|pupilentes|Pupilentes)",
        ["Ofrecemos una variedad de lentes de contacto. Te invitamos a visitar nuestra tienda para conocer nuestras opciones disponibles y ver si le recomendamos usarlos.",]
    ],
    [
        r"(.*)(Sol|sol|Fotocromaticos|fotocromaticos|Fotocromaticas|fotocromaticas)",
        ["Sí, tenemos una amplia selección de lentes de sol de marcas reconocidas. Puedes venir a nuestra tienda para ver nuestra colección completa.",]
    ],
    [
        r"(.*)(Ubicación|ubicación|Ubicacion|ubicacion|Ubican|ubican|ubica|Ubica|donde|Donde|queda|Queda)",
        ["Nos ubicamos en el Mercado 24 de enero, local 167, col. ---,municipio ---, Estado de México"]
    ],
    [
        r"(.*)(Telefono|telefono|numero|Número|Numero|número|whatsapp|Whatsapp|WhatsApp)",
        ["Tenemos Whatsapp con el numero 55 ---- --01"]
    ],
]

#  Al pobar el bot y hacerle cambios, hay que detenerlo, para eso esta clase
# Definimos la clase CustomChat que hereda de Chat
class CustomChat(Chat):

    # Definimos un método personalizado para iniciar la conversación
    def conversar(self, quit="adiós"):
        user_input = "" # Inicializamos una variable para almacenar la entrada del usuario
        print(Fore.GREEN +"Hola, esta es la optica Flores, tienen dudas con el horario semanal, precio de los lentes, tipos de lentes, ubicacion o numero?"+ Style.RESET_ALL)

        # Mientras la entrada del usuario no esté en la lista de palabras para terminar la conversación
        while user_input.lower() not in [quit, 'adios', 'Adios','Adiós','ADIOS', 'ADIÓS']:
            user_input = input("> ")# Pedimos al usuario que ingrese algo
            
            # Verificamos nuevamente si la entrada del usuario es una de las palabras para terminar
            if user_input.lower() in [quit, 'adios', 'Adios','Adiós','ADIOS', 'ADIÓS']:
                print(Fore.RED + "¡Gracias por visitarnos! Si tienes más preguntas, no dudes en hacérnoslas.", "Hasta luego, ¡que tengas un buen día!" + Style.RESET_ALL)  # Respuesta en color rojo
                break  # Rompemos el bucle para terminar la conversación

            else:
                response = self.respond(user_input)# Obtenemos la respuesta del chatbot usando el método respond de la clase Chat
                if(response!=None):
                    print(Fore.GREEN + response + Style.RESET_ALL)  # Respuesta en color verde
                else:
                    print(response)
            
# definimos el chatbot que vamos a usar (instancia)
def chatbot():
    """
    Inicia el chatbot y comienza la conversación con el usuario.
    """
    chat = CustomChat(pairs, reflections)
    chat.conversar()

# Probamos el chat
nltk.download('punkt')  # Descargar recursos necesarios para hacer la tokenizacion (dividir texto en palabras, oraciones, etc)
chatbot()