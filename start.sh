#!/bin/bash

# WhatsApp Mistral Bot - Startup Script for Replit

echo "🚀 Starting WhatsApp Mistral Bot..."
echo "=================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "✅ .env created. Please update with your MISTRAL_API_KEY in Replit Secrets"
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Run the server
echo "✅ Starting FastAPI server..."
echo "🌐 Server running at http://0.0.0.0:8000"
echo "📝 API docs at http://0.0.0.0:8000/docs"
echo ""

uvicorn main:app --host 0.0.0.0 --port 8000
