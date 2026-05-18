# Projeto_expecialista_chatbot
 

# 🎓 Chronos: Assistente Pessoal de Agenda Digital

O **Chronos** é um chatbot inteligente desenvolvido em Python voltado para estudantes universitários que precisam otimizar sua rotina, organizar cronogramas de estudos e gerenciar o tempo de forma eficiente. 

Este projeto utiliza Engenharia de Prompts avançada e Grandes Modelos de Linguagem (LLMs) via **LangChain** e **Groq Cloud**, moldando as respostas dinamicamente com base no perfil comportamental do aluno.

---

## 🎯 Características do Projeto e Foco em UX

O software foi construído seguindo diretrizes estritas de **User Experience (UX)** para interfaces de linha de comando (CLI):

* **Design Centrado no Aluno:** Sistema de onboarding inicial que mapeia o curso e o perfil (ex: focado, trabalhador, procrastinador) para personalizar o tom e a densidade das respostas.
* **Arquitetura de Dados Temporal:** Prompt do sistema projetado para segmentar informações de maneira estruturada por **conteúdo, horários, dia, mês e ano**.
* **Tratamento Resiliente de Erros:** Mensagens amigáveis que traduzem exceções técnicas (como queda de rede ou falha de chave) em instruções claras de resolução para o usuário.
* **Memória de Curto Prazo:** Implementação de histórico de mensagens (`MessagesPlaceholder`) para manter o contexto completo durante a sessão de chat.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3
* **LLM Engine:** `llama-3.3-70b-versatile` (via Groq APIs)
* **Framework de Orquestração:** LangChain (`langchain_groq` e `langchain_core`)

---

## 🚀 Como Executar o Projeto

Este projeto foi validado para rodar perfeitamente tanto em ambiente local quanto no **Google Colab**.

### Passo 1: Obter a API Key do Groq
1. Acesse o site do [Groq Cloud Console](https://console.groq.com/).
2. Crie uma conta gratuita e navegue até a seção **API Keys**.
3. Gere uma nova chave 
4. Substitua a parte "SUA_CHAVE_AQUI" e cole a chave API criada
5. Depois so roda o código

### Passo 2: Instalação das Dependências
Antes de executar o script, instale as bibliotecas oficiais necessárias executando o comando abaixo no seu terminal ou em uma célula do Colab:

```bash
pip install -q langchain-groq langchain-core
