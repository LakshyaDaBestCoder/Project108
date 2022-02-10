import plotly.figure_factory as pff
import pandas as pd

df = pd.read_csv("data.csv")
fig = pff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=False)
fig.show()