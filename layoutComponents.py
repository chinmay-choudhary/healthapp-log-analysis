from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

def createTitle(title):
    return dbc.Row([
        dbc.Col(html.H1(title, className="text-center title"), className="mb-5 mt-5")
    ])

def createDescription(description):
    return dbc.Row([
        dbc.Col(html.P(description, className="text-center"), className="mb-4")
    ])

def createGraphContent(description, figure_function):
    return dbc.Row([
        dbc.Col(html.P(description, className="text-center description-title"), className="mb-4"),
        dbc.Row(
            dbc.Col(dcc.Graph(figure=figure_function()), width={"size": 10, "offset": 0.5}),justify="center"
        )
    ])