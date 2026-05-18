# WhatsApp Mistral Bot 🤖

Un chatbot WhatsApp intelligent alimenté par Mistral AI. Ce bot reçoit des messages via un webhook, les traite avec l'API Mistral et renvoie des réponses intelligentes.

## 🚀 Démarrage rapide

### Prérequis
- Python 3.8+
- Une clé API Mistral (obtenir sur [mistral.ai](https://mistral.ai))
- Twilio pour la gestion de WhatsApp (optionnel)

### Installation

1. **Cloner le repository**
```bash
git clone https://github.com/lejuriste237/whatsapp-mistral-bot.git
cd whatsapp-mistral-bot
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditer .env et ajouter votre clé Mistral API
```

### Lancer le serveur

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

L'API sera disponible sur `http://localhost:8000`

## 📋 API Endpoints

### GET `/`
Vérifie que le bot fonctionne
```bash
curl http://localhost:8000/
```

### POST `/webhook`
Reçoit les messages WhatsApp et retourne une réponse
```bash
curl -X POST http://localhost:8000/webhook \
  -d "Body=Bonjour"
```

## 🔧 Configuration Twilio

Pour intégrer avec WhatsApp via Twilio :

1. Créer un compte sur [Twilio](https://www.twilio.com)
2. Configurer un numéro WhatsApp
3. Dans la console Twilio, définir le webhook :
   - **URL**: `https://votre-domaine.com/webhook`
   - **Method**: POST

## 📦 Dépendances

- **FastAPI**: Framework web moderne et rapide
- **Uvicorn**: Serveur ASGI
- **Requests**: Client HTTP pour Mistral API
- **python-dotenv**: Gestion des variables d'environnement

## 🛠️ Structure du projet

```
whatsapp-mistral-bot/
├── main.py              # Point d'entrée de l'application
├── requirements.txt     # Dépendances Python
├── .env.example         # Configuration template
├── .gitignore           # Fichiers à ignorer
└── README.md            # Cette documentation
```

## 🤝 Contribuer

Les contributions sont bienvenues! N'hésitez pas à :
- Ouvrir des issues
- Proposer des pull requests
- Améliorer la documentation

## 📝 Licence

Ce projet est open source.

## 📧 Support

Pour toute question, veuillez ouvrir une issue sur GitHub.
