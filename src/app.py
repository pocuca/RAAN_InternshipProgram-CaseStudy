import dash
from dash.dependencies import Input, Output
from plotter import make_plot
from page_layout import div_page

app = dash.Dash(__name__)
server = app.server

app.layout = div_page

# Callbacks
@app.callback(Output("plot-container", "children"), Input("DD", "value"))
def update_plot(value):

    new_plot = make_plot(value)

    return new_plot


if __name__ == "__main__":
    app.run_server()
