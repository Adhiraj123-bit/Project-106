import numpy.express as px
import csv

with open("./data/cups of coffee vs hours of sleep.csv") as csv_file:
    df = cvs.Dictreader(cvs_file)
    fig = px.scatter(df,x="Coffe in ml", y="sleep in hours", color="week")
    fig.show()