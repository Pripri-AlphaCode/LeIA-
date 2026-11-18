import streamlit as st
from leia.cliente_ollama import consultar_model


MODELO = "gpt-oss:20b"


def aplicar_estilo_figma():
    st.markdown(
        """
        <style>
        /* Fundo principal em degradê Azul Profundo e Roxo Violeta */
        .stApp {
            background: radial-gradient(circle at 15% 15%, #1e1347 0%, #0d0924 55%, #05030f 100%);
            color: #f8fafc;
        }

        /* Barra Lateral (Sidebar) com visual encorpado e colorido */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #16103b 0%, #0d0926 100%);
            border-right: 1px solid rgba(139, 92, 246, 0.35);
            box-shadow: 4px 0 30px rgba(0, 0, 0, 0.5);
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p {
            color: #f1f5f9 !important;
        }

        /* Colorindo os Menus Suspensos (Selectbox) da Sidebar */
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: linear-gradient(135deg, rgba(49, 36, 117, 0.85) 0%, rgba(30, 22, 77, 0.9) 100%) !important;
            border: 1px solid rgba(167, 139, 250, 0.45) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stSelectbox"] [role="group"] {
            background: linear-gradient(135deg, rgba(49, 36, 117, 0.85) 0%, rgba(30, 22, 77, 0.9) 100%) !important;
            border: 1px solid rgba(167, 139, 250, 0.45) !important;
            border-radius: 10px !important;
            overflow: hidden;
        }

        section[data-testid="stSidebar"] [data-testid="stSelectbox"] input[role="combobox"] {
            background: transparent !important;
            border: 0 !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stSelectbox"] button {
            background: transparent !important;
            border: 0 !important;
            color: #c4b5fd !important;
        }

        [data-testid="stSelectboxVirtualDropdown"] {
            background: linear-gradient(135deg, #211b50 0%, #13112f 100%) !important;
            border: 1px solid rgba(167, 139, 250, 0.55) !important;
            border-radius: 12px !important;
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
        }

        [data-testid="stSelectboxVirtualDropdown"] [role="option"] {
            color: #e2e8f0 !important;
            border-radius: 8px;
        }

        [data-testid="stSelectboxVirtualDropdown"] [role="option"]:hover,
        [data-testid="stSelectboxVirtualDropdown"] [role="option"][data-selected="true"] {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.5) 0%, rgba(139, 92, 246, 0.5) 100%) !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] textarea,
        section[data-testid="stSidebar"] input[type="text"] {
            background-color: rgba(30, 22, 77, 0.85) !important;
            border: 1px solid rgba(167, 139, 250, 0.45) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] textarea::placeholder,
        section[data-testid="stSidebar"] input::placeholder {
            color: #94a3b8 !important;
        }

        /* Opções de aprendizagem em cartões, como no painel do Figma */
        section[data-testid="stSidebar"] [data-testid="stRadioGroup"] {
            gap: 0.55rem;
        }

        section[data-testid="stSidebar"] [data-testid="stRadioOption"] {
            background: linear-gradient(135deg, rgba(35, 26, 87, 0.75) 0%, rgba(24, 18, 62, 0.85) 100%);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 12px;
            padding: 0.65rem 0.75rem;
            margin: 0;
            transition: all 0.25s ease;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }

        section[data-testid="stSidebar"] [data-testid="stRadioOption"]:hover {
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.4) 0%, rgba(139, 92, 246, 0.4) 100%);
            border-color: #a78bfa;
            box-shadow: 0 0 12px rgba(139, 92, 246, 0.3);
        }

        section[data-testid="stSidebar"] [data-testid="stRadioGroup"] > div[data-selected="true"] > [data-testid="stRadioOption"] {
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.48) 0%, rgba(109, 72, 196, 0.48) 100%);
            border-color: rgba(167, 139, 250, 0.75);
            box-shadow: 0 0 14px rgba(139, 92, 246, 0.2);
        }

        section[data-testid="stSidebar"] [data-testid="stRadioOption"] [data-testid="stMarkdownContainer"] p {
            color: #e2e8f0 !important;
            font-size: 0.84rem !important;
            line-height: 1.4 !important;
            margin: 0 !important;
        }

        /* Título Principal (mantido exatamente como você aprovou) */
        .titulo-leia {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(90deg, #c4b5fd 0%, #818cf8 50%, #93c5fd 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: -0.5rem;
            margin-bottom: 0.1rem;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        .subtitulo-leia {
            color: #94a3b8;
            font-size: 0.98rem;
            margin-bottom: 1.2rem;
        }

        /* Balões de Mensagem do Chat Coloridos e com Leitura Ultra Nítida */
        div[data-testid="stChatMessage"] {
            background: linear-gradient(135deg, rgba(42, 31, 102, 0.85) 0%, rgba(26, 20, 68, 0.9) 100%);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(167, 139, 250, 0.45);
            border-left: 4px solid #8b5cf6;
            border-radius: 16px;
            padding: 1.1rem 1.3rem;
            margin-bottom: 0.9rem;
            box-shadow: 0 6px 24px rgba(15, 10, 40, 0.45);
        }

        div[data-testid="stChatMessage"] p,
        div[data-testid="stChatMessage"] li,
        div[data-testid="stChatMessage"] span {
            color: #ffffff !important;
            font-size: 1.02rem !important;
            line-height: 1.55 !important;
        }

        div[data-testid="stChatMessage"] strong {
            color: #c4b5fd !important;
            font-weight: 700 !important;
        }

        /* Botões de Ação e Sugestões Rápidas */
        div.stButton > button {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.25) 0%, rgba(139, 92, 246, 0.35) 100%);
            color: #f8fafc;
            border: 1px solid rgba(167, 139, 250, 0.45);
            border-radius: 12px;
            padding: 0.45rem 0.8rem;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.25s ease;
            width: 100%;
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            border-color: #c4b5fd;
            color: #ffffff;
            box-shadow: 0 0 15px rgba(139, 92, 246, 0.5);
            transform: translateY(-1px);
        }

        /* Barra inferior e campo de mensagem do chat */
        [data-testid="stBottom"] > div {
            background: rgba(5, 5, 20, 0.96) !important;
        }

        div[data-testid="stChatInput"] {
            background: linear-gradient(135deg, rgba(26, 30, 70, 0.98) 0%, rgba(25, 22, 65, 0.98) 100%) !important;
            border: 1px solid rgba(139, 92, 246, 0.5) !important;
            border-radius: 14px !important;
            box-shadow: 0 6px 24px rgba(15, 10, 40, 0.35);
        }

        div[data-testid="stChatInput"] > div {
            background: transparent !important;
        }

        div[data-testid="stChatInput"] textarea {
            color: #f8fafc !important;
        }

        div[data-testid="stChatInput"] textarea::placeholder {
            color: #8e9ac5 !important;
        }

        div[data-testid="stChatInput"] button {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
            border: 1px solid rgba(196, 181, 253, 0.65) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }

        div[data-testid="stChatInput"] button:hover {
            background: linear-gradient(135deg, #7c7ff7 0%, #a06bf7 100%) !important;
            box-shadow: 0 0 14px rgba(139, 92, 246, 0.45);
        }

        header[data-testid="stHeader"] {
            background: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def processar_pergunta(pergunta_usuario: str):
    mensagens = st.session_state.mensagens
    mensagens.append({"role": "user", "content": pergunta_usuario})

    with st.chat_message("user"):
        st.markdown(pergunta_usuario)

    with st.chat_message("assistant"):
        try:
            trechos = consultar_model(modelo=MODELO, mensagens=mensagens)

            texto_resposta = st.write_stream(
                trecho.message.content
                for trecho in trechos
                if trecho.message.content
            )
        except Exception as erro:
            st.error(f"Erro ao gerar a resposta: {erro}")
            return

        if not texto_resposta:
            st.warning("O modelo retornou uma resposta sem texto.")
            return

        mensagens.append({"role": "assistant", "content": texto_resposta})


def iniciar_interface():
    st.set_page_config(
        page_title="LeIA - Lecionador Inteligente e Adaptativo",
        page_icon="🤖",
        layout="wide"
    )

    aplicar_estilo_figma()

    # -------------------------------------------------------------
    # BARRA LATERAL (Painel de Mapeamento Cognitivo e Pedagógico)
    # -------------------------------------------------------------
    st.sidebar.markdown("## ⚙️ Painel do Aluno")
    st.sidebar.caption("Personalize sua experiência de tutoria em APC.")
    st.sidebar.divider()

    nivel_aluno = st.sidebar.selectbox(
        "Nível atual em programação",
        ["Iniciante Absoluto", "Iniciante", "Intermediário"]
    )

    # Menu de Estilo de Aprendizagem idêntico ao Figma com todas as opções solicitadas
    estilo_escolhido = st.sidebar.radio(
        "Como você prefere aprender?",
        [
            "💡 Analogias Práticas (Exemplos do dia a dia)",
            "📐 Passo a Passo Lógico (Estrutura mental e matemática)",
            "🧱 Blocos Estruturados (Sintaxe e lógica direta)",
            "🛠️ Depuração de Código (Investigue o erro antes da correção)",
            "❓ Revisão por Perguntas (Perguntas curtas com retorno imediato)",
            "✏️ Outros (Escreva o modelo que deseja usar)"
        ]
    )

    # Se o aluno escolher "Outros", exibe campo de texto personalizado na barra lateral
    estilo_final = estilo_escolhido
    if "Outros" in estilo_escolhido:
        outro_estilo = st.sidebar.text_input(
            "Descreva seu modelo personalizado:",
            placeholder="Ex: Foco em analogias com música..."
        )
        if outro_estilo.strip():
            estilo_final = f"Outros: {outro_estilo}"

    topico_estudo = st.sidebar.selectbox(
        "Tópico de estudo atual",
        [
            "Laços de Repetição (for/while)",
            "Variáveis e Tipos de Dados",
            "Estruturas Condicionais (if/else)",
            "Funções em Python",
            "Listas e Dicionários"
        ]
    )

    objetivo_aluno = st.sidebar.text_area(
        "O que você quer alcançar?",
        placeholder="Quero aprender Python de forma construtiva, passo a passo, até chegar à resposta...",
        height=85
    )

    botao_aplicar = st.sidebar.button("✨ Aplicar Preferências")

    # -------------------------------------------------------------
    # GERENCIAMENTO DE ESTADO E PROMPT SOCRÁTICO
    # -------------------------------------------------------------
    if "mensagens" not in st.session_state or botao_aplicar:
        foco_extra = f" Objetivo específico declarado pelo aluno: {objetivo_aluno}." if objetivo_aluno.strip() else ""
        prompt_sistema = (
            f"Você é o LeIA (Lecionador Inteligente e Adaptativo), um tutor de Algoritmos e Programação de Computadores (APC) "
            f"empático, acolhedor e socrático. Responda sempre em Português do Brasil. "
            f"Perfil atual do aluno: Nível {nivel_aluno}, estilo de aprendizagem escolhido: {estilo_final}, "
            f"estudando o tópico {topico_estudo}.{foco_extra} "
            f"DIRETRIZ DE OURO: Nunca entregue o código pronto de exercícios. "
            f"Guie o aluno passo a passo com perguntas orientadoras, analogias claras e feedback positivo."
        )

        st.session_state.mensagens = [
            {"role": "system", "content": prompt_sistema},
            {
                "role": "assistant",
                "content": (
                    f"Olá! Vi que você quer estudar **{topico_estudo}** usando **{estilo_final}**. "
                    f"Vamos lá: pense no processo de forma construtiva. "
                    f"Qual é o seu primeiro passo ou desafio com código hoje?"
                )
            }
        ]

    # -------------------------------------------------------------
    # ÁREA PRINCIPAL (Cabeçalho, Sugestões Rápidas e Chat)
    # -------------------------------------------------------------
    st.markdown('<div class="titulo-leia">🤖 LeIA: Lecionador Inteligente e Adaptativo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo-leia">Sua plataforma inteligente e adaptativa para o aprendizado de Algoritmos e Programação de Computadores (APC).</div>',
        unsafe_allow_html=True
    )

    st.caption("💡 Sugestões rápidas para começar:")
    col1, col2, col3 = st.columns(3)
    sugestao_clicada = None

    with col1:
        if st.button("O que range(5) faz?"):
            sugestao_clicada = "O que range(5) faz no Python?"
    with col2:
        if st.button("Como repetir até uma condição?"):
            sugestao_clicada = "Como repetir até uma condição em Python?"
    with col3:
        if st.button("Quero um exercício prático"):
            sugestao_clicada = "Me dê um exercício prático guiado"

    st.divider()

    # Renderização do histórico do chat
    for msg in st.session_state.mensagens:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Dispara pergunta se o aluno clicou em uma sugestão rápida
    if sugestao_clicada:
        processar_pergunta(sugestao_clicada)
        st.rerun()

    if pergunta := st.chat_input("Digite sua dúvida ou cole um trecho de código Python..."):
        processar_pergunta(pergunta)