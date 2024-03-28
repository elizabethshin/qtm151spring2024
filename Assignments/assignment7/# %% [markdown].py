# %% [markdown]
# # Assignment 7

# %% [markdown]
# ## Submit as an HTML file

# %% [markdown]
# <font size = "5">
# Print your name below

# %%
print('Elizabeth Shin')

# %% [markdown]
# <font size = "5">
# 
# Import the "pandas" and "numpy" library

# %%
# Write your answer here:

import pandas as pd
import numpy as np

# %% [markdown]
# <font size = "5">
# 
# (a) Replace values from intervals
# 
# <font size = "3">
# 
# - Import the dataset "data_raw/students.csv" to a new object "students"
# - Use "pd.cut()" to assign the column "numericgrade" to a letter grade <br>
# 
# - Using the following grading scale: <br>
# 
# <img src="figures/grading_scale.png" alt="drawing" width="600"/>
# 

# %%
students = pd.read_csv("data_raw/students.csv")

bins = [0, 55, 60, 65, 70, 75, 80, 83, 87, 93, 100]
labels = ["F", "D", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]

students["lettergrade"] = pd.cut(students["numericgrade"],
                                bins = bins,
                                right = True,
                                labels = labels)


# %% [markdown]
# <font size = "5">
# 
# For questions (b)-(e) use "results.csv", <br>
# a dataset on competitive car racing
# 
# Import the dataset "data_raw/results.csv" to <br>
#  a new object "results"

# %%
# Write your own code

results = pd.read_csv("data_raw/results.csv")

# %% [markdown]
# <font size = "5">
# 
# (b) Check column types
# 
# <font size = "3">
# 
# - View the dataset
# - Use the function "results.dtypes" to get the column types
# - Search for the "results" table in "codebook/f1_codebook.pdf".
# - Does the type of the "time" column agree with the codebook? <br>
# i.e. is it an integer, float, or string/object?
# 
# 
# HINT: See Lectures 12 and 14 for how to interpret the codebook
# 

# %%
# Write your own code here
# Note: When you run "results.dtypes" you will get the type (int, float, object)
# Object represents columns coded as strings.

results
results.dtypes

#The time column is an object and the time column agrees with the codebook because in the codebook, it is listed as varchar(255) 
#which means that there is a maximum of 255 characters. The object contains many string values, and string values include text. 


# %% [markdown]
# <font size = "5">
# 
# (c) Clean a column
# 
# <font size = "3">
# 
# - Import the dataset "data_raw/results.csv" to a new object "results"
# - Our goal is to replace any string values in the column "milliseconds" <br>
# to missing values (NaNs) and covert to numeric
# - To do so
#     - "Extract list of non-numeric values"
#     - "Replace certain values"
#     - "Convert column to numeric"
#     - "Display"
#  
# 

# %%
# Write your own code here

results = pd.read_csv("data_raw/results.csv")

results["milliseconds"].str.isnumeric()

subset = results.query("milliseconds.str.isnumeric() == False")
list_unique = pd.unique(subset["milliseconds"])
print(list_unique)

list_old = ['\\N']
list_new = [np.nan]

results["milliseconds"] = results["milliseconds"].replace(list_old, list_new)

results["milliseconds_numeric"] = pd.to_numeric(results["milliseconds"])
print(results["milliseconds_numeric"])


# %% [markdown]
# <font size = "5">
# 
# (d) Groupby + Aggregate
# 
# <font size = "3">
# 
# - Compute the mean and standard deviation of "laps", <br>
# grouping by "constructorId". Store the new dataset <br>
# as "df_aggCon_pos"
# - Sort the aggregate dataset in decending <br>
# order of mean laps using ".sort_values()"
# 
# 

# %%
# Write your own code

df_aggCon_pos = (results.groupby("constructorId").agg(mean_laps = ('laps', 'mean'),
                                                      sd_laps = ('laps','std')))
df_aggCon_pos

constructor_agg = (results.groupby("constructorId")
                   .agg(mean_laps = ("laps", "mean"))
                   .sort_values(by = "mean_laps", ascending = False))
constructor_agg

# %% [markdown]
# <font size = "5" >
# 
# (e) Query + Groupby + Aggregate
# 
# <font size = "3">
# 
# - Use ".query()" to subset observations with <br>
# 'race_id >= 150'
# - Compute the mean and standard deviation of "position", <br>
# grouping by "constructorId". Store the new dataset <br>
# as "df_subAggCon_pos"
# 

# %%
# Write your own code

df_subAggCon_pos = (results.query("raceId >= 150")
                         .groupby(["raceId", "constructorId"])
                         .agg(mean_laps = ('laps', 'mean'),
                              sd_position = ('laps', 'std')))

df_subAggCon_pos



