import osmium as osm
import get_node

class AddTag(osm.SimpleHandler):

    # hàm khởi tạo
    def __init__(self):
        super(AddTag, self).__init__()
        self.node = get_node.GetSign()
        self.node.apply_file("VN.osm")
        self.maxspeeds = self.node.maxspeed_sign
        self.oneways = self.node.oneway_sign

    # hàm xử lý thêm tính chất vào đường
    def add_tag(self, o):
        newtags = []
        modified = False
        for t in o.tags:
            newtags.append(t)
        
        # duyệt các nodes thuộc đường
        temp = []
        for n in o.nodes:
            temp.append(n.ref)
        
        # Nếu biển báo là 1 node thuộc đường thì thêm tính chất của biển vào tính chất của đường
        for maxspeed in self.maxspeeds:
            if maxspeed['id'] in temp and not "maxspeed" in o.tags:
                newtags.append(("maxspeed", maxspeed['maxspeed']))
                modified = True
        for oneway in self.oneways:
            if oneway['id'] in temp and not "oneway" in o.tags:
                newtags.append(("oneway", oneway['oneway']))
                modified = True

        if modified:
            return o.replace(tags=newtags)
        else:
            return o
