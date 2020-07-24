import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calvin",
    version="0.0.1",
    author="Phil Mohun, Malcolm Navarro, DNE LLC",
    author_email="calvin@philmohun.com",
    description="Calvin is a Python library for developers using GPT-3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pmohun/calvin",
    download_url="https://github.com/pmohun/calvin/archive/v0.1.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    	"License :: OSI Approved :: BSD 3-Clause "New" or "Revised" License (BSD-3-Clause)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
