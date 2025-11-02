#!/bin/bash
set -e

echo "🚀 Iniciando build do J.A.R.V.I.S..."

# Instalar dependências do frontend
echo "📦 Instalando dependências do frontend..."
cd frontend
npm install

# Build do frontend
echo "🔨 Construindo frontend..."
npm run build

echo "✅ Build concluído com sucesso!"
echo "📁 Frontend buildado em: frontend/dist"
