import pandas as pd
import networkx as nx

# Read the data from the Excel file
def read_data():

    data = pd.read_excel(
        "data/raan_case_study interns.xlsx", sheet_name=["edges", "nodes"]
    )

    return data["edges"], data["nodes"]  # dictionaries


EDGES_DF, NODES_DF = read_data()

# The graph is directed and for this reason we use DiGraph
GRAPH: nx.Graph = nx.from_pandas_edgelist(
    EDGES_DF, "source_id", "target_id", ["weights"], create_using=nx.DiGraph()
)

NODE_ATTR = NODES_DF.set_index("node_id").T.to_dict()

# Weight the nodes on Page rank
PAGE_RANK = nx.pagerank(GRAPH, weight="weights")
