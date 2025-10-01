import sys
assert sys.version_info >= (3, 7)
from packaging import version
import sklearn
assert version.parse(sklearn.__version__) >= version.parse("1.0.1")
import pandas as pd
from pathlib import Path
import numpy as np

# importing of the data
datafile = "data/50_Startups.csv"
dataset = pd.read_csv(datafile)