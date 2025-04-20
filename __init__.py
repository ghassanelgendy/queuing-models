"""
Queuing Theory Models Package

This package provides implementations of various queuing theory models.
"""

# Import all models
from queue import QueueModel
from mm1 import MM1
from mm1k import MM1K
from mm1m import MM1m
from mmk import MMk
from mminf import MMInf

# Define what's available when using "from package import *"
__all__ = ['QueueModel', 'MM1', 'MM1K', 'MM1m', 'MMk', 'MMInf']

# Package metadata
__version__ = '1.0.0'
__author__ = 'Queuing Models Team' 