import threading
import pyttsx3
import speech_recognition as sr
import os
from unidecode import unidecode
from flask import Flask, jsonify, send_from_directory
from responses import responses
from fuzzywuzzy import process  # Importar a função de comparação difusa
from calcHow.soma import calcular_soma_agora  # Importar a função de soma
import time

class Assistant:
    def __init__(self, name="Duda"):
        self.name = name
        self.active_until = 0
        self.assistant_on = True
        self.current_response = ""
        self.response_lock = threading.Lock()
        self.last_spoken_response = ""

    def get_response(self, user_input):
        user_input = unidecode(user_input.lower())
        best_match = process.extractOne(user_input, responses.keys())
        if best_match:
            matched_response = best_match[0]
            return responses.get(matched_response, "Desculpe, eu não entendi a sua pergunta. Pode reformular?")
        else:
            return "Desculpe, não entendi o que você disse."

    def capture_voice(self):
        self.last_spoken_response
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"{self.name} está ouvindo... Diga algo!")
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="pt-BR")
                text_no_accents = unidecode(text)  # Remover acentos da entrada

                # Verifica se a entrada é igual à última resposta falada
                if text_no_accents.strip() == self.last_spoken_response.strip():
                    print("Ignorando entrada auto-gerada.")
                    return ""  # Ignora a entrada

                print(f"Você disse: {text_no_accents}")
                return text_no_accents
            except sr.UnknownValueError:
                return "Nao consegui entender o que voce disse."
            except sr.RequestError as e:
                return f"Erro ao acessar o servico de reconhecimento: {e}"

    def response_to_name(self):
        with self.response_lock:
            engine = pyttsx3.init()
            engine.setProperty('rate', 200)
            engine.setProperty('volume', 1)
            engine.say("Oi, me chamou?")
            engine.runAndWait()
        self.current_response = ""

    def activate(self):
        self.active_until = time.time() + 200

    def is_active(self):
        return time.time() <= self.active_until

    def process_voice_input(self, user_input):
        print(f"Entrada de voz processada: {user_input}")

        if user_input.lower().startswith(self.name.lower()):
            self.activate()
            user_input = user_input[len(self.name):].strip()
            if not user_input.strip():
                self.response_to_name()
                return

        if self.is_active():
            self.handle_active_commands(user_input)
        else:
            self.speak("Esta assistente virtual esta desligada. Aguardando uma chamada...")
            print("Assistente inativa, aguardando ser chamada novamente.")

    def handle_active_commands(self, user_input):
        if user_input.lower() == "calcular" and self.assistant_on:
            self.speak("Me fale a expressão que deseja calcular.")
            user_input = self.capture_voice()
            result = calcular_soma_agora(user_input).replace("calcular", "").split()
            self.speak(result)

        elif user_input.lower() == "desligar" and self.assistant_on:
            self.speak("Tudo bem, vou desligar. Até logo!")
            self.assistant_on = False

        elif user_input.lower() == "ligar" and not self.assistant_on:
            self.speak("Olá, estou de volta. Como posso te ajudar?")
            self.assistant_on = True

        else:
            self.response = self.get_response(user_input)
            self.speak(self.response)

    def speak(self, text):
        try:
            with self.response_lock:
                engine = pyttsx3.init()
                engine.setProperty('rate', 200)
                engine.setProperty('volume', 1)
                engine.say(self.response)
                engine.runAndWait()
                engine.stop()
            self.last_spoken_response = unidecode(text)  # Armazena a resposta falada
        except Exception as e:
            error_message = f"Erro ao falar a resposta: {e}"
            self.speak(error_message)

    def listen_continuously(self):
        last_input = ""
        while True:
            user_input = unidecode(self.capture_voice())
            print(f"Entrada de voz: {user_input}")
            if user_input == last_input:
                continue
            last_input = user_input
            self.process_voice_input(user_input)

app = Flask(__name__)
assistant = Assistant()

@app.route('/audio', methods=['GET'])
def audio_assistant():
    return jsonify({"response": assistant.current_response})

@app.route('/')
def serve_html():
    return send_from_directory(directory=os.path.abspath("."), path='index.html')

if __name__ == '__main__':
    listening_thread = threading.Thread(target=assistant.listen_continuously, daemon=True)
    listening_thread.start()
    app.run(debug=True)
