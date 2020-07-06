import processor
import osmium as osm

# Class xuất dữ liệu ra file OSM, PBF
class WriteTag(osm.SimpleHandler):
    def __init__(self, writer):
        super(WriteTag, self).__init__()
        self.writer = writer

    #hàm xuất dữ liệu node
    def node(self, o):
        self.writer.add_node(o)

    #hàm xuất dữ liệu way
    def way(self, o):
        self.writer.add_way(processor.AddTag().add_tag(o))

    #hàm xuất dữ liệu relation
    def relation(self, o):
        self.writer.add_relation(o)

if __name__ == '__main__':

    # path to the output file (OSM or PBF)
    writer = osm.SimpleWriter("VN1.osm")
    # path to the input file (PBF)
    WriteTag(writer).apply_file("VN.osm")
    writer.close()
    
    print("Write Success!")