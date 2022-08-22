@REM Launch RPA client
SET RPA_LOGLEVEL=INFO
cd C:\Users\torst\Abiaz\rpa
pipenv run python rpa.py --ini-file rpa.ini --profile RPA_auto
shutdown -s

