def calcular_soma_agora(expressao):
    try:
        # Substitui os espaços e tenta avaliar a expressão
        resultado = eval(expressao)
        return f"O resultado da operação é {resultado}"
    except Exception as e:
        return "Desculpe, não consegui calcular. Verifique se a expressão está correta."
