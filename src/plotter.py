import dash_cytoscape as cyto
from data.reader import GRAPH, NODE_ATTR, PAGE_RANK

cyto.load_extra_layouts()

# Transform networx graph into list of elements for cytoscape
def nx_to_cs(graph):
    elem = []
    for source_node, target_node in GRAPH.edges:
        weight = GRAPH.adj[source_node][target_node]["weights"]
        element = {
            "data": {
                "source": source_node,
                "target": target_node,
                "weight": weight,
                "weight_2": weight / 2,
            },
        }
        elem.append(element)
    for node in GRAPH.nodes:
        element = {
            "data": {
                "id": node,
                "name": NODE_ATTR[node]["node_label"],
                "node_color": NODE_ATTR[node]["node_color"],
                "page_rank": PAGE_RANK[node],
            },
        }
        elem.append(element)
    return elem


# Transform the graph to elements and plot
def make_plot(layout):
    elements = nx_to_cs(GRAPH)
    my_plot = cyto.Cytoscape(
        id="my_plot",
        elements=elements,
        style={"width": "100%", "height": "700px"},
        layout={"name": layout},
        stylesheet=[
            {
                "selector": "node",
                "style": {
                    "label": "data(name)",
                    "background-color": "data(node_color)",
                    "color": "data(node_color)",
                    "width": f"mapData(page_rank, 0, {max(list(PAGE_RANK.values()))}, 15, 50)",
                    "height": f"mapData(page_rank, 0, {max(list(PAGE_RANK.values()))}, 15, 50)",
                    "opacity": 0.5,
                },
            },
            {
                "selector": "edge",
                "style": {
                    "curve-style": "bezier",
                    "width": "data(weight_2)",
                    "target-arrow-shape": "vee",
                    "opacity": 0.5,
                },
            },
        ],
    )
    return my_plot
