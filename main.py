import logging
import os
import queue
import threading
import time
from typing import List

import pyttsx3
import speech_recognition as sr
from flask import Flask, jsonify, send_from_directory
from unidecode import unidecode
from waitress import serve

from config.clean_prompt import clean_prompt
from gemini_client import Gemini

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Constantes
RESPONSE_TIMEOUT = 10
AUDIO_ENERGY_THRESHOLD = 300
AUDIO_TIMEOUT = 5
AUDIO_PHRASE_LIMIT = 10
SPEECH_RATE = 200
ACTIVE_DURATION = 200  # segundos


class Assistant:
    def __init__(self, name: str = 'Maria'):
        self.name = name
        self.active_until = 0.0
        self.assistant_on = True
        self.current_response = ''
        self.last_input = ''
        self.recent_responses: List[str] = []
        self.response_lock = threading.Lock()
        self.last_spoken_response = ''
        self.command_queue = queue.Queue()
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = AUDIO_ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = True
        self.engine = None
        self.listening_active = True
        self.tts_lock = threading.Lock()
        self.is_speaking = False
        self.speech_cooldown = 0.5
        self.last_speech_time = 0

    def _init_tts_engine(self):
        """Inicializa ou reinicializa o motor de texto para fala."""
        with self.tts_lock:
            try:
                if self.engine:
                    try:
                        self.engine.endLoop()
                    except:
                        pass
                
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', SPEECH_RATE)
                self.engine.setProperty('volume', 1)
                logger.info("Motor TTS inicializado/reinicializado")
                return self.engine
            except Exception as e:
                logger.error(f'Erro ao inicializar o motor TTS: {e}')
                raise

    def activate(self, duration: float = ACTIVE_DURATION) -> None:
        """Ativa o assistente por um período de tempo."""
        self.active_until = time.time() + duration
        logger.info(f'Assistente ativado por {duration} segundos')

    def is_active(self) -> bool:
        """Verifica se o assistente está ativo."""
        return time.time() <= self.active_until

    @staticmethod
    def get_response(user_input: str) -> str:
        """Obtém resposta do assistente IA."""
        user_input = unidecode(user_input.lower())
        try:
            if assistant_IA:
                return clean_prompt(assistant_IA.ask(user_input))
        except Exception as e:
            logger.error(f'Erro ao obter resposta do Gemini: {e}')
        return ''

    def capture_voice(self) -> str:
        if not self.listening_active or self.is_speaking:
            return ''

        if (time.time() - self.last_speech_time) < self.speech_cooldown:
            return ''

        try:
            with sr.Microphone() as source:
                logger.info(f'{self.name} está ouvindo... Diga algo!')
                self.recognizer.adjust_for_ambient_noise(source, duration=1.5)

                try:
                    audio = self.recognizer.listen(
                        source,
                        timeout=AUDIO_TIMEOUT,
                        phrase_time_limit=AUDIO_PHRASE_LIMIT,
                    )
                    text = self.recognizer.recognize_google(audio, language='pt-BR')
                    text_no_accents = unidecode(text).strip()

                    if text_no_accents == self.last_spoken_response:
                        logger.debug('Ignorando eco da própria resposta.')
                        return ''

                    logger.info(f'Você disse: {text_no_accents}')
                    return text_no_accents

                except sr.UnknownValueError:
                    logger.debug("Não foi possível entender o áudio")
                except sr.RequestError as e:
                    logger.error(f"Erro no serviço de reconhecimento: {e}")
                except sr.WaitTimeoutError:
                    logger.debug('Tempo de escuta esgotado sem capturar áudio.')

        except Exception as e:
            logger.error(f'Erro no reconhecimento de voz: {str(e)}', exc_info=True)
            
        return ''

    def process_voice_input(self, user_input: str) -> None:
        """Processa a entrada de voz do usuário."""
        if not user_input or not self.listening_active:
            return

        logger.info(f'Processando entrada: {user_input}')

        self.last_input = user_input.strip()
        self.activate()

        if self.is_active():
            self.listening_active = False

            try:
                command = user_input.lower()

                if command == 'ligar' and not self.assistant_on:
                    self.speak('Olá, estou de volta. Como posso te ajudar?')
                    self.assistant_on = True
                elif command == 'desligar' and self.assistant_on:
                    self.speak('Tudo bem, vou desligar. Até logo!')
                    self.assistant_on = False
                else:
                    try:
                        response = self.get_response(user_input)
                        if response:
                            self.speak(response)
                    except Exception as e:
                        logger.error(f'Erro ao obter resposta: {str(e)}')
                        self.speak('Desculpe, não consegui processar sua solicitação.')
            except Exception as e:
                logger.error(f'Erro ao processar comando: {str(e)}')
            finally:
                self.listening_active = True
                logger.info(f'{self.name} está ouvindo novamente...')

    def speak(self, text: str) -> None:
        if not text or not text.strip():
            return

        def _speak_inner():
            self.is_speaking = True
            normalized_text = unidecode(text)
            
            if normalized_text == self.last_spoken_response:
                self.is_speaking = False
                return

            with self.response_lock:
                try:
                    logger.info(f'Maria vai falar: {text}')
                    self.last_spoken_response = normalized_text
                    self.recent_responses.append(normalized_text)

                    if len(self.recent_responses) > RESPONSE_TIMEOUT:
                        self.recent_responses.pop(0)

                    if self.engine is None:
                        self._init_tts_engine()

                    self.engine.say(text)
                    self.engine.runAndWait()
                    
                    self.last_speech_time = time.time()
                    time.sleep(0.5)
                    
                except Exception as e:
                    logger.error(f'Erro ao falar a resposta: {e}')
                    try:
                        self._init_tts_engine()
                        self.engine.say(text)
                        self.engine.runAndWait()
                        self.last_speech_time = time.time()
                    except Exception as e2:
                        logger.error(f'Falha ao reinicializar TTS: {e2}')
                finally:
                    self.is_speaking = False
                    self.listening_active = True

        threading.Thread(target=_speak_inner, daemon=True).start()

    def listen_continuously(self) -> None:
        """Ouve continuamente por comandos de voz."""
        while True:
            try:
                if not self.is_speaking and \
                   (time.time() - self.last_speech_time) >= self.speech_cooldown:
                    
                    user_input = self.capture_voice()
                    if user_input:
                        self.process_voice_input(user_input)
                
                time.sleep(0.1)
                
            except Exception as e:
                logger.error(f'Erro na escuta contínua: {str(e)}')
                time.sleep(1)


# Inicializa o cliente Gemini
assistant_IA = Gemini()

# Configuração do Flask
app = Flask(__name__)
assistant = Assistant()


@app.route('/audio', methods=['GET'])
def audio_assistant():
    return jsonify({
        'response': assistant.current_response,
        'status': 'active' if assistant.is_active() else 'inactive',
    })


@app.route('/')
def serve_html():
    return send_from_directory(
        directory=os.path.abspath('.'), path='index.html'
    )


def create_app():
    """Factory function para criar a aplicação Flask"""
    return app


def run_assistant():
    """Inicia o assistente em modo de produção"""
    listening_thread = threading.Thread(
        target=assistant.listen_continuously, daemon=True
    )
    listening_thread.start()
    logger.info('Assistente iniciado e pronto para receber comandos')


def run_production():
    """Executa a aplicação em modo produção"""
    serve(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run_assistant()
    run_production()