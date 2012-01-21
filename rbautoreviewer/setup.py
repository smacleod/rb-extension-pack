from setuptools import setup, find_packages

PACKAGE="rbautoreviewer"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Auto Reviewer extension for reviewboard""",
    author="Steven MacLeod",
    packages=["rbautoreviewer"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbautoreviewer.extension:AutoReviewerExtension' % PACKAGE,
    },
    package_data={
        'rbautoreviewer': [
            'templates/rbcia/*.html',
        ],
    }
)
