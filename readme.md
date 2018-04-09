## blog.robot
blog robot

### start dev
python3 manage.py runserver 0.0.0.0:8080 --settings=app.settings.dev

### deploy prod
settings=app.settings.prod

### 创建表结构
python3 manage.py migrate

### 模型有变更
python3 manage.py makemigrations robot

### 创建表结构
python3 manage.py migrate robot
