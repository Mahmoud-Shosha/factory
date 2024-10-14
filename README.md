
# Factory Management  
  
An Odoo project that provides features for managing factories.  
Odoo version used: Odoo18.
  
## Run from docker  
- This is used to run the project for demonstration, testing, production purposes  
- Steps  
	1. Make sure you have docker installed
	2. Prepare the database (Get its host, port, username, password)
	3. Clone the repository
	```git clone https://www.github.com/Mahmoud-Shosha/factory .```
	4. Build the docker image ```docker build -t odoo-factory .```
	5. Run the docker container
		(Replace the host, port, username, password with yours)
		```bash
		docker run  --name odoo-factory-0  --network docker_default  
		            -p 8069:8069  -p 8071:8071  -p 8072:8072  
		            -e DB_HOST=postgres  -e DB_PORT=5432 -e DB_USER=odoo  -e DB_PASSWORD=odoo   	   
		            odoo-factory
	6. Validate that Odoo runs through http://localhost:8069
  
## Run from sourcecode  (Ubuntu)
- This is used to run the project for development purposes  
- Steps  
	1. Install the system dependencies (Python3, pip, venv, ...)
	```sudo apt update && sudo apt upgrade```
	```sudo apt install python3-dev python3-pip python3-wheel python3-venv build-essential libpq-dev libxslt-dev libxml2-dev  libzip-dev libldap2-dev libsasl2-dev libssl-dev ```
	2. Support right-to-left languages like Arabic
	```sudo apt install nodejs npm```
	```sudo npm install -g rtlcss```
	3. Download Odoo sourcecode
	```git clone https://www.github.com/odoo/odoo --branch 18.0 --depth 1 /opt/odoo18```
	4. Clone the repository
	```git clone https://www.github.com/Mahmoud-Shosha/factory .```
	5. Change configurations (host, port, username, password) in ```local-env.conf``` file
	6. Install Python dependencies
	```virtualenv -p python3 env```
	```source env/bin/activate```
	```pip install -r /opt/odoo16/requirements.txt```
	```pip install /opt/odoo17```
	7. Run Odoo server
	```opt/odoo16/odoo-bin -c local-env.conf -i base```
	8. Validate that Odoo runs through http://localhost:8069