FROM python:3

# Todo lo que esté en el path lo copie al container
COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
