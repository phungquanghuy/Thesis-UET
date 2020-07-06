import osmium as osm

# Class lấy dữ liệu các nodes biển báo
class GetSign(osm.SimpleHandler):

    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.maxspeed_sign = []
        self.oneway_sign = []

    # Lấy nodes biển báo có tag maxspeed       
    def node(self, n):
        if "maxspeed" in n.tags:
            self.maxspeed_sign.append({'id': n.id, 'maxspeed': n.tags.get('maxspeed')})

    # Lấy nodes biển báo có tag oneway        
    def node_oneway(self, n):
        if "oneway" in n.tags:
            self.oneway_sign.append({'id': n.id, 'oneway': n.tags.get('oneway')})
    
    # Lấy nodes biển báo cấm       
    # def node(self, n):
    #     if "highway" in n.tags:
    #         self.sign_nodes.append({'id': n.id, 'highway': n.tags.get('highway')})