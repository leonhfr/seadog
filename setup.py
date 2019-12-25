import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seadog",
    version="0.1.2",
    author="leonhfr",
    author_email="hello@leonh.fr",
    description="Statistical data visualization from the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonhfr/seadog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.7',
)