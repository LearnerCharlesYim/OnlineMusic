# _*_ codding:utf-8 _*_
from app import create_app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import render_template
from werkzeug.security import generate_password_hash
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#创建管理员
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
def create_admin(username,password):
    user = User(username=username,
                pwd = generate_password_hash(password),# 对密码加密
                flag=1
                )
    db.session.add(user)
    db.session.commit()
    print(f'管理员{user.username}添加成功！')


@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    return render_template("home/404.html"), 404

if __name__ == '__main__':
    manager.run()
