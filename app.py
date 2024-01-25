from dash import Dash, html
import dash_bootstrap_components as dbc
from graphing import createStepLinePlot, createStepsBarplot, createCaloriesPlot, createActivePlot, createScreenDataLineFig, createScreenStatusTimeline,createComponentHistogram,createEventIdHistogram
from enums import APP_DESC,STEP_FIG_DESC,STEP_FIG_PER_DATE_DESC,CALORIE_FIG_DESC,STANDUP_FIG_DESC,SCREEN_STATUS_TIME_DESC,TIMELINE_VIEW_DESC,COMPONENT_GRAPH_DESC,EVENT_ID_GRAPH_DESC
from layoutComponents import createDescription,createGraphContent,createTitle

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def generate_layout():
    return html.Div([
        dbc.Container([
            createTitle("Health App Step Count Analysis"),
            createDescription(APP_DESC),
            createGraphContent(STEP_FIG_DESC, createStepLinePlot),
            createGraphContent(STEP_FIG_PER_DATE_DESC, createStepsBarplot),
            createGraphContent(CALORIE_FIG_DESC, createCaloriesPlot),
            createGraphContent(STANDUP_FIG_DESC, createActivePlot),
            createGraphContent(SCREEN_STATUS_TIME_DESC, createScreenDataLineFig),
            createGraphContent(TIMELINE_VIEW_DESC, createScreenStatusTimeline),
            createGraphContent(COMPONENT_GRAPH_DESC,createComponentHistogram),
            createGraphContent(EVENT_ID_GRAPH_DESC,createEventIdHistogram)
        ])
    ])

app.layout = generate_layout

app.run_server(debug=False,host='0.0.0.0')
