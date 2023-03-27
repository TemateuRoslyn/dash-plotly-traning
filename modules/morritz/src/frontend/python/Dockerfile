FROM python:3.10 AS build

ENV DASH_DEBUG_MODE True
WORKDIR /app
COPY ./app/requirements.txt /app/
RUN set -ex && \
    pip install -r requirements.txt

FROM build

COPY ./app /app

EXPOSE 4000
EXPOSE 4001
EXPOSE 4002

CMD ["python", "work-on-dash-view/main.py"]
# CMD ["python", "work-on-dash-view/responsive-sidebar/sidebar.py"]
# CMD ["python", "work-on-dash-view/sidebar-with-icons/app.py"]
