import copy
import Nodes

def create_node(id,parent,cost,open,close):
    new_node = Nodes.node()
    new_node.map_key = create_key(id)
    new_node.cost = copy.deepcopy(cost)
    new_node.is_open = copy.deepcopy( open )
    new_node.is_closed = close
    new_node.id = copy.deepcopy ([id[0], id[1]])
    if(parent!=None):
        new_node.parent_id = copy.deepcopy([parent[0],parent[1]])
    return new_node

def create_key(id):
    key = str(id[0]) + "_" + str(id[1])
    return key