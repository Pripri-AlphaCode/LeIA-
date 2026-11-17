import streamlit as st
from leia.cliente_ollama import consultar_model

MODELO = "qwen3.5:9b"

def iniciar_interface():
    st.set_page_config(
        page_title="LeIA - Lecionador para você",
        page_icon="🤖",
        layout="wide"
    )

    # Barra Lateral (Mapeamento do Perfil do Aluno)
    st.sidebar.title("⚙️ Painel do Aluno")
    st.sidebar.markdown("Configure seu perfil para personalizar a tutoria em **APC**.")

    nivel_aluno = st.sidebar.selectbox(
        "Qual o seu nível atual em programação?",
        ["Iniciante Absoluto", "Intermediário", "Avançado"]
    )

    estilo_preferido = st.sidebar.radio(
        "Como prefere que a IA explique?",
        ["Analogias Práticas (Dia a dia)", "Passo a Passo Lógico", "Blocos Diretos de Código"]
    )

    topico_estudo = st.sidebar.selectbox(
        "Qual tópico de APC deseja estudar hoje?",
        [
            "Variáveis e Tipos de Dados",
            "Estruturas Condicionais (if/else)",
            "Laços de Repetição (for/while)",
            "Funções em Python"
        ]
    )

    botao_aplicar = st.sidebar.button("Aplicar Preferências")

    # Histórico e Prompt de Sistema (adaptado do seu main.py original)
    if "mensagens" not in st.session_state or botao_aplicar:
        prompt_sistema = (
            f"Você é um tutor IA empático e socrático (LeIA) para iniciantes que querem aprender a programar em Python. "
            f"Perfil atual do aluno: Nível {nivel_aluno}, prefere explicações com {estilo_preferido}, "
            f"estudando o tópico {topico_estudo}. "
            f"Nunca entregue o código pronto de exercícios; guie o aluno com perguntas e dicas."
        )
        
        st.session_state.mensagens = [
            {"role": "system", "content": prompt_sistema},
            {
                "role": "assistant",
                "content": f"Olá! Sou o **LeIA**. Vi que você quer estudar **{topico_estudo}** com foco em **{estilo_preferido}**. Qual é a sua primeira dúvida hoje?"
            }
        ]

    # Área Principal do Chat
    st.title("🤖 LeIA: Lecionador para você")
    st.markdown("*Sua plataforma web adaptativa para o aprendizado de Algoritmos e Programação de Computadores (APC).*")
    st.divider()

    for msg in st.session_state.mensagens:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Entrada de texto substituindo o antigo input() do terminal
    if pergunta := st.chat_input("Digite sua dúvida ou cole seu código Python aqui..."):
        st.session_state.mensagens.append({"role": "user", "content": pergunta})
        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            with st.spinner("LeIA está pensando na melhor orientação..."):
                try:
                    # Chama exatamente a SUA função do cliente_ollama.py!
                    resposta_completa = consultar_model(modelo=MODELO, mensagens=st.session_state.mensagens)
                    texto_resposta = resposta_completa["message"]["content"]
                    
                    st.markdown(texto_resposta)
                    st.session_state.mensagens.append({"role": "assistant", "content": texto_resposta})
                except Exception:
                    st.error(f"Erro ao conectar com o Ollama. Verifique se o aplicativo está rodando e se o modelo `{MODELO}` está baixado.")