import threading
import pyttsx3
import speech_recognition as sr
import os
from unidecode import unidecode
from flask import Flask, jsonify, send_from_directory
from responses import responses
from fuzzywuzzy import process  # Importar a função de comparação difusa
from calcHow.soma import calcular_soma_agora # Importar a função de soma

app = Flask(__name__)

# Nome do assistente
assistant_name = "Duda"

assistant_on = True  # Variável para controlar o estado do assistente

# Variáveis globais
current_response = ""
response_lock = threading.Lock()  # Criação do Lock para sincronizar as threads

# Função para o assistente responder com comparação difusa
def get_response(user_input):
    user_input = unidecode(user_input.lower())  # Remover acentos e transformar em minúsculas
    # Usar fuzzywuzzy para buscar a melhor correspondência da entrada do usuário nas respostas disponíveis
    best_match = process.extractOne(user_input, responses.keys())
    if best_match:
        matched_response = best_match[0]
        return responses.get(matched_response, "Desculpe, eu não entendi a sua pergunta. Pode reformular?")
    else:
        return "Desculpe, eu sou um assistente virtual e ainda estou aprendendo. Não entendi o que você disse."

# Função para capturar entrada de voz
def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{assistant_name} está ouvindo... Diga algo!")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="pt-BR")
            text_no_accents = unidecode(text)  # Remover acentos da entrada
            print(f"Você disse: {text_no_accents}")
            return text_no_accents
        except sr.UnknownValueError:
            return "Nao consegui entender o que voce disse."
        except sr.RequestError as e:
            return f"Erro ao acessar o servico de reconhecimento: {e}"

# Função para capturar a resposta ao ser chamado pelo nome do assistente
def response_to_name():
    with response_lock:
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 1)
        engine.say("Oi, me chamou?")
        engine.runAndWait()

# Função que ficará ouvindo continuamente
def listen_continuously():
    global current_response, assistant_on  # Acessa a variável global assistant_on
    
    while True:
        # Captura entrada de voz
        user_input = unidecode(capture_voice())  
        print(f"Entrada de voz: {user_input}")
        
        if user_input.lower() == "calcular" and assistant_on:
            engine = pyttsx3.init()
            engine.setProperty('rate', 200)
            engine.setProperty('volume', 1)
            engine.say("Me fale a expressão que deseja calcular.")
            engine.runAndWait()
            engine.stop()
            user_input = unidecode(capture_voice())
            current_response = calcular_soma_agora(user_input).replace("calcular", "").split()
            try:
                with response_lock:
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 200)
                    engine.setProperty('volume', 1)
                    engine.say(f"{current_response}")
                    engine.runAndWait()
                    engine.stop()
            except Exception as e:
                print(f"Erro ao falar a resposta: {e}")
            continue  # Continua o loop, esperando nova entrada
            
        # Se disser "desligar", desliga o assistente
        if user_input.lower() == "desligar" and assistant_on:
            print("Assistente desligado.")
            assistant_on = False  # Muda o estado para desligado
            try:
                with response_lock:
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 200)
                    engine.setProperty('volume', 1)
                    engine.say("Tudo bem, vou desligar. Até logo!")
                    engine.runAndWait()
                    engine.stop()
            except Exception as e:
                print(f"Erro ao falar a resposta: {e}")
            continue  # Continua o loop, esperando nova entrada
        
        # Se disser "ligar", reinicia o assistente
        if user_input.lower() == "ligar" and not assistant_on:
            print("Assistente ligado.")
            assistant_on = True  # Muda o estado para ligado
            try:
                with response_lock:
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 200)
                    engine.setProperty('volume', 1)
                    engine.say("Olá, estou de volta. Como posso te ajudar?")
                    engine.runAndWait()
                    engine.stop()
            except Exception as e:
                print(f"Erro ao falar a resposta: {e}")
            continue  # Continua o loop, esperando nova entrada
        
        # Se o assistente estiver ligado, processa a entrada
        if assistant_on:
            # Verifica se a entrada começa com o nome do assistente
            
            if user_input.lower().startswith(assistant_name.lower()):
                user_input = user_input[len(assistant_name):].strip()  # Remove o nome do assistente da entrada

                # Responde imediatamente se apenas o nome for chamado
                if not user_input.strip():
                    response_to_name()
                    continue

                # Processa apenas se a entrada não estiver vazia
                if user_input.strip():
                    response = get_response(user_input)  # Processa a entrada e gera a resposta
                    current_response = response
                    try:
                        with response_lock:  # Evita chamadas simultâneas ao pyttsx3
                            engine = pyttsx3.init()
                            engine.setProperty('rate', 200)
                            engine.setProperty('volume', 1)
                            engine.say(response)
                            engine.runAndWait()
                            engine.stop()
                    except Exception as e:
                        print(f"Erro ao falar a resposta: {e}")
                else:
                    print("Entrada vazia, nada para processar.")
            else:
                if user_input.lower() != user_input.lower().strip():
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 200)
                    engine.setProperty('volume', 1)
                    engine.say(f"Oi, oque você quer saber sobre {user_input}. Pode repetir?")
                    engine.runAndWait()
                    engine.stop()
                print("Pergunta não reconhecida, sem prefixo do assistente.")
        else:
            print("Assistente desligado, aguardando comando de 'ligar'.")

@app.route('/audio', methods=['GET'])
def audio_assistant():
    global current_response
    return jsonify({"response": current_response})

# Rota para servir o arquivo HTML
@app.route('/')
def serve_html():
    return send_from_directory(directory=os.path.abspath("."), path='index.html')

if __name__ == '__main__':
    # Iniciar a escuta contínua em uma thread separada para não bloquear o Flask
    listening_thread = threading.Thread(target=listen_continuously, daemon=True)
    listening_thread.start()
    
    # Iniciar o servidor Flask
    app.run(debug=True)
