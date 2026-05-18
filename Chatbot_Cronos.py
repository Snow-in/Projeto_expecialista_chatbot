import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# 1. Configuração da Chave de API (Substitua 'SUA_CHAVE_AQUI' pela sua chave real)
os.environ['GROQ_API_KEY'] = 'SUA_CHAVE_AQUI'

def inicializar_bot():
    try:
        # 2. Configura o modelo Llama 3.3 70b
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
        return llm
    except Exception as e:
        # UX: Explicação amigável de erro de conexão ou chave
        print(f"\n[ERRO DE CONEXÃO] Não consegui falar com o servidor Groq.")
        print(f"Detalhe técnico: {e}")
        print("Dica: Verifique se sua API Key está correta e se você tem internet.\n")
        return None

def chatbot_academico():
    llm = inicializar_bot()
    if not llm: return # Interrompe se o bot não iniciar

    # 3. Definição da Persona e Estrutura de UX
    # O System Prompt molda o comportamento: Organizado, Prático e Didático.
    system_prompt = (
        "Você é o Chronos, um Assistente Pessoal de Agenda Digital especializado em estudantes universitários. "
        "Sua missão é organizar conteúdos, horários, dias, meses e anos de forma lógica. "
        "Sempre priorize a clareza e ajude o usuário a evitar sobrecarga de tarefas."
    )

    # Memória simples para a sessão atual
    historico = []

    print("-" * 50)
    print("🎓 CHRONOS: SEU ASSISTENTE DE ESTUDOS")
    print("Digite 'x' a qualquer momento para encerrar.")
    print("-" * 50)

    # 4. Coleta de Perfil (UX Personalizada)
    perfil_usuario = input("\nChronos: Olá! Para eu te ajudar, descreva: qual seu curso e que tipo de estudante você é? (Ex: procrastinador, focado, trabalha e estuda...)\nVocê: ")

    # Adicionamos o perfil ao contexto inicial do bot
    contexto_usuario = f"O usuário é um estudante de: {perfil_usuario}. Adapte suas sugestões a esse perfil."

    print(f"\nChronos: Entendido! Perfil configurado como '{perfil_usuario}'. Como posso organizar seu dia hoje?")

    # 5. Loop Principal de Conversa (Ponto 5 da especificação)
    while True:
        try:
            entrada = input("\nVocê: ")

            # Condição de saída
            if entrada.lower() == 'x':
                print("\nChronos: Agenda fechada. Bons estudos e até logo!")
                break

            # 6. Construção do Prompt dinâmico
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("system", contexto_usuario),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
            ])

            # Criação da "chain" (corrente) de execução
            chain = prompt | llm

            # 7. Execução e Resposta
            resposta = chain.invoke({"input": entrada, "chat_history": historico})

            # Exibição da resposta com foco em UX
            print(f"\nChronos: {resposta.content}")

            # Atualiza histórico para manter o contexto da conversa
            historico.append(HumanMessage(content=entrada))
            historico.append(AIMessage(content=resposta.content))

        except Exception as e:
            # UX: Tratamento de erro durante a conversa
            print("\n[OPS!] Tive um pequeno problema ao processar seu pedido.")
            print("Pode tentar reescrever de outra forma? (Erro: Limite de requisições ou falha de rede)")

# Iniciar o programa
if __name__ == "__main__":
    chatbot_academico()
