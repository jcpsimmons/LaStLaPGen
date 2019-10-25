from constructors.htmlObj import HTMLObject
from constructors import htmlSnippets
from datetime import datetime
from bs4 import BeautifulSoup


def locationParse(strLocation):
    # Turns raw string input (CSV) into array for location of object in 2D array
    insertLocation = strLocation.split(",")
    insertLocation = list(map(lambda x: int(x)-1, insertLocation))
    return(insertLocation)


def mappingSequence():
    # Creates HTMLObjects in a 2D array - each row has nested columns
    vdom = []
    hasVideo = False
    rows = int(input('How many rows? '))
    for row in range(rows):
        colList = []
        cols = int(input('How many columns in row {}? '.format(str(row+1))))
        for col in range(cols):
            colList.append(HTMLObject(row + 1, col + 1))
        vdom.append(colList)

    # IMAGES
    numImages = int(input('How many cells contain images (0 for none)? '))
    if numImages > 0:
        for i in range(numImages):
            insertLocation = input(
                'What is the location for image {} in row/col format, e.g. 1,3? '.format(str(i+1)))
            insertLocation = locationParse(insertLocation)
            altText = input('Enter alt text for this image: ')
            vdom[insertLocation[0]][insertLocation[1]].setImage(altText)

    # VIDEO
    isVideo = int(input('Is there a video (1 yes, 0 no)? '))
    if isVideo:
        insertLocation = input(
            'What is the location of the video in row/col format, e.g. 1,3? ')
        insertLocation = locationParse(insertLocation)
        altText = input('Enter alt text for the thumbnail image: ')
        link = input('Enter embed link for the YT video: ')
        vdom[insertLocation[0]][insertLocation[1]].videoTrue(altText)

    # Assemble HTML
    finalHTML = ""
    for row in range(len(vdom)):
        columnCode = ""
        for col in range(len(vdom[row])):
            columnCode = columnCode + \
                vdom[row][col].renderComponent()
        rowCode = "<div class='container {}'>{}</div>".format(
            "row{}".format(str(row+1)), columnCode)
        finalHTML = finalHTML + rowCode

    if hasVideo:
        finalHTML = finalHTML + htmlSnippets.videoModal
    finalHTML = htmlSnippets.css + "<div class='x'>" + finalHTML + "</div>"
    return(finalHTML)


vdom = mappingSequence()
# prettify the HTML
vdom = BeautifulSoup(vdom)
vdom = vdom.prettify()

try:
    with open('x.html', 'w') as file:
        file.write(vdom)
    print("Saved file as x.html")
except Exception as e:
    print(e)
