from datetime import datetime

def numero_para_palavra(num):
    numeros_extenso = {
        0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
        12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
        17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte", 21: "vinte e um",
        22: "vinte e dois", 23: "vinte e três", 24: "vinte e quatro", 25: "vinte e cinco",
        26: "vinte e seis", 27: "vinte e sete", 28: "vinte e oito", 29: "vinte e nove",
        30: "trinta", 31: "trinta e um", 32: "trinta e dois", 33: "trinta e três",
        34: "trinta e quatro", 35: "trinta e cinco", 36: "trinta e seis", 37: "trinta e sete",
        38: "trinta e oito", 39: "trinta e nove", 40: "quarenta", 41: "quarenta e um",
        42: "quarenta e dois", 43: "quarenta e três", 44: "quarenta e quatro",
        45: "quarenta e cinco", 46: "quarenta e seis", 47: "quarenta e sete",
        48: "quarenta e oito", 49: "quarenta e nove", 50: "cinquenta", 51: "cinquenta e um",
        52: "cinquenta e dois", 53: "cinquenta e três", 54: "cinquenta e quatro",
        55: "cinquenta e cinco", 56: "cinquenta e seis", 57: "cinquenta e sete",
        58: "cinquenta e oito", 59: "cinquenta e nove"
    }
    return numeros_extenso.get(num, str(num))

def obter_tempo_agora():
    tempo_agora = datetime.now()

    hora_extenso = numero_para_palavra(tempo_agora.hour)
    minuto_extenso = numero_para_palavra(tempo_agora.minute)
    
    # Tratar "meia hora" de forma especial
    if tempo_agora.minute == 30:
        minuto_extenso = "meia"
    
    # Ajuste para "hora" ou "horas"
    if tempo_agora.hour == 1:
        hora_extenso = f"uma hora"
    elif tempo_agora.hour == 0:
        hora_extenso = f"meia hora"
    elif tempo_agora.hour > 1:
        hora_extenso = f"{hora_extenso} horas"
    
    # Ajuste para "minuto" ou "minutos"
    if tempo_agora.minute == 1:
        minuto_extenso = "um minuto"
    elif tempo_agora.minute == 0:
        minuto_extenso = ""  # Não dizemos minutos se for 0
    else:
        minuto_extenso = f"{minuto_extenso} minutos"

    # Se o minuto for zero, a resposta será apenas a hora
    if tempo_agora.minute == 0:
        return f"{hora_extenso}"
    
    return f"{hora_extenso} e {minuto_extenso}"

