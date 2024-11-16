FROM odoo:18

WORKDIR  /opt/odoo/factory
COPY . .
USER root
RUN apt update
RUN apt install -y  pkg-config libcairo-dev
RUN pip install  --break-system-packages rlPyCairo
# USER non-root-user
EXPOSE 8069


# Override the ENTRYPOINT to include the correct parameters
# ENTRYPOINT ["odoo"]
# # Set environment variables for the database connection
# ENV DB_HOST=${DB_HOST}
# ENV HOST=${HOST}
# ENV DB_PORT=${DB_PORT}
# ENV DB_USER=${DB_USER}
# ENV DB_PASSWORD=${DB_PASSWORD}
# ENV PORT=${PORT}


# ENV PORT=${PORT}
# Override the ENTRYPOINT from the base image
# ENTRYPOINT ["-c", "prod-env.conf", "-i", "factory"]
# ENTRYPOINT ["sh", "-c", "odoo -c local-env.conf -i factory "]


# Use CMD to pass database connection parameters
# CMD ["--db_host=${DB_HOST}", "--db_port=${DB_PORT}", "--db_user=${DB_USER}", "--db_password=${DB_PASSWORD}"]

# sudo  docker login --username AWS -p $(aws ecr get-login-password --region us-east-1)  https://023481417683.dkr.ecr.us-east-1.amazonaws.com
# sudo docker build -t odoo-factory .
# sudo docker tag odoo-factory:latest 023481417683.dkr.ecr.us-east-1.amazonaws.com/odoo-factory:latest
# sudo docker push 023481417683.dkr.ecr.us-east-1.amazonaws.com/odoo-factory:latest
# sudo docker run --name odoo-factory-0 --network docker_default -p 8069:8069 -p 8071:8071 -p 8072:8072   -e DB_HOST=postgres   -e DB_PORT=5432   -e DB_USER=odoo   -e DB_PASSWORD=odoo   odoo-factory

# Some system dependencies
# sudo apt-get install pkg-config
#  sudo apt-get install libcairo-dev
# pip install rlPyCairo

