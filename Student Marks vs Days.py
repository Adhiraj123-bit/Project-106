import csv
import numpy as np


def getDataSource(data_path):
    marks_in_precentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))


    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrceof(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,11])

def setup():
    data_path = "./data/student Marks vs Days Present.cvs"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

    setup()