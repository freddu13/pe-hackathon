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

# %% scrolled=true
df = pd.read_csv('PS_2023.10.31_06.09.13.csv', sep = ',', header = 96)
df.info()

# %%
df1 = pd.read_csv('PS_2023.10.31_06.09.13.csv', sep = ':',header = 2, nrows = 92,names = [''])

# %%
df1

# %%
df.columns = df1['']

# %%
df.columns = df.columns.str.lstrip()

# %%
df

# %%
dfdate = pd.to_datetime(df['Date of Last Update'])
df['Date of Last Update'] = dfdate
df

# %%
df.sort_values('Date of Last Update')

# %% scrolled=true

# %%
df = df.drop_duplicates (subset = 'Planet Name', keep = 'last')

# %%

# %% scrolled=true

# %%
df.columns

# %%
df2 = df[['Planet Name', 'Distance [pc]','Discovery Year','Stellar Effective Temperature [K]','Equilibrium Temperature [K]','Insolation Flux [Earth Flux]']]

# %%
df2

# %%
df2 = df2[~df2['Distance [pc]'].isna()]
df2 = df2.sort_values(['Distance [pc]'])
df2 = df2.reset_index(drop = True)
df2['x'] = df2.index
df2

# %%

# %%
df2.plot(kind='scatter', x='Discovery Year', y='Distance [pc]')

# %%
df3 = df2[~df2['Stellar Effective Temperature [K]'].isna()]
df3

# %%
df3.plot(kind='scatter', x='Distance [pc]', y='Stellar Effective Temperature [K]', xlim=(0,2500), ylim = (0,12000))

# %%
df4 = df2[~df2['Equilibrium Temperature [K]'].isna()]
df4

# %%
df4.plot(kind='scatter', y='Insolation Flux [Earth Flux]', x='Equilibrium Temperature [K]', xlim = (0,3000), ylim = (0,2000))

# %%
