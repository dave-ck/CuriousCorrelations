def splice():
    f = open("indexpt1.txt", "r")
    firsthtml = f.read()
    f.close()
    f = open("indexpt2.txt", "r")
    secondhtml = f.read()
    f.close()
    f = open("basic-scatter-plot.html", "r")
    graphhtml = f.read()
    f.close()


    htmlstring = firsthtml + graphhtml + secondhtml
    f = open("indextest.html", "w")
    f.write(htmlstring)
    f.close()
