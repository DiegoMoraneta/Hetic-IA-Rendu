## Introduction
------------
L'application MultiPDF Chat est une application Python qui vous permet de discuter avec plusieurs documents PDF. Vous pouvez poser des questions sur les PDF en utilisant le langage naturel, et l'application fournira des réponses pertinentes basées sur le contenu des documents. Cette application utilise un modèle de langage pour générer des réponses précises à vos requêtes. Veuillez noter que l'application ne répondra qu'aux questions liées aux PDF chargés.

## Comment ça marche
------------

L'application suit ces étapes pour fournir des réponses à vos questions :

1. Chargement des PDF : L'application lit plusieurs documents PDF et extrait leur contenu textuel.

2. Division du texte : Le texte extrait est divisé en petits morceaux qui peuvent être traités efficacement.

3. Modèle de langage : L'application utilise un modèle de langage pour générer des représentations vectorielles (embeddings) des morceaux de texte.

4. Correspondance de similarité : Lorsque vous posez une question, l'application la compare avec les morceaux de texte et identifie les plus similaires sémantiquement.

5. Génération de réponse : Les morceaux sélectionnés sont transmis au modèle de langage, qui génère une réponse basée sur le contenu pertinent des PDF.

6. J'ai essayé d'ajouter un moyen de remplacer l'OpenAI payant en utilisant HuggingFace, mais j'ai rencontré quelques problèmes en cours de route. Je vous encourage néanmoins à essayer de l'utiliser si vous avez besoin d'un LLM gratuit. N'oubliez pas d'obtenir une clé API de HuggingFace. https://huggingface.co/settings/tokens

## Dépendances et installation
----------------------------
Pour installer l'application MultiPDF Chat, veuillez suivre ces étapes :

1. Clonez le dépôt sur votre machine locale.

2. Installez les dépendances requises en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

3. Obtenez une clé API d'OpenAI et ajoutez-la au fichier `.env` dans le répertoire du projet.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Utilisation
-----
Pour utiliser l'application MultiPDF Chat, suivez ces étapes :

1. Assurez-vous d'avoir installé les dépendances requises et ajouté la clé API OpenAI au fichier `.env`.

2. Exécutez le fichier `main.py` en utilisant le CLI Streamlit. Exécutez la commande suivante :
    ```
    streamlit run app.py
    ```

3. L'application se lancera dans votre navigateur web par défaut.