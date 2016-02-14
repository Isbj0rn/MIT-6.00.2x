def test(src, dest, distance, outdoors):
    edges = {}
    edges[src]= []
    distances = (distance, outdoors)
    package = [dest, distances]
    edges[src].append(package)
    return edges

edges = {}
edges['dicks'] = [['b', (10, 5)]]
