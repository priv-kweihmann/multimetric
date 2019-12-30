import subprocess
import setuptools

_long_description = "See https://github.com/priv-kweihmann/multimetric for documentation"
_long_description_content_type = "text/plain"
try:
    with open("README.md") as i:
        _long_description = i.read()
        _long_description_content_type = "text/markdown"
except Exception:
    pass

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="multimetric",
    version="1.1.0",
    author="Konrad Weihmann",
    author_email="kweihmann@outlook.com",
    description="Calculate code metrics in various languages",
    long_description=_long_description,
    long_description_content_type=_long_description_content_type,
    url="https://github.com/priv-kweihmann/multimetric",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    scripts=['bin/multimetric'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
