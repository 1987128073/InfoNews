from flask_migrate import MigrateCommand
from flask_script import Manager
from info import create_app

# 创建web应用
app = create_app()
# 创建脚本管理
mgr = Manager(app)
# 使用管理器生成迁移命令
mgr.add_command("mc", MigrateCommand)


if __name__ == '__main__':
    app.run(debug=True)
