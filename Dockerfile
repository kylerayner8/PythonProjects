FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/app"

ENTRYPOINT ["python", "./scripts/generate_email.py"]