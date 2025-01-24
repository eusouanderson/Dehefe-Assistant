import re

def calcular_soma_agora(expressao):
    print(f"Expressão de cálculo: {expressao}")
    try:
        # Mapeamento de palavras para operadores matemáticos
        mapeamento = {
            "x": "*",  # Multiplicação
            "mais": "+",  # Adição
            "menos": "-",  # Subtração
            "dividido": "/",  # Divisão
            "vezes": "*",  # Vezes como multiplicação
            "por": "*"  # 'por' também como multiplicação
        }

        # Substitui palavras-chave pelos operadores
        for palavra, operador in mapeamento.items():
            expressao = expressao.replace(palavra, operador)
        
        # Remove espaços em branco da expressão
        expressao = expressao.replace(" ", "")
        
        # Verifica se a expressão contém apenas números e operadores matemáticos válidos
        if not re.match(r'^[\d\+\-\*/\(\)\.\s]+$', expressao):
            raise ValueError("Expressão inválida. Apenas números e operadores matemáticos são permitidos.")
        
        # Avalia a expressão matematicamente
        resultado = eval(expressao)
        
        # Verifica se o resultado é um número válido
        if isinstance(resultado, (int, float)):
            print(f"Resultado da operação: {resultado}")
            return f"O resultado da operação é {resultado}"
        else:
            raise ValueError("Resultado da operação não é válido.")
    except Exception as e:
        return 
