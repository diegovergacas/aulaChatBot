# 🤖 Chatbot com Informações da Wikipédia usando Python e PLN

Este projeto é uma atividade desenvolvida para uma aula teste de professor em uma entidade de ensino que fica em São Paulo - Brasil, com foco na criação de **assistentes virtuais e chatbots** que proporcionem interações eficientes e naturais com os usuários.

## 🎯 Objetivo

Desenvolver um **chatbot simples**, utilizando bibliotecas Python e modelos de Processamento de Linguagem Natural (PLN), que seja capaz de consultar dados em tempo real da Wikipédia e responder perguntas formuladas pelo usuário. O projeto também respeita os princípios da **LGPD**, oferecendo uma aplicação prática com foco em ética e responsabilidade no uso da IA.

## 📌 O que o chatbot faz?

- Recebe o nome de uma celebridade como entrada.
- Busca o resumo dessa pessoa na Wikipédia (em português).
- Permite ao usuário fazer perguntas livres sobre essa celebridade.
- Usa um modelo pré-treinado de **Pergunta e Resposta (QA)** da Hugging Face para responder com base no conteúdo extraído.

## 💡 Tecnologias e Bibliotecas Utilizadas

- [`wikipedia`](https://pypi.org/project/wikipedia/): consulta e extrai textos diretamente da Wikipédia.
- [`transformers`](https://huggingface.co/docs/transformers): biblioteca da Hugging Face para modelos de linguagem natural.
- Modelo: `deepset/roberta-base-squad2` (pergunta e resposta).

## 🛠️ Como executar

1. Instale as bibliotecas necessárias:
   ```bash
   pip install wikipedia transformers
   ```

2. Execute o script:
   ```bash
   python bio.py
   ```

3. Siga as instruções no terminal:
   - Digite o nome de uma celebridade.
   - Faça perguntas sobre ela.
   - Digite `voltar` para mudar de celebridade ou `sair` para encerrar.

## 📚 Exemplos de uso

```bash
Nome da celebridade: Albert Einstein

Pergunte algo sobre essa pessoa ('voltar' para trocar de celebridade): Onde ele nasceu?
Bot: Ulm

Pergunte algo sobre essa pessoa ('voltar' para trocar de celebridade): Qual era a profissão dele?
Bot: físico teórico
```

## 🚧 Próximos passos

Nas próximas aulas, será desenvolvida uma **interface web** para tornar o chatbot mais amigável e acessível ao público geral.

## ✨ Mensagem final

> “Você não está apenas aprendendo a programar máquinas – está aprendendo a criar experiências humanas com tecnologia.  
> O futuro da IA começa com a sua curiosidade.” – *ChatGPT, junho 2025*
