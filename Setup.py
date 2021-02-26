from setuptools import setup
from setuptools import find_packages
import re
from os.path import abspath, dirname, join

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, "src", "Libdoc2TestBench", "__init__.py"), encoding="utf-8") as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)

setup(
    name="robotframework-libdoc2testbench",
    version=VERSION,
    author="imbus AG",
    author_email="maximilian.birkenhagen@imbus.de",
    description="Tool to create TestBench imports.",
    url="https://www.imbus.de",
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    install_requires=["robotframework > 3.2.2"],
    python_requires=">=3.7",
)
