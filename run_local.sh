set -e

export FLASK_APP='app.py'
export FLASK_ENV='development'
flask run &
python window.py