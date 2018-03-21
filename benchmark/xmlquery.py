import xml.sax


class XMLQuery(xml.sax.ContentHandler):

    PARSE_NONE = 0
    PARSE_BEGIN = 1
    PARSE_QUERY = 2
    PARSE_END = 3

    def __init__(self, query_num):
        self.state = XMLQuery.PARSE_NONE
        self.num = str(query_num)
        self.text = ""

    def startElement(self, name, attr):
        if name == "topic" and attr.getValue("number") == self.num:
            self.state = XMLQuery.PARSE_BEGIN

        if name == "summary" and self.state == XMLQuery.PARSE_BEGIN:
            self.state = XMLQuery.PARSE_QUERY

    def characters(self, content):
        if self.state == XMLQuery.PARSE_QUERY:
            self.text += content
            self.state = XMLQuery.PARSE_END



