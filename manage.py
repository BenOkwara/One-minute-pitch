from app import create_app
from app import flask_script import Manager,Server


# Creat app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()
