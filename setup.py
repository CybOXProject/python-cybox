from setuptools import setup, find_packages

setup(
    name="cybox",
    version="1.0a2",
    author="CybOX Project",
    author_email="cybox@mitre.org",
    description="An API for parsing and generating CybOX content.",
    url="http://cybox.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3'],
)
