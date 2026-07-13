FROM python:3.11-slim

# Install Chrome + Xvfb + shared libs seleniumbase/undetected-chromedriver need
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg ca-certificates \
    xvfb \
    libnspr4 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 \
    libxrandr2 libgbm1 libasound2 libpango-1.0-0 libpangocairo-1.0-0 \
    fonts-liberation \
    && wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y /tmp/chrome.deb \
    && rm /tmp/chrome.deb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# undetected-chromedriver needs a real display even in server environments
ENV DISPLAY=:99

CMD Xvfb :99 -screen 0 1920x1080x24 & python app.py
