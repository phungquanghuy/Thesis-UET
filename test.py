import osmium as osm
import get_node

class StreetNormalizer(osm.SimpleHandler):

    def __init__(self):
        super(StreetNormalizer, self).__init__()
        self.node = get_node.GetWayNode()
        self.node.apply_file("VN.osm")

        # list các id đường + các node kèm theo
        # self.street_nodes = self.get_node.street_nodes
        # list các nodes biển báo 
        self.signs = self.node.sign_nodes

    def add_tag(self, o):
        # new tags should be kept in a list so that the order is preserved
        newtags = []
        # pyosmium is much faster writing an original osmium object than
        # a osmium.mutable.*. Therefore, keep track if the tags list was
        # actually changed.
        modified = False
        for t in o.tags:
            newtags.append(t)
        
        temp = []
        for n in o.nodes:
            temp.append(n.ref)
        
        for sign in self.signs:
            if sign['id'] in temp and not "maxspeed" in o.tags:
                newtags.append(("maxspeed", sign['maxspeed']))
                modified = True

        if modified:
            # We have changed tags. Create a new object as a copy of the
            # original one with the tag list replaced.
            return o.replace(tags=newtags)
        else:
            return o

    # def node(self, o):
    #     self.writer.add_node(o)

    # def way(self, o):
    #     self.writer.add_way(self.add_tag(o))

    # def relation(self, o):
    #     self.writer.add_relation(o)


# if __name__ == '__main__':

#     # path to the output file (OSM or PBF)
#     # writer = osm.SimpleWriter("/home/likk/data/vietnam1.osm.pbf")
#     writer = osm.SimpleWriter("VN1.osm")
#     # path to the input file (PBF)
#     StreetNormalizer(writer).apply_file("VN.osm")
#     writer.close()