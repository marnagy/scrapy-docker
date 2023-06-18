FROM python:3.10.10-bullseye

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir playwright scrapy-playwright scrapinghub-entrypoint-scrapy psycopg2-binary \
    && playwright install --with-deps chromium \
    && mv /root/.cache/ms-playwright /ms-playwright \
    && mv /ms-playwright/chromium-* /ms-playwright/chromium \
    # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && chmod -Rf 777 /ms-playwright

COPY . .

CMD ["scrapy", "crawl", "srealityspider"] 
