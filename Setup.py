import re
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, "src", "Libdoc2TestBench", "__init__.py"), encoding="utf-8") as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="robotframework-libdoc2testbench",
    version=VERSION,
    author="imbus AG | Maximilian Birkenhagen",
    author_email="maximilian.birkenhagen@imbus.de",
    description="Robot Framework Libdoc Extension that generates imbus TestBench Library import formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imbus/robotframework-libdoc2testbench",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        'console_scripts': [
            'Libdoc2TestBench = Libdoc2TestBench.__main__:main',
            'libdoc2testbench = Libdoc2TestBench.__main__:main',
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    install_requires=["robotframework >= 4.0.0"],
    extras_require={'dev': ['isort', 'mypy', 'pylint', 'black']},
    python_requires=">=3.7",
)
