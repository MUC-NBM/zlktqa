from flask import Flask

import config
from exts import db,mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate #migrate可以迁移新增字段，但是db.createall不行


app = Flask(__name__)
#绑定配置文件-
app.config.from_object(config)

db.init_app(app)#先创建，后绑定
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

#bLueprint:用来做模块化的
#电影、读书、音乐、xxx
if __name__ =='__main__':
    app.run()