1. 安装所需库，这个库比较特殊，其他库自行安装解决
``pip install flask-migrate``

2. 迁移三部曲(用来迁移数据库)

``flask db init ``

``flask db migrate``

``flask db upgrade``

最后会生成一个migrations文件,并且数据库中会多两张表

修改html路径，

发送验证码：
1. 安装flask库:
    ``pip install flask-mail``    


