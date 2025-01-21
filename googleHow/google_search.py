from googlesearch import search

def pesquisar_no_google(consulta, num_resultados=5):
    """
    Faz uma pesquisa no Google e retorna os links encontrados.

    :param consulta: Termo ou frase a ser pesquisada.
    :param num_resultados: Número de resultados a serem retornados.
    :return: Lista de links encontrados.
    """
    try:
        resultados = search(consulta, num_results=num_resultados, lang="pt")
        return list(resultados)
    except Exception as e:
        print(f"Erro ao realizar a pesquisa: {e}")
        return []


