FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y ffmpeg
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]