# Agente IA para Instalações Elétricas

Um agente de inteligência artificial projetado para auxiliar profissionais e pessoas leigas da área de construção civil, especialmente no segmento elétrico, a tomar decisões seguras e eficientes com base nas melhores práticas, normas técnicas e cálculos especializados.

---

## 🧠 Objetivo

O objetivo deste projeto é oferecer uma API inteligente capaz de:

- Responder dúvidas sobre instalações elétricas residenciais e comerciais.
- Realizar cálculos elétricos (bitolas, disjuntores, potência, etc.).
- Buscar informações técnicas em normas e documentos específicos (ex: NBR 5410).
- Auxiliar na tomada de decisão com explicações baseadas em boas práticas.

A aplicação está sendo construída com foco em modularidade e escalabilidade, utilizando IA generativa (LLMs) local através do Ollama.

---

## ⚙️ Tecnologias Utilizadas

- **FastAPI** – API rápida e moderna em Python
- **Ollama** – LLM local para processamento de linguagem natural
- **Pydantic** – Validação de dados e configurações
- **Python 3.11+**
- **Requests** – Cliente HTTP para comunicação com Ollama

---

## 🖥️ Como Rodar o Projeto Localmente

### 1. Pré-requisitos

- Python 3.11 ou superior
- Ollama instalado e rodando localmente ([Instruções de instalação do Ollama](https://ollama.ai/))
- Git

### 2. Clone o repositório

```bash
git clone https://github.com/fsantosfp/effies-app-ia-electrical.git
cd effies-app-ia-electrical
```

### 3. Crie e ative um ambiente virtual
```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Linux/macOS
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Inicie o Ollama
Certifique-se de que o Ollama está rodando localmente na porta padrão (11434)

### 6. Execute a API
```bash
uvicorn main:app --reload
```

## 🚀 Usando a API

A API possui um endpoint principal para interação com o agente:

### POST /ask
Envie perguntas para o agente através deste endpoint:

```json
{
  "agent": "assistant",
  "message": "Sua pergunta sobre instalações elétricas aqui"
}
```

Exemplo de uso:
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"agent": "assistant", "message": "Quantas tomadas posso colocar em um circuito de 2,5mm?"}'
```

## 📁 Estrutura do Projeto
```
agente-eletrica/
│
├── app/
│   ├── agents/
│   │   └── agent_selector.py    # Seleção de agentes especializados
│   ├── core/
│   │   └── agent.py            # Lógica principal do agente
│   └── services/
│       └── ollama_client.py    # Cliente para comunicação com Ollama
│
├── main.py                     # Ponto de entrada da API
├── requirements.txt            # Dependências do projeto
└── README.md
```

## 📌 Roadmap
- [x] Criação do repositório e documentação inicial
- [x] Setup da API com FastAPI
- [x] Integração com Ollama
- [x] Sistema de seleção de agentes
- [ ] Módulo de cálculos elétricos
- [ ] Base de conhecimento técnico expandida
- [ ] Interface Web ou Mobile (futura)

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuindo
Se você deseja contribuir com melhorias ou novos módulos, fique à vontade para abrir uma issue ou enviar um pull request.

## 🐛 Problemas Conhecidos
- Certifique-se de que o Ollama está rodando localmente antes de iniciar a API
- O modelo padrão usado é o gemma:7b, certifique-se de tê-lo baixado no Ollama