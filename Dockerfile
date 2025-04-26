FROM odoo:18

WORKDIR /poc
COPY . .

USER root
RUN apt update && \
    apt install -y  pkg-config libcairo-dev && \
    pip install  --break-system-packages rlPyCairo
USER odoo

EXPOSE 8069
ENTRYPOINT ["odoo"]
