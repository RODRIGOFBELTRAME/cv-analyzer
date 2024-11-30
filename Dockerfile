# Use a imagem base do Python 3.11
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Execute os comandos de configuração
RUN python analyze/create_job.py
RUN python analyze/import_cv.py

# Exponha a porta do Streamlit
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "analyze/app.py", "--server.port=8080", "--server.address=0.0.0.0"]