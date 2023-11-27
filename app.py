from flask import Flask,session,g
from models import EmailCaptchaModel
import config
from exts import db,mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate #migrate可以迁移新增字段，但是db.createall不行


app = Flask(__name__)
#绑定配置文件
app.config.from_object(config)

db.init_app(app)#先创建，后绑定
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

#bLueprint:用来做模块化的
#电影、读书、音乐、xxx

# 用户发出请求后,先用一个对象存储用户的user_id，然后再去执行视图函数
# flask db init:只需要执行一次
# flask db migrate:将orm模型生成迁移脚本
# flask db upgrade:将迁移脚本映射到数据库中


@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        #g是全局的意思
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)

@app.context_processor
#上下文处理器的概念：上下文处理器将所有的变量都存储在上下文当中，
#当其他模板需要渲染变量的时候就直接使用上下文处理器中的变量，
#而不需要重新去一个一个去获取
def my_context_processor():
    return {"user":g.user}

if __name__ =='__main__':
    app.run()   