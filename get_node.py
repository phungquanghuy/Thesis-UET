import osmium as osm

class GetWayNode(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.sign_nodes = []

    # Lấy nodes biển báo có tag maxspeed       
    def node(self, n):
        if "maxspeed" in n.tags:
            self.sign_nodes.append({'id': n.id, 'maxspeed': n.tags.get('maxspeed')})