FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
