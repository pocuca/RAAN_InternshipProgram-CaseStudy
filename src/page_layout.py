import dash_html_components as html
import dash_core_components as dcc
from plotter import make_plot

header = html.H1(
    children="RAAN Case Study - Bojana Počuča",
    id="main_header",
    style={"font-size": 24, "font-weight": "bolder", "text-align": "center"},
)

dropdown = dcc.Dropdown(
    id="DD",
    options=[
        {"label": "Random", "value": "random"},
        {"label": "Grid", "value": "grid"},
        {"label": "Circular", "value": "circle"},
        {"label": "Concentric", "value": "concentric"},
        {"label": "Cose", "value": "cose"},
        {"label": "Cose-bilkent", "value": "cose-bilkent"},
        {"label": "Klay", "value": "klay"},
        {"label": "Spread", "value": "spread"},
        {"label": "Cola", "value": "cola"},
        {"label": "Euler", "value": "euler"},
        {"label": "Dagre", "value": "dagre"},
        {"label": "Breadthfirst", "value": "breadthfirst"},
    ],
    value="klay",
)

div_plot = html.Div(id="plot-container", children=make_plot("random"))
div_page = html.Div([header, dropdown, div_plot])
