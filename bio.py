#Importação das bibliotecas
import wikipedia
from transformers import pipeline
'''
wikipedia: biblioteca Python que permite acessar e extrair conteúdo diretamente da Wikipédia.
transformers: biblioteca da Hugging Face que traz modelos de IA para PLN. A função pipeline facilita o uso desses modelos prontos.
'''

# Configura idioma para português ou inglês
wikipedia.set_lang("pt")
'''
Define o idioma para as buscas da Wikipedia.
"pt" para português. Pode ser trocado para "en" (inglês), "es" (espanhol), etc.
'''

# Carrega pipeline de pergunta e resposta
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
'''
Cria um pipeline especializado em responder perguntas com base em um texto (modelo do tipo Question Answering).
O modelo usado aqui é o roberta-base-squad2, treinado com base em perguntas e respostas (SQuAD v2).
'''

# Mensagem inicial
print("Chatbot de celebridades baseado na Wikipédia.")
print("Digite o nome de uma celebridade ou 'sair' para encerrar.\n")
# Apresenta instruções no terminal para o usuário saber como interagir.

# Loop principal: usuário escole a celebridade
while True:
    nome = input("Nome da celebridade: ")
    if nome.lower() in ["sair", "exit", "quit"]:
        print("Encerrando...")
        break
        '''
        O programa entra em loop até o usuário digitar "sair".
        O nome.lower() transforma o input em minúsculas, garantindo que "Sair" ou "SAIR" funcionem também.
        '''

    try:
        # Busca o resumo da Wikipedia
        resumo = wikipedia.summary(nome, sentences=5)
        print(f"\nResumo de {nome}:\n{resumo}\n")
        '''
        Busca o resumo da página da Wikipédia referente à celebridade.
        Traz as 5 primeiras sentenças.
        '''

        # Novo loop: perguntas sobre esse celebridade
        while True:
            pergunta = input("Pergunte algo sobre essa pessoa ('voltar' para trocar de celebridade): ")
            if pergunta.lower() in ["voltar", "volta", "back"]:
                print()
                break

            resposta = qa_pipeline(question=pergunta, context=resumo)
            print("Bot:", resposta['answer'], "\n")
            '''
            Enquanto o usuário quiser perguntar, ele pode digitar livremente.
            A IA busca responder com base no resumo da Wikipédia.
            question=pergunta, context=resumo é o coração do modelo de question answering.
            '''

    # Tratamento de erros
    except wikipedia.exceptions.PageError:
        print("❌ Não encontrei essa pessoa na Wikipédia. Tente outro nome.\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print("⚠️ Esse nome é ambíguo. Exemplos encontrados:", e.options[:5], "\n")
        '''
        PageError: página não encontrada.
        DisambiguationError: a Wikipedia tem muitas páginas com esse nome (ex: "Silva") — o programa mostra até 5 opções.
        '''
