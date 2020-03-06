import pandas as pd
import requests
import json
import re
import itertools
import time

df_festival = pd.read_csv('./data/festivals.csv', keep_default_na=False)
df_festival