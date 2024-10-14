FROM odoo:18

WORKDIR  /opt/odoo/factory
COPY . .
EXPOSE 8069

ENTRYPOINT odoo -c prod-env.conf -i factory \
            --db_host=$DB_HOST \
            --db_port=$DB_PORT \
            --db_user=$DB_USER \
            --db_password=$DB_PASSWORD

# To run a container
# $ sudo docker run --name odoo-factory-0 --network docker_default -p 8069:8069 -p 8071:8071 -p 8072:8072 \
#   -e DB_HOST=postgres \
#   -e DB_PORT=5432 \
#   -e DB_USER=expertsvision \
#   -e DB_PASSWORD=0D5thNlqR7SNJ1ZwM9De \
#   odoo-factory
