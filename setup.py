# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import setuptools

_long_description = "See https://github.com/priv-kweihmann/multimetric for documentation"

with open('README.md') as f:
    _long_description = f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="multimetric",
    version="2.0.2",
    author="Konrad Weihmann",
    author_email="kweihmann@outlook.com",
    description="Calculate code metrics in various languages",
    long_description=_long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/priv-kweihmann/multimetric",
    packages=setuptools.find_packages(exclude='tests',),
    install_requires=requirements,
        entry_points={
        "console_scripts": [
            "multimetric = multimetric.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: zlib/libpng License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires='>=3.10',
)
