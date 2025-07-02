import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # ← Aqui ele carrega GOOGLE_API_KEY do .env

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

import concurrent.futures

class Gemini:
    def __init__(self):
        self.model = genai.GenerativeModel(model_name='models/gemini-2.0-flash')

    def ask(self, prompt: str, timeout: int = 10) -> str:
        print(f'[Gemini] Pergunta: {prompt}')
        
        # Adiciona a instrução no prompt original
        instrucoes = (
            "\n\nPor favor, responda em blocos curtos de até duas linhas por parágrafo. "
            "Evite respostas longas ou parágrafos grandes."
        )
        prompt_formatado = prompt.strip() + instrucoes
        
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(self.model.generate_content, prompt_formatado)
                response = future.result(timeout=timeout)

            resposta = response.text.strip()
            print(f'[Gemini] Resposta: {resposta}')
            return resposta
        except concurrent.futures.TimeoutError:
            print('[Gemini] Erro: Tempo limite excedido.')
            return 'A IA demorou demais para responder, Problema com a conexão.'
        except Exception as e:
            print(f'[Gemini] Erro: {e}')
            return 'Desculpe, ocorreu um erro ao acessar a IA.'




