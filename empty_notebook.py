# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# %% [markdown]
# # un notebook vierge
#
# sauvé en Python

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% scrolled=true
# cat PS_2023.10.31_06.09.13.csv

# %% scrolled=true
df = pd.read_csv('PS_2023.10.31_06.09.13.csv', sep = ',', header = 96)
df

# %%
df1 = pd.read_csv('PS_2023.10.31_06.09.13.csv', sep = ':',header = 2, nrows = 92,names = [''])

# %%
df1

# %%
df.columns = df1['']

# %%
df

# %%
