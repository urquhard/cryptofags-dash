import dash
from dash import html, dash_table
from flask import current_app
from .data_loader import load_data

def init_dashboard(server):
    dash_app = dash.Dash(
        __name__,
        server=server,
        url_base_pathname='/dashboard/'
    )

    # Define a function to serve the layout dynamically
    def serve_layout():
        # Load data fresh on each page load
        
        df1, df2 = load_data(server.config)

        table1 = dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in df1.columns],
            data=df1.to_dict('records'),
            page_size=10,
            sort_action='native',
            filter_action='native'
        )

        table2 = dash_table.DataTable(
            id='table2',
            columns=[{"name": i, "id": i} for i in df2.columns],
            data=df2.to_dict('records'),
            page_size=10,
            sort_action='native',
            filter_action='native'
        )

        return html.Div([
            html.H1("Funding strategy:"),
            html.H2("telegram Jordan data"),
            table1,
            html.H2("tokens exchange data"),
            table2
        ])

    # Assign the layout function to the Dash app
    # This ensures the layout (and therefore data load) happens on every page load.
    dash_app.layout = serve_layout

    return dash_app
