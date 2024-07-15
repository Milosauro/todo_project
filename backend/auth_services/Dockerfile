FROM python:3.9-slim

WORKDIR /app

COPY ./ /app

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt
RUN pip3 install fastapi uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]