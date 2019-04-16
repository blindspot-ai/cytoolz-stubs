import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


requirements = [
    'cytoolz==0.9.0.1',
]

test_requirements = [
    'flake8==3.7.7',
]

setup(
    name='cytoolz-stubs',
    maintainer="Martin Matyasek",
    maintainer_email="martin.matyasek@blindspot.ai",
    description="PEP 561 type stubs for cytoolz",
    url="https://github.com/blindspot-ai/cytoolz-stubs",
    license='MIT',
    version="0.0.1",
    packages=['cytoolz-stubs'],
    zip_safe=False,
    install_requires=requirements,
    extras_require={'test': test_requirements},
    tests_require=requirements + test_requirements,
    package_data=find_stubs('cytoolz-stubs'),
)
