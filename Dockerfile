
FROM python:3.11.9
RUN aptupdate -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip install -y torch
RUN pip install transformers accelerate 

CMD ["python", "app.py"]


