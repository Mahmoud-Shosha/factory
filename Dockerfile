FROM odoo:18

USER root
RUN apt update && \
    apt install -y  pkg-config libcairo-dev lsof cron && \
    pip install  --break-system-packages rlPyCairo schedule

#RUN (crontab -l -u root 2>/dev/null; echo "* * * * * python3 /ev-odoo/license/main.py") | crontab -u root -

WORKDIR /ev-odoo

COPY custom-addons custom-addons
COPY license license
COPY entrypoint.sh .
COPY run-profiles/dev-ubuntu/env.conf .
COPY run-profiles/local-windows/env.conf .

RUN chmod +x /ev-odoo/entrypoint.sh

EXPOSE 8069

ENTRYPOINT ["/ev-odoo/entrypoint.sh"]

USER odoo