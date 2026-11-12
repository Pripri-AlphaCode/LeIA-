from leia.cliente_ollama import consultar_model

from time import perf_counter, sleep

Pergunta = input("Digite sua pergunta: ")

#O tempo de uma letra para outra
WAIT_LETTER = 0.05

mensagem = [
    {"role": "system", "content": "Você é um tutor IA, chamado LeIA, para iniciantes neurotípicos que querem aprender a programar em Python."}, 
    {"role": "user", "content": Pergunta}
]

answer = consultar_model(modelo = "gpt-oss:20b", mensagens = mensagem)

time_start = perf_counter()

print("\nLeIA: ", end = "",  flush = True)

for piece in answer:
    text = piece.message.content
    for letters in text:
        print(letters, end="", flush=True)
        sleep(WAIT_LETTER)

time_end = perf_counter()
print(f'\nDemorou {time_end - time_start:.3} segundos, para responder')

