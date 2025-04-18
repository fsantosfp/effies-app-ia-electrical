# Agente IA para Instalações Elétricas

Um agente de inteligência artificial projetado para auxiliar profissionais e pessoas leigas da área de construção civil, especialmente no segmento elétrico, a tomar decisões seguras e eficientes com base nas melhores práticas, normas técnicas e cálculos especializados.

---

## 🧠 Objetivo

O objetivo deste projeto é oferecer uma API inteligente capaz de:

- Responder dúvidas sobre instalações elétricas residenciais e comerciais.
- Realizar cálculos elétricos (bitolas, disjuntores, potência, etc.).
- Buscar informações técnicas em normas e documentos específicos (ex: NBR 5410).
- Auxiliar na tomada de decisão com explicações baseadas em boas práticas.

A aplicação está sendo construída com foco em modularidade e escalabilidade, utilizando IA generativa (LLMs), busca semântica e ferramentas especializadas para cálculo.

---

## ⚙️ Tecnologias Utilizadas

- **FastAPI** – API rápida e moderna em Python.
- **LangChain** – Framework para agentes de IA.
- **OpenAI GPT-4** – LLM principal via API.
- **FAISS** – Busca semântica local baseada em vetores.
- **Python 3.10+**
- (Em breve) suporte a modelos locais com **Ollama**

---

## 🖥️ Como Rodar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/fsantosfp/effies-app-ia-electrical.git

cd effies-app-ia-electrical
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv

venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS
```

### 3. Instale as dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure sua chave da OpenAI
```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 5. Execute a API
```bash
uvicorn app.main:app --reload
```

## 📁 Estrutura Inicial do Projeto
```
agente-eletrica/
│
├── app/
│   └── main.py          # Ponto de entrada da API
│
├── .env.example         # Exemplo de variáveis de ambiente
├── .gitignore
├── requirements.txt     # Dependências do projeto
└── README.md
```

## 📌 Roadmap Inicial
 - [x] Criação do repositório e documentação inicial

 - [ ] Setup da API com FastAPI

 - [ ] Configuração do agente LangChain

 - [ ] Módulo de cálculos elétricos

 - [ ] Base vetorial com conteúdo técnico (normas)

 - [ ] Interface Web ou Mobile (futura)

 ## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuindo
Se você deseja contribuir com melhorias ou novos módulos, fique à vontade para abrir uma issue ou enviar um pull request.