#!/usr/bin/env python
"""Provides statistical tests and distributions.

Also provides NumberList and FrequencyDistribution, two classes for
working with statistical data.
"""
from .distribution import chi_high as chisqprob


__all__ = [
    "chisqprob",
    "contingency",
    "distribution",
    "information_criteria",
    "kendall",
    "ks",
    "special",
    "test",
]


__author__ = ""
__copyright__ = "Copyright 2007-2020, The Cogent Project"
__credits__ = [
    "Gavin Huttley",
    "Rob Knight",
    "Sandra Smit",
    "Catherine Lozupone",
    "Micah Hamady",
]
__license__ = "BSD-3"
__version__ = "2020.7.2a"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"
