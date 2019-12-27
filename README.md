# multimetric

![Build status](https://github.com/priv-kweihmann/tlv/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/multimetric.svg)](https://badge.fury.io/py/multimetric)
[![Python version](https://img.shields.io/pypi/pyversions/multimetric)](https://img.shields.io/pypi/pyversions/multimetric)
[![Downloads](https://img.shields.io/pypi/dm/multimetric)](https://img.shields.io/pypi/dm/multimetric)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/priv-kweihmann/multimetric.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/priv-kweihmann/multimetric/context:python)

Calculate code metrics in various languages

## Purpose

This tool tries to calculate the following metrics for many, many programming languages

* Comment to Code percentage
* Cyclomatic complexity according to McCabe
* Number of delivered bugs according to Halstead
* Time required to program according to Halstead
* Difficulty according to Halstead
* Volume according to Halstead
* Effort according to Halstead
* Lines of code
* Maintainability index

This tool was heavily inspired by [metrics](https://github.com/markfink/metrics)

## Requirements

* python3
* [Pygments](http://pygments.org/)

## Installation

### PyPi

simply run

```sh
pip3 install multimetric
```

### From source

* Install the needed requirements by running ```pip3 install pygments```
* git clone this repository
* cd to \<clone folder\>
* run `python3 setup.py build`

## Usage

```shell
usage: multimetric [-h] [--bugpredict {old,new}]
                   [--maintindex {sei,classic,microsoft}]
                   files [files ...]

Calculate code metrics in various languages

positional arguments:
  files                 Files to parse

optional arguments:
  -h, --help            show this help message and exit
  --bugpredict {old,new}
                        Method how to calculate the bug prediction
  --maintindex {sei,classic,microsoft}
                        Method how to calculate the maintainability index
```

By default tool guesses the content type by the filename, if that doesn't work for you please see below

## Output

Output will be written to stdout as json.

### Output structure

* `files` contains a list of each file passed by CLI
* `overall` contains the calculated values for all passed files
* `stats` contains the statistically calculated values over all files passed [see Statistical additions](#statistics)

#### Item structure

* `comment_ratio` = Comment to Code percentage
* `cyclomatic_complexity` = Cyclomatic complexity according to McCabe
* `halstead_bugprop` = Number of delivered bugs according to Halstead
* `halstead_timerequired` = Time required to program according to Halstead
* `halstead_difficulty` = Difficulty according to Halstead
* `halstead_volume` = Volume according to Halstead
* `halstead_effort` = Effort according to Halstead
* `lang` = list of idendified programming languages
* `loc` = Lines of code
* `maintainability_index` = Maintainability index
* `operands_sum` = Number of used operands
* `operands_uniq` = Number of unique used operands
* `operators_sum` = Number of used operators
* `operators_uniq` = Number of unique used operators

#### Statistics

The item `stats` contains in addition to the above mentioned the following items, which by themselves contain all the items mentioned at [Item structure](#item-structure)

* `max` = the maximum value of all items of the metric
* `mean` = statistical mean over all items of the metric
* `median` = statistical median over all items of the metric
* `min` = the minimum value of all items of the metric
* `sd` = standard deviation over all items of the metric

## Further reading

* [Pygments](http://pygments.org/)

## Bugs & Contribution

Feel free to create issues or pull requests
