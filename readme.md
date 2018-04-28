### blog.robot
blog robot and facade

#### install dependencies
pip3 install

#### start dev
python3 manage.py runserver 0.0.0.0:8080 --settings=app.settings.dev

#### deploy prod
settings=app.settings.prod

#### migrate
python3 manage.py migrate

#### update model
python3 manage.py makemigrations robot

#### create model
python3 manage.py migrate robot
