#!/bin/bash

# activate the env 
source env/bin/activate

# Run Odoo with auto-reload enabled
/opt/odoo18/odoo-bin \
  -c local-env.conf \
  -u ev_website \
  --dev=all
