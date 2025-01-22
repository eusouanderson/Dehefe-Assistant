from datetime import datetime
import pytz

def numero_para_palavra(numero):
    numeros_por_extenso = {
        0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
        11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze",
        16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte",
        21: "vinte e um", 22: "vinte e dois", 23: "vinte e três", 30: "trinta"
    }
    return numeros_por_extenso.get(numero, str(numero))

def obter_tempo_agora():
    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    tempo_agora = datetime.now(fuso_brasilia)

    hora = tempo_agora.hour
    minuto = tempo_agora.minute

    hora_extenso = numero_para_palavra(hora)
    minuto_extenso = numero_para_palavra(minuto)

    if minuto == 30:
        minuto_extenso = "meia"

    if hora == 1:
        hora_extenso = "uma hora"
    elif hora == 0:
        hora_extenso = "meia-noite"
    elif hora > 1:
        hora_extenso = f"{hora_extenso} horas"

    if minuto == 1:
        minuto_extenso = "um minuto"
    elif minuto == 0:
        minuto_extenso = ""
    else:
        minuto_extenso = f"{minuto_extenso} minutos"

    if minuto == 0:
        return f"{hora_extenso}"
    return f"{hora_extenso} e {minuto_extenso}"
