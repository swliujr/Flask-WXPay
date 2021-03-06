#!/usr/bin/env python
import re

from setuptools import find_packages, setup

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()


with open('flask_wxpay/__init__.py', 'r', encoding='utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='Flask-WXPay',
    version=version,
    description='Flask Extension for WeChat Pay.',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/Flask-WXPay',
    license='MIT',
    install_requires=['requests', 'defusedxml'],
    packages=find_packages(),
)
