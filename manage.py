
import unittest
import coverage
import sys
from project import create_app
import time
from flask.cli import FlaskGroup
import xmlrunner
COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()
app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def test():
    """Runs test without scode coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = xmlrunner.XMLTestRunner(output='test-reports').run(tests)
    if result.wasSuccessful():
        return sys.exit(0)
    return sys.exit(1)


@cli.command()
def cov():
    """Checks coverage of unit tests."""
    tests = unittest.TestLoader().discover('project/tests')
    result = xmlrunner.XMLTestRunner(output='test-reports').run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return sys.exit(0)
    return sys.exit(1)


if __name__ == "__main__":
    cli()
