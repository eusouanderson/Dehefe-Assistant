import threading
import pyttsx3
import speech_recognition as sr
import os
import re
from unidecode import unidecode
from flask import Flask, jsonify, send_from_directory
from responses import responses
from fuzzywuzzy import process  # Importar a função de comparação difusa
from calcHow.calcular import calcular_soma_agora  # Importar a função de soma
import time

log_buffer = []

class Assistant:
    def __init__(self, name="Maria"):
        self.name = name
        self.active_until = 0
        self.assistant_on = True
        self.current_response = ""
        self.last_input = ""
        self.recent_responses = []
        self.response_lock = threading.Lock()
        self.last_spoken_response = ""

    def get_response(self, user_input, min_score=88):
        user_input = unidecode(user_input.lower())
        best_match = process.extractOne(user_input, responses.keys())
        if best_match:
            matched_response, score = best_match  # A tupla best_match tem dois elementos: a resposta e a pontuação
            if score >= min_score:
                return responses.get(matched_response, "Desculpe, eu não entendi a sua pergunta. Pode reformular?")
            else:
                return "Desculpe, não consegui encontrar uma correspondência satisfatória."
        else:
            return "Desculpe, não entendi o que você disse."

    def wait_for_question(self):
        print(f"{self.name} está aguardando sua pergunta...")
        while True:
            user_input = self.capture_voice()
            if user_input:
                print(f"Você disse: {user_input}")
                self.process_voice_input(user_input)
                break
    
    def capture_voice(self):
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 300  # Ajusta a sensibilidade do reconhecimento de voz
        
        try:
            # Seleciona o microfone e começa a ouvir
            with sr.Microphone() as source:
                print(f"{self.name} está ouvindo... Diga algo!")
                
                # Adiciona um tempo limite para evitar loops eternos ao escutar
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                # Faz o reconhecimento de voz
                text = recognizer.recognize_google(audio, language="pt-BR")
                text_no_accents = unidecode(text).strip()
                
                # Verifica se a entrada é igual à última resposta falada
                if text_no_accents == self.last_spoken_response:
                    print("Ignorando entrada auto-gerada.")
                    return ""  # Ignora a entrada gerada pela assistente
                
                print(f"Você disse: {text_no_accents}")
                return text_no_accents
    
        except sr.UnknownValueError:
            # Caso o reconhecimento não entenda o áudio
            print("Não consegui entender o que você disse.")
            return "Nao consegui entender o que voce disse."
    
        except sr.RequestError as e:
            # Caso haja erro ao acessar o serviço de reconhecimento
            print(f"Erro ao acessar o serviço de reconhecimento: {e}")
            return f"Erro ao acessar o servico de reconhecimento: {e}"
    
        except Exception as e:
            # Tratamento genérico para outros erros
            print(f"Erro inesperado: {e}")
            return f"Erro inesperado: {e}"


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
        print(f"Estado do assistente: {self.assistant_on} @@@@@@@@@@@@@@@@@")  # Imprime o estado do assistente (self.assistant_on)

        # Verifica se a assistente está ativa
        if not self.assistant_on:
            print("Assistente inativa, aguardando ser chamada novamente.")
            return

        # Adiciona verificação para ignorar a mesma entrada repetida
        if user_input.strip() == self.last_input.strip():
            print("Entrada repetida, ignorando.")
            return

        # Armazena a última entrada processada
        self.last_input = user_input.strip()

        # Ignora entradas que correspondem a respostas recentes
        if user_input.strip() == self.last_spoken_response:
            print("Ignorando a própria resposta.")
            return
        self.activate()
        # Verifica se o nome da assistente foi mencionado
        '''if user_input.lower().startswith(self.name.lower()):
            self.activate()  # Ativa a assistente
            user_input = user_input[len(self.name):].strip()

            # Se não houver nada além do nome, ela entra em modo de espera
            if not user_input.strip():
                self.response_to_name()
                self.wait_for_question()  # Aguarda a próxima entrada
                return'''

        # Processa comandos se a assistente estiver ativa
        if self.is_active():
            self.handle_active_commands(user_input)

    def handle_active_commands(self, user_input):
         
         # Condição para ligar o assistente
        if user_input.lower() == "ligar" and not self.assistant_on:
            self.speak("Olá, estou de volta. Como posso te ajudar?")
            self.assistant_on = True
        
        # Condição para desligar o assistente
        if user_input.lower() == "desligar" and self.assistant_on:
            self.speak("Tudo bem, vou desligar. Até logo!")
            self.assistant_on = False

        # Condição para iniciar o modo de cálculo
        elif user_input.lower() == "calcular" and self.assistant_on:
            self.speak("Me fale a expressão que deseja calcular.")
            while True:  # Loop para continuar aguardando a expressão de cálculo
                user_input = self.capture_voice()  # Captura a voz do usuário
                
                if user_input:  # Apenas processa se houver uma entrada válida
                    
                    # Condição para sair do modo de cálculo
                    if "sair de calcular" in user_input.lower():
                        self.speak("Saindo do modo de cálculo.")
                        break  # Encerra o loop de cálculo
                    
                    user_input = user_input.replace("vezes", "*").replace("dividido por", "/").replace("mais", "+").replace("menos", "-").replace("x", "*")
                    if re.match(r'^[0-9+\-*/().\s]+$', user_input):
                        try:
                            result = calcular_soma_agora(user_input).replace("calcular", "").strip()
                            if not result:
                                self.speak("Desculpe, não consegui entender a expressão. Tente novamente.")

                            self.speak(result)
                            
                        except Exception as e:
                            self.speak("Desculpe, não consegui entender a expressão. Tente novamente.")
                            print(f"Erro no cálculo: {e}")
                    else:
                        self.speak("Não entendi a expressão. Tente novamente.")  # Caso a entrada seja inválida

        # Caso nenhuma das condições anteriores seja atendida, responde normalmente
        else:
            self.response = self.get_response(user_input)
            if self.response != self.last_spoken_response:  # Evita repetir a mesma resposta
                self.speak(self.response)

    def speak(self, text):
        if not text or not text.strip():
            return  # Ignora texto vazio
        
        # Evita falar repetidamente a mesma coisa
        if self.last_spoken_response == unidecode(text):
            return
        
        try:
            with self.response_lock:
                engine = pyttsx3.init()
                engine.setProperty('rate', 200)
                engine.setProperty('volume', 1)
                self.last_spoken_response = unidecode(text)  # Salva a resposta
                self.recent_responses.append(unidecode(text))  # Adiciona à lista de respostas recentes
                # Limita o tamanho da lista para evitar crescimento indefinido
                if len(self.recent_responses) > 5:
                    self.recent_responses.pop(0)
                
                engine.say(text)
                engine.runAndWait()

            # Aguarda brevemente para evitar autoescuta
            time.sleep(0.5)
        except Exception as e:
            print(f"Erro ao falar a resposta: {e}")

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
