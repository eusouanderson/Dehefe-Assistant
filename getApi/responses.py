import requests

BASE_URL = 'http://localhost:3000/api/responses'  


def send_phrase(phrase, response):
    payload = {
        'phrase': phrase,
        'response': response
    }
    try:
        response = requests.post(BASE_URL, json=payload)
        if response.status_code == 201:
            print(f"Frase enviada com sucesso: {phrase}")
        else:
            print(f"Erro ao enviar frase: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar requisição: {e}")

def get_phrases():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            phrases = response.json()
            result = []
            for item in phrases:
                result.append(f"{item['phrase']}: {item['response']}")
            return result
        else:
            print(f"Erro ao pegar frases: {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro ao enviar requisição: {e}")
        return []

# Exemplos de uso
if __name__ == "__main__":
    # Enviar uma frase
    send_phrase('Olá', 'Oi! Como posso ajudar?')

    # Pegar todas as frases
    response = get_phrases()
    print(response)