import ollama 

def consultar_model(modelo, mensagens):

    resposta = ollama.chat(
        model = modelo, 
        messages = mensagens,
        stream = True
        )
    return resposta