@REM Launch RPA client
SET RPA_LOGLEVEL=INFO
pipenv run python3 rpa.py --ini-file rpa.ini --profile RPA_std
