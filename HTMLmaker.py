def splice(graphhtml):
    f = open("indexpt1.txt", "r")
    firsthtml = f.read()
    f.close()
    f = open("indexpt2.txt", "r")
    secondhtml = f.read()
    f.close()
    graphhtml = graphhtml.split("<body>")
    graphhtml = graphhtml[1]
    graphhtml = graphhtml.split("</body>")
    graphhtml = graphhtml[0]

    htmlstring = firsthtml + graphhtml + secondhtml
    return htmlstring