from datetime import datetime


class HTMLObject:
    def __init__(self, row, column):
        self.html = ""
        self.column = column
        self.row = row
        self.isVideo = False
        self.altText = ""
        self.isImage = False
        self.imageSrc = ""

    def setImage(self, alt):
        self.isImage = True
        self.alt = alt
        month = str(datetime.now().month)
        if len(month) < 2:
            month = "0" + month
        self.imageSrc = "/globalassets/images/lp/{}/{}/TK_IMAGE.JPG".format(
            month, str(datetime.now().year))

    def videoTrue(self, alt, link):
        self.isVideo = True
        self.videoLink = link
        self.alt = alt

    def renderComponent(self):
        # Image code
        if self.isImage:
            self.html = "<a href='/TK-LINK'><img src='{}' alt='{}' class='img-responsive'></a>".format(
                self.imageSrc, self.alt)
        # Video code - will need to insert modal later
        if self.isVideo:
            self.html = "<div class='videoModal'><div id='mobile_modal' data-toggle='modal' data-target='#modal-video_01' tabindex='0' data-theVideo='{}'><img class='img-responsive video-thumb' src='/TK-VIDEO-THUMB.JPG' alt='{}'></div></div>".format(
                self.videoLink, self.alt)
        # Nest it all in a div - No image or video? That's fine, it'll make a div with nothing in it!
        self.html = "<div class='{}{}'>{}</div>".format(
            str(self.row), str(self.column), self.html)
        return(self.html)
