import sys
import os
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('ENV_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)
    sys.exit(len(test_result.failures))


@manager.command
def run_am_i_alive(param_1, param_2):
    """ python application.py run_am_i_alive 123 11 """
    """ just runs a command to verify this application is runnable """
    print("I am alive! param_1:{} param_2:{}".format(param_1, param_2))
    sys.exit(0)

if __name__ == '__main__':
    # import profile
    # profile.run('manager.run()')
    manager.run()
