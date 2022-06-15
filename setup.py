from setuptools import *

classiflers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Linux',
    'Programming Language :: Python :: 3'
]

setup(
    name='badpy',
    version='1.3',
    description='Python package for hacking. (This package including hacking modules.)',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='TheSadError',
    author_email='syntaxerrorses@gmail.com',
    license='MIT',
    classiflers=classiflers,
    keywords='hack,package,python package for hacking,pythonda hack paketleri,pentest library,pentesting,TheSadError',
    packages=find_packages(),
    install_requires=['requests','colorama','sockets']
)