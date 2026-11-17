from leia.cliente_ollama import consultar_model

Pergunta = input("Digite sua pergunta: ")

mensagem = [
    {"role": "system", "content": "Você é um tutor IA para iniciantes neurotípicos que querem aprender a programar em Python."}, 
    {"role": "user", "content": Pergunta}
]

resposta = consultar_model(modelo = "qwen3.5:0.8b", mensagens = mensagem)
print(resposta)