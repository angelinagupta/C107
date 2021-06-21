import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    size = []
    time = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row["Size of TV"]))
            time.append(float(row["time"]))
    return{"x" : size, "y" : time}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between size of TV vs Average time spent watching TV in a week is: ", corelation[0,1])

def main():
    data_path = "D:\code\python\TV.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

main()