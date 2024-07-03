@REM Launch RPA client
SET RPA_LOGLEVEL=INFO
C:\Users\Torsten\Documents\GitHub\rpa
pipenv run python rpa.py --ini-file rpa.ini --profile RPA_auto
shutdown -s

