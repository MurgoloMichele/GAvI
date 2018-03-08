import xml.sax


class XMLDocument(xml.sax.ContentHandler):

    PARSE_NONE = 0
    PARSE_TITLE = 1
    PARSE_AUTHORS = 2
    PARSE_AUTHOR_SURNAME = 3
    PARSE_AUTHOR_NAME = 4
    PARSE_DATE = 5
    PARSE_DATE_DAY = 6
    PARSE_DATE_MONTH = 7
    PARSE_DATE_YEAR = 8
    PARSE_ABSTRACT = 9
    PARSE_BODY = 10

    def __init__(self):
        self.state = XMLDocument.PARSE_NONE
        self.title = ""
        self.authors = []
        self.day = "01"
        self.month = "01"
        self.year = "1970"
        self.abstract = ""
        self.body = ""

    def startElement(self, name, attr):
        # Parse title
        if name == "article-title" and len(self.title) == 0:
            self.state = XMLDocument.PARSE_TITLE

        # Parse authors
        elif name == "contrib-group":
            self.state = XMLDocument.PARSE_AUTHORS

        elif self.state == XMLDocument.PARSE_AUTHORS:
            if name == "surname":
                self.state = XMLDocument.PARSE_AUTHOR_SURNAME

            elif name == "given-names":
                self.state = XMLDocument.PARSE_AUTHOR_NAME

        # Parse date
        elif name == "date" and attr.getValue("date-type") == "accepted":
            self.state = XMLDocument.PARSE_DATE

        elif self.state == XMLDocument.PARSE_DATE:
            if name == "day":
                self.state = XMLDocument.PARSE_DATE_DAY

            elif name == "month":
                self.state = XMLDocument.PARSE_DATE_MONTH

            elif name == "year":
                self.state = XMLDocument.PARSE_DATE_YEAR

        elif name == "abstract":
            self.state = XMLDocument.PARSE_ABSTRACT

        elif name == "body":
            self.state = XMLDocument.PARSE_BODY

    def endElement(self, name):
        if name == "contrib-group" or name == "date" or name == "abstract" or name == "body":
            self.state = XMLDocument.PARSE_NONE

    def characters(self, content):
        # Parse title
        if self.state == XMLDocument.PARSE_TITLE:
            self.title += content;
            self.state = XMLDocument.PARSE_NONE

        # Parse authors
        elif self.state == XMLDocument.PARSE_AUTHOR_SURNAME:
            self.authors.append(content)
            self.state = XMLDocument.PARSE_AUTHORS

        elif self.state == XMLDocument.PARSE_AUTHOR_NAME:
            self.authors[len(self.authors) - 1] += " " + content
            self.state = XMLDocument.PARSE_AUTHORS

        # Parse date
        elif self.state == XMLDocument.PARSE_DATE_DAY:
            self.day = str(int(content)).zfill(2)
            self.state = XMLDocument.PARSE_DATE

        elif self.state == XMLDocument.PARSE_DATE_MONTH:
            self.month = str(int(content)).zfill(2)
            self.state = XMLDocument.PARSE_DATE

        elif self.state == XMLDocument.PARSE_DATE_YEAR:
            self.year = content
            self.state = XMLDocument.PARSE_DATE

        elif self.state == XMLDocument.PARSE_ABSTRACT:
            self.abstract += content

        elif self.state == XMLDocument.PARSE_BODY:
            self.body += content