# J.A.R.V.I.S - Assistente de IA Autônomo

Assistente de IA inteligente com agente autônomo usando Function Calling do Google Gemini. Frontend React + Backend Flask integrados em um único serviço.

## 🎯 Características

- **Agente Autônomo**: A IA decide automaticamente qual ferramenta usar
- **Function Calling**: Integração nativa com ferramentas do Gemini
- **Frontend + Backend Unificado**: Deploy simplificado em um único serviço
- **Múltiplas Capacidades**:
  - Chat inteligente
  - Busca na web em tempo real
  - Busca por localização (Google Maps)
  - Geração de imagens
  - Análise e edição de imagens
  - Geração de vídeos
  - Text-to-Speech

## 📁 Estrutura do Projeto

```
jarvis-unified/
├── backend/              # Backend Flask
│   ├── main.py          # Servidor principal (serve API + frontend)
│   ├── config.py
│   ├── database_schema.py
│   ├── gemini_integration.py
│   ├── jarvis_controller.py
│   ├── knowledge_base_manager.py
│   ├── learning_module.py
│   ├── rule_engine.py
│   └── requirements.txt
├── frontend/            # Frontend React
│   ├── src/
│   │   ├── App.tsx     # Componente principal com agente autônomo
│   │   ├── components/
│   │   ├── services/
│   │   │   ├── geminiService.ts
│   │   │   └── geminiTools.ts  # Definições de ferramentas
│   │   ├── hooks/
│   │   └── types.ts
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── build.sh            # Script de build
├── package.json        # Scripts de gerenciamento
└── render.yaml         # Configuração do Render
```

## 🚀 Deploy no Render

### Passo 1: Preparar o Repositório

1. Faça push deste código para o GitHub
2. Certifique-se de que todos os arquivos estão commitados

### Passo 2: Criar Serviço no Render

1. Acesse [Render Dashboard](https://dashboard.render.com/)
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: `jarvis-unified`
   - **Region**: Oregon (ou sua preferência)
   - **Branch**: `main` (ou sua branch principal)
   - **Root Directory**: deixe vazio
   - **Environment**: Python 3
   - **Build Command**: `./build.sh && pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && gunicorn main:app`

### Passo 3: Configurar Variáveis de Ambiente

No Render, adicione:
- **GEMINI_API_KEY**: Sua chave da API do Google Gemini
- **PORT**: 10000 (já configurado automaticamente)

### Passo 4: Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o build e deploy (pode levar alguns minutos)
3. Acesse a URL fornecida pelo Render

## 💻 Desenvolvimento Local

### Backend

```bash
# Instalar dependências
cd backend
pip install -r requirements.txt

# Configurar variável de ambiente
export GEMINI_API_KEY="sua-chave-aqui"

# Rodar servidor
python main.py
```

### Frontend

```bash
# Instalar dependências
cd frontend
npm install

# Rodar em modo dev
npm run dev
```

### Build Completo

```bash
# Na raiz do projeto
./build.sh
```

## 🔧 Configuração

### Variáveis de Ambiente Necessárias

- `GEMINI_API_KEY`: Chave da API do Google Gemini (obrigatória)
- `PORT`: Porta do servidor (padrão: 10000)

### Obter Chave da API Gemini

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova chave de API
3. Copie e configure no Render

## 📖 Como Usar

1. Acesse a URL do seu serviço no Render
2. Digite qualquer pergunta ou comando
3. O J.A.R.V.I.S decide automaticamente qual ferramenta usar
4. Exemplos:
   - "Qual é a notícia mais recente sobre IA?" → Usa busca web
   - "Gere uma imagem de um gato de chapéu" → Usa geração de imagem
   - "Onde fica o restaurante mais próximo?" → Usa Google Maps
   - "O que tem nesta imagem?" (com upload) → Usa análise de imagem

## 🛠️ Tecnologias

- **Frontend**: React, TypeScript, Vite, Tailwind CSS
- **Backend**: Flask, Python 3.11
- **IA**: Google Gemini API (Function Calling)
- **Deploy**: Render
- **Banco de Dados**: SQLite (local)

## 📝 Notas

- O frontend é buildado estaticamente e servido pelo Flask
- Todas as requisições de API vão para `/api/*`
- O agente autônomo processa uma ferramenta por vez (sequencial)
- Mensagens de status aparecem durante a execução das ferramentas
- Tratamento de erros robusto com feedback para a IA

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

MIT License
