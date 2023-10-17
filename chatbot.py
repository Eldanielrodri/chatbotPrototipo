class Chatbot:
    def __init__(self):
        self.state = "initial"

    def respond(self, user_input):
        user_input = user_input.lower()

        if self.state == "initial":
            if "hola" in user_input or "hola" in user_input:
                self.state = "greeting"
                return "¡Hola! ¿En qué puedo ayudarte?"
            elif "adiós" in user_input or "chao" in user_input:
                self.state = "goodbye"
                return "Hasta luego."
            else:
                return "No entiendo. ¿Puedes repetir?"
        
        elif self.state == "greeting":
            if "¿cómo estás?" in user_input:
                return "Estoy bien, gracias por preguntar. ¿En qué puedo ayudarte?"
            elif "adiós" in user_input or "chao" in user_input:
                self.state = "goodbye"
                return "Hasta luego."
            else:
                return "¿En qué más puedo ayudarte?"
        
        elif self.state == "goodbye":
            return "Adiós. ¡Espero verte pronto."

if __name__ == "__main__":
    bot = Chatbot()
    print("Bot: ¡Hola! Soy un chatbot simple. Puedes saludar o hacer preguntas simples. Para salir, escribe 'adiós'.")

    while bot.state != "goodbye":
        user_input = input("Tú: ")
        response = bot.respond(user_input)
        print("Bot:", response)
