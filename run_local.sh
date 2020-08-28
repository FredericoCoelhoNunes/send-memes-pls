set -e

export FLASK_APP='app.py'
export FLASK_ENV='development'
export FLASK_SECRET_KEY='test'
flask run &
python window.py