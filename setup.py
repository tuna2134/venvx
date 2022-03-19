import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()
  
packages = []

setuptools.setup(
    entry_points={
        "console_scripts": [
            "venvx = shell:main"
        ]
    },
    project_urls = {
        "Documentation": "https://tuna2134.github.io/venvx/"
    },
    extras_require=extras,
    packages=packages,
    name="venvx",
    version="0.0.1",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="venv wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuna2134/venvx",
    install_requires=_requires_from_file('rqs.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
