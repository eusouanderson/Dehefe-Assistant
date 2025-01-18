import pyttsx3
import speech_recognition as sr
from flask import Flask, jsonify

app = Flask(__name__)

# Configuração do sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 0.9)  # Volume da fala

# Nome do assistente
assistant_name = "Dehefe Assistant"

# Dicionário de respostas do assistente
responses = {
    "hello": f"Olá! Eu sou o {assistant_name}. Como posso ajudar você?",
    "weather": "Hoje está ensolarado com temperaturas entre 25 e 30 graus.",
    "time": "Desculpe, ainda não consigo dizer o horário, mas você pode verificar no relógio!",
    "exit": f"Até logo! Foi um prazer ajudar você. Assinado, {assistant_name}.",
}

# Função para o assistente responder
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, f"Desculpe, eu sou o {assistant_name} e ainda estou aprendendo. Não entendi o que você disse.")

# Função para capturar entrada de voz
def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{assistant_name} está ouvindo... Diga algo!")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            return "Não consegui entender o que você disse."
        except sr.RequestError as e:
            return f"Erro ao acessar o serviço de reconhecimento: {e}"

# Função para listar microfones
def list_microphones():
    print("Dispositivos de áudio disponíveis:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")

# Endpoint para entrada de áudio
@app.route('/audio', methods=['GET'])
def audio_assistant():
    # Captura entrada de voz
    user_input = capture_voice()
    
    # Processa a entrada e gera a resposta
    response = get_response(user_input)
    
    # Fala a resposta usando síntese de voz
    engine.say(response)
    engine.runAndWait()
    
    return jsonify({"message": user_input, "response": response})

# Ajuste para ruído ambiente e captura do microfone
def setup_microphone():
    list_microphones()
    
    with sr.Microphone(device_index=0) as source:  # Substitua 0 pelo índice do microfone correto
        print("Ajustando o microfone para o ruído ambiente... Aguarde.")
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        print("Pronto! Fale algo...")

if __name__ == '__main__':
    print(f"{assistant_name} está pronto para ajudar!")
    setup_microphone()
    app.run(debug=True)
