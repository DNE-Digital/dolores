import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dolores",
    version="1.0.3",
    author="Phil Mohun, Malcolm Navarro, DNE LLC",
    author_email="dolores@philmohun.com",
    description="Dolores is a Python library for developers using GPT-3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dne-digital/dolores",
    download_url="https://pypi.org/project/dolores/",
    packages=setuptools.find_packages(),
    package_dir = {'dolores': 'dolores'},
    package_data = {'dolores': ['dolores/*.json']},
    #data_files = [('dolores', 'packages/prompts.json')],
    classifiers=[
        "Programming Language :: Python :: 3",
    	"License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
