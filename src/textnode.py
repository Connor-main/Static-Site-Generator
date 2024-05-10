class TextNode:
    def __init__(self,text,text_type,url):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(Textnode_A,Textnode_B):
        return Textnode_A.text == Textnode_B.text and Textnode_A.text_type == Textnode_B.text_type and Textnode_A.url == Textnode_B.url
    def __repr__(self):
        return self.text + " "+self.text_type + " "+ self.url