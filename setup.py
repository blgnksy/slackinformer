from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["slackclient"]

setup(
    name="slackinformer",
    version="0.0.1",
    author="Fatih Baltacı",
    author_email="baltacifatih14@gmail.com",
    description="Informs Slack for sth.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/blgnksy/slackinformer/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
