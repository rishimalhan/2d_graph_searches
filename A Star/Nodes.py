class node(object):
    def __init__(self):
        self.id = None
        self.cost = None
        self.map_key = None
        self.is_open = None
        self.is_closed = None
        self.parent_id = None
        return