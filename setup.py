from os.path import abspath
from os.path import dirname
from os.path import join

from setuptools import setup

here = dirname(abspath(__file__))
requirements = list(open(join(here, "requirements.txt")).readlines())

console_scripts = [
    "init_dashboard_db = api.db_conn:init_db",
]
setup(
    name="test_package",  # add the desired package name
    author="Kartik",
    version="1.0.0",
    python_requires=">=3.10",
    install_requires=requirements,
    packages=["api"],
    entry_points={"console_scripts": console_scripts},
)
