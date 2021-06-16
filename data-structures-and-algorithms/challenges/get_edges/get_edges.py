from data_structures.graph.graph import Graph, Vertex

def get_edges(route_map, itinerary):

    def get_node_reference(city):

        for node in route_map.get_nodes():
            if node.val == city:
                return node
        return None

    if len(itinerary) < 2:
        raise ValueError('You must provide at least 2 cities')

    possible, price = True, 0
    start_city = get_node_reference(itinerary[0])

    for i in range(1, len(itinerary)):
        end_city = itinerary[i]
        connections = route_map.get_neighbors(start_city)

        for connection in connections:
            if connection['vertex'].val == end_city:
                price += connection['weight']
                start_city = get_node_reference(end_city)
                possible = True
                break
            else:
                possible = False

        if not possible:
            return (False, f'${0}')

    return (True, f'${price}')
