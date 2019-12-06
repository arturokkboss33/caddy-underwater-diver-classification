#!/usr/bin/env python3

import pandas as pd
import numpy as np
import pickle

#fn = '../model-F/test-df-model-F.pkl'
#
#with (open(fn, "rb")) as openfile:
#	files_dict = pickle.load(openfile)
#
#print(files_dict)

fn = '../model-F/test-df-model-F.csv'

df = pd.read_csv(fn)

print(df.columns)
print(df)

print(len(df['backwards'].index))
