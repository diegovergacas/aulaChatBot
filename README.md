# 🤖 Aula Teste – Chatbot com Python, Wikipédia e PLN

**Professor:** Diego Vergaças  
**Formato:** Aula teste para vaga docente – Inteligência Artificial  
**Ferramentas:** Lousa digital + Terminal Python + Biblioteca Transformers + Wikipedia API

---

## 🎯 Objetivo

Demonstrar como construir um **chatbot baseado em perguntas e respostas** com dados da Wikipédia, utilizando técnicas de **Processamento de Linguagem Natural (PLN)** e bibliotecas Python, com foco em:

- Extração de conhecimento via API pública (Wikipedia)
- Uso de modelo pré-treinado de Pergunta e Resposta (QA)
- Interação textual natural, respeitando princípios da LGPD
- Aplicação prática com código simples e comentado

---

## 📚 Conteúdo da Aula

- Diferença entre **chatbots regidos por regras** e **assistentes virtuais inteligentes**
- Importância da IA e do PLN na criação de interfaces mais humanas
- Consulta e tratamento de texto com a biblioteca `wikipedia`
- Uso do modelo `deepset/roberta-base-squad2` com Hugging Face
- Implementação de perguntas e respostas com `transformers.pipeline`
- Loop de interação via terminal com troca de contexto (celebridade)

---

## 💡 Exemplos de uso

```bash
Nome da celebridade: Albert Einstein

Pergunte algo sobre essa pessoa ('voltar' para trocar de celebridade): Onde ele nasceu?
Bot: Ulm

Pergunte algo sobre essa pessoa ('voltar' para trocar de celebridade): Qual era a profissão dele?
Bot: físico teórico
```

---

## 💻 Execução no Terminal

1. Instale as bibliotecas:
   ```bash
   pip install wikipedia transformers
   ```

2. Rode o script:
   ```bash
   python bio.py
   ```

---

## 📂 Arquivos deste repositório

- `aulaTesteChatGithub.pdf` – Slides da apresentação com base teórica e prática
- `bio.py` – Código completo do chatbot com interações e comentários

---

## ✨ Frase de Encerramento

> **"Você não está apenas aprendendo a programar máquinas – está aprendendo a criar experiências humanas com tecnologia."**  
> O futuro da IA começa com a sua curiosidade – e com o primeiro `input()` que você ousar digitar.
