# Usa imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do backend para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar o backend
CMD ["python", "app.py"]
