# %%
import pandas as pd
import altair as alt
import numpy as np

# %%
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat = pd.read_csv(url, encoding = "latin1", encoding_errors = "ignore", header=0)


# %%
dat.head()
# %%

# %%
