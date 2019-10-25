from datetime import datetime


class HTMLObject:
    def __init__(self):
        self.type = ''
        self.column = 0
        self.row = 0
        self.isVideo = False
        self.altText = ""
        self.isImage = False
        self.imageSrc = ""

    def setLocation(self, column, row):
        self.column = column
        self.row = row

    def setImage(self, alt):
        self.alt = alt
        month = str(datetime.now().month)
        if len(month) < 2:
            month = "0" + month
        self.imageSrc = "/globalassets/images/lp/{}/{}/TK_IMAGE.JPG".format(
            month, str(datetime.now().year))

    def videoTrue(self):
        self.isVideo = True
