from setuptools import setup, find_packages

setup(
    name="cybox",
    version="1.0.0b1",
    author="CybOX Project, MITRE Corporation",
    author_email="cybox@mitre.org",
    description="A Python library for parsing and generating CybOX content.",
    url="http://cybox.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3', 'python-dateutil'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
