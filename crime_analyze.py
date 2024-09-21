'''This file reads a crime dataset based on LAPD.
It produces summary statistics and a data visualization'''

from zipfile import ZipFile
import polars as pl
import matplotlib.pyplot as plt
from IPython.display import display

ZIP_FILE = "Crime_Data_from_2020_to_Present.csv.zip"

df = pl.read_csv(
    ZipFile(ZIP_FILE).read("Crime_Data_from_2020_to_Present.csv")
)

# Convert the time occurred column to accurate hour of the day 
    # with decimal representing accurate minute proportion of the hour
df = df.with_columns((pl.col("TIME OCC")//100 + df['TIME OCC']%100/60).alias("TimeOccHr"))

## Show summary statistics of the dataframe.
display(df.describe())

# Distribution of Crome Occcurence over Time of Occurence
plt.figure(figsize = (15,6))
plt.hist(df['TimeOccHr'], bins = 24)
plt.xlabel("Hour of Day")
plt.ylabel("Crime Occurences")
plt.title("Distribution of Crime Occurences over Time of Day")
plt.xticks(ticks = [2*i for i in range(13)])
plt.show()
