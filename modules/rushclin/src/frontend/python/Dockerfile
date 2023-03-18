FROM python:3.10 AS build

ENV DASH_DEBUG_MODE True
WORKDIR /app
COPY ./app/requirements.txt /app/
RUN set -ex && \
    pip install -r requirements.txt

FROM build

COPY ./app /app
EXPOSE 8050
CMD ["python", "app.py"]
