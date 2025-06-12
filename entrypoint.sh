#!/bin/bash
echo "Running entrypoint.sh ..."

python3 ./license/main.py
exit_code=$?
if [ $exit_code -ne 0 ]; then
    exit $exit_code
fi

python3 ./license/job.py &

exec odoo "$@"






