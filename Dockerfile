FROM python:3.9-slim

WORKDIR /app

COPY . /app/


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]

#docker build -t pj1-a .
#docker run -it --rm -v "$(pwd)/algoritmos":/app/algoritmos -v "$(pwd)/assets":/app/assets -v "$(pwd)/data":/app/data -v "$(pwd)/src":/app/src pj1-ia
