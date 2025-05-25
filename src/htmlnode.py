class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        str_to_return = ""
        for key in self.props:
            str_to_return = str_to_return + " " + key + "=" + '"' + self.props[key] + '"'
        return str_to_return
    def __repr__(self):
        return (f"HTMLNode({self.tag},{self.value},{self.children},{self.props})")
    
    def __eq__(self,node1):
        return (self.tag == node1.tag) and (self.value == node1.value) and (self.children == node1.children) and (self.props == node1.props)
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        if value == None:
            raise Exception ("value cannot be empty for leaf")
        super().__init__(tag,value,None,props)
        self.value = value
        self.tag = tag
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            html_formatted_text = "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
            return html_formatted_text
