# Utilisez l'image de base Python pour créer une image Docker
FROM python:3.9-slim-buster

# Définissez le répertoire de travail pour l'application
WORKDIR /app

# Copiez les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiez tous les fichiers du projet dans le conteneur
COPY . .

# Définissez l'exécutable par défaut pour le conteneur
CMD [ "python", "./main.py" ]
