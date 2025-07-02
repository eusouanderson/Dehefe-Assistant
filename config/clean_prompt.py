import re

def clean_prompt(texto: str) -> str:
    # Remove tags HTML (se houver)
    texto = re.sub(r'<[^>]+>', '', texto)

    # Remove links markdown [texto](url)
    texto = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', texto)

    # Remove símbolos comuns de markdown: *, **, __, ``, >, #, -, +, !
    texto = re.sub(r'[*_`>#\-+!]+', '', texto)

    # Remove emojis (baseado em blocos Unicode)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # símbolos e pictogramas
        "\U0001F680-\U0001F6FF"  # transporte e símbolos
        "\U0001F1E0-\U0001F1FF"  # bandeiras
        "\U00002700-\U000027BF"  # dingbats
        "\U000024C2-\U0001F251"  # vários outros
        "]+",
        flags=re.UNICODE,
    )
    texto = emoji_pattern.sub(r'', texto)

    # Remove múltiplos espaços
    texto = re.sub(r'\s{2,}', ' ', texto)

    # Remove espaços no começo/fim
    texto = texto.strip()

    return texto
