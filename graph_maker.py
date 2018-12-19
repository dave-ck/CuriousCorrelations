import Data_Graph_and_Unzip
import Histogram
import jsonReader


def graph(varx, vary):
    data = jsonReader.getDataCollection(varx, vary)
    discrete = jsonReader.discrete(varx)
    if discrete:
        print("Attempting to graph a boxplot.")
        # make data into a dictionary
        dictionary = {}
        for i in data:
            if i[0] in dictionary:
                # update entry i to include i[1]
                dictionary[i[0]].append(i[1])
            else:
                dictionary[i[0]] = [i[1]]
        return Histogram.plottingBox(dictionary)
    else:
        return Data_Graph_and_Unzip.fin_func(varx, vary)


def pp(dictionary):
    print("Data:")
    print(dictionary)
    for i in dictionary:
        print(i, ":", dictionary[i])

