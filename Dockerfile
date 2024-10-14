FROM odoo:18

WORKDIR  /opt/odoo/factory
COPY . .
EXPOSE 8069

ENTRYPOINT odoo -c prod-env.conf -i factory \
            --db_host=$DB_HOST \
            --db_port=$DB_PORT \
            --db_user=$DB_USER \
            --db_password=$DB_PASSWORD
