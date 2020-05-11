import test
import osmium as osm

class WriteTag(osm.SimpleHandler):
    def __init__(self, writer):
        super(WriteTag, self).__init__()
        self.writer = writer

    def node(self, o):
        self.writer.add_node(o)

    def way(self, o):
        self.writer.add_way(test.StreetNormalizer().add_tag(o))

    def relation(self, o):
        self.writer.add_relation(o)

if __name__ == '__main__':

    # path to the output file (OSM or PBF)
    # writer = osm.SimpleWriter("/home/likk/data/vietnam1.osm.pbf")
    writer = osm.SimpleWriter("VN1.osm")
    # path to the input file (PBF)
    WriteTag(writer).apply_file("VN.osm")
    writer.close()