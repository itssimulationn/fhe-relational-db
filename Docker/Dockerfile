FROM zamafhe/concrete-ml

# Installer les bibliothèques supplémentaires
RUN pip install fastapi uvicorn sqlparse pydantic

# Définir le répertoire de travail
WORKDIR /workspace

# Commande par défaut
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]