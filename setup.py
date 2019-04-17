import os
from typing import Mapping, Sequence

from setuptools import setup


def find_stubs(package: str) -> Mapping[str, Sequence[str]]:
    stubs = [
        os.path.join(root, file).replace(package + os.sep, '', 1)
        for root, dirs, files in os.walk(package)
        for file in files
    ]
    return {package: stubs}


requirements = [
    'cytoolz==0.9.0.1',
]

dev_requirements = [
    'bumpversion==0.5.3',
    'twine==1.13.0',
]

test_requirements = [
    'flake8==3.7.7',
]

version = '0.0.1'

setup(
    name='cytoolz-stubs',
    version=version,
    license='MIT',
    description='PEP 561 type stubs for cytoolz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/blindspot-ai/cytoolz-stubs',
    maintainer='Martin Matyasek',
    maintainer_email='martin.matyasek@blindspot.ai',
    keywords='cytoolz stubs',
    packages=['cytoolz-stubs'],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=requirements,
    extras_require={'dev': dev_requirements, 'test': test_requirements},
    tests_require=requirements + test_requirements,
    package_data=find_stubs('cytoolz-stubs'),
)
