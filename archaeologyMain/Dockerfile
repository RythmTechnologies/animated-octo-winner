# Adım 1: Python tabanlı bir görüntü kullan
FROM python:3.12


ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizinini ayarla
WORKDIR /home/archaeology

# Bağımlılıkları kopyala ve kur
COPY requirements.txt /home/archaeology

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Adım 2: Uygulama kodunu kopyala
COPY . .