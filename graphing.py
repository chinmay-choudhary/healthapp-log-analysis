import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from utils import *
from enums import STEPS_EVENT_ID,ACTIVE_EVENT_ID,CALORIE_EVENT_ID,STEP_LIST_SPLIT_INDEX,CALORIE_LIST_SPLIT_INDEX,ACTIVE_LIST_SPLIT_INDEX,STEP_SPLIT_STRING,CALORIE_SPLIT_STRING,ACTIVE_SPLIT_STRING

data = pd.read_csv('HealthApp_2k.log_structured.csv',index_col='LineId')
data = preprocessData(data)
_,StartDate,endDate = calculateLogTimeSpan()

def createStepLinePlot():
    
    steps = generateData(data,STEPS_EVENT_ID,STEP_SPLIT_STRING,STEP_LIST_SPLIT_INDEX,'steps')

    stepFigSub = make_subplots(rows=2, cols=2, specs=[[{"colspan": 2}, None], [{}, {}]],subplot_titles=['Steps Over Total Time',f'Steps On {StartDate}',f'Steps On {endDate}'])


    overallSteps = go.Scatter(x=steps["Time"], y=steps["steps"], mode='lines+markers',showlegend=False)
    stepsDay1 = go.Scatter(x=steps["Time"], y=steps[steps["Date"]==23]["steps"], mode='lines+markers',showlegend=False)
    stepsDay2 = go.Scatter(x=steps["Time"], y=steps[steps["Date"]==24]["steps"], mode='lines+markers',showlegend=False)


    stepFigSub.add_trace(overallSteps, row=1, col=1)
    stepFigSub.add_trace(stepsDay1, row=2, col=1)
    stepFigSub.add_trace(stepsDay2, row=2, col=2)

    stepFigSub.add_annotation(
        x=steps.loc[steps[steps['steps'] == 0].index[0]]['Time'],
        y=1,
        text=f"Steps Reset at {steps.loc[steps[steps['steps'] == 0].index[0]]['Time'].strftime('%Y-%m-%d %H:%M:%S')}",
        showarrow=True,
        arrowhead=1,
        ax=20,
        ay=-20,
        xref="x",
        yref="y",
        row=1,
        col=1
    )

    stepFigSub.update_layout(
        height=800, 
        width=1200, 
        title_text="Step Count Over Time", 
        title_font_size=24,
        
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        
        plot_bgcolor='white',
        paper_bgcolor='white',
        
    )
    return stepFigSub

def createStepsBarplot():
    steps = generateData(data,STEPS_EVENT_ID,STEP_SPLIT_STRING,STEP_LIST_SPLIT_INDEX,'steps')
    stepsPerDate = steps.groupby('Date')['steps'].last().reset_index()
    stepsPerDateFig = px.bar(stepsPerDate, x="Date", y="steps", text="steps")

    stepsPerDateFig.update_layout(
        height=600,
        width=1200,
        title='Steps Per Date',
        xaxis_title='Date',
        yaxis_title='Steps',
        legend=dict(title='Steps', x=1, y=1),
        title_font_size=24,
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return stepsPerDateFig

def createCaloriesPlot():
    calories = generateData(data,CALORIE_EVENT_ID,CALORIE_SPLIT_STRING,CALORIE_LIST_SPLIT_INDEX,'calories')
    calorieFigSub = make_subplots(rows=2, cols=2, specs=[[{"colspan": 2}, None], [{}, {}]],subplot_titles=['Calories Over Total Time',f'calories On {StartDate}',f'calories On {endDate}'])


    overallSteps = go.Scatter(x=calories["Time"], y=calories["calories"], mode='lines+markers',showlegend=False)
    caloriesDay1 = go.Scatter(x=calories["Time"], y=calories[calories["Date"]==23]["calories"], mode='lines+markers',showlegend=False)
    caloriesDay2 = go.Scatter(x=calories["Time"], y=calories[calories["Date"]==24]["calories"], mode='lines+markers',showlegend=False)


    calorieFigSub.add_trace(overallSteps, row=1, col=1)
    calorieFigSub.add_trace(caloriesDay1, row=2, col=1)
    calorieFigSub.add_trace(caloriesDay2, row=2, col=2)


    calorieFigSub.update_layout(
        height=800, 
        width=1200, 
        title_text="Calorie Count Over Time", 
        title_font_size=24,
        
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        
        plot_bgcolor='white',
        paper_bgcolor='white',
        
    )

    return calorieFigSub

def createActivePlot():
    active = generateData(data,ACTIVE_EVENT_ID,ACTIVE_SPLIT_STRING,ACTIVE_LIST_SPLIT_INDEX,'standUp')
    activeFig = make_subplots(rows=2, cols=2, specs=[[{"colspan": 2}, None], [{}, {}]],subplot_titles=['Standup Count Over Total Time',f'Standup Count on {StartDate}',f'Standup Count {endDate}'])


    overallActive = go.Histogram(x=active["Time"],showlegend=False)
    activeDay1 = go.Histogram(x=active[active["Date"]==23]["Time"],showlegend=False)
    activeDay2 = go.Histogram(x=active[active["Date"]==24]["Time"],showlegend=False)


    activeFig.add_trace(overallActive, row=1, col=1)
    activeFig.add_trace(activeDay1, row=2, col=1)
    activeFig.add_trace(activeDay2, row=2, col=2)

    activeFig.update_layout(
        height=800, 
        width=1200, 
        title_text="Standup Count Over Time", 
        title_font_size=24,
        
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis2=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        xaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis3=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        
        plot_bgcolor='white',
        paper_bgcolor='white',
        
    )
    return activeFig

def createScreenDataLineFig():

    screenData = generateScreenStatusData(data)

    statusFig = px.line(screenData, x='Time', y='screenStatus')

    statusFig.update_layout(
        height=400, 
        width=1200, 
        title_text='Screen Status Over Time',
        title_font_size=24,
        
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        
        plot_bgcolor='white',
        paper_bgcolor='white',
        
    )
    return statusFig

def createScreenStatusTimeline():
    screenData = generateScreenStatusData(data)
    timelineFig = px.timeline(screenData, x_start='Time', x_end='timeShifted', y='yVal', color='ScreenStatusCat', color_continuous_scale='bluered')

    timelineFig.update_layout(
        height=400, 
        width=1200, 
        title_text='Event Timeline of Screen Status',
        title_font_size=24,
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True,title_text=''),
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return timelineFig

def createComponentHistogram():
    componentCount = data["Component"].value_counts().reset_index()
    componentCount.columns = ['Component', 'Frequency']

    componentHistogram = go.Figure(go.Bar(
        x=componentCount['Component'], 
        y=componentCount['Frequency'],
        showlegend=False,
        text=componentCount['Frequency']
    ))
    componentHistogram.update_layout(
        height=400, 
        width=1200, 
        title_text='Histogram for Component',
        title_font_size=24,
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True,title_text=''),
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return componentHistogram

def createEventIdHistogram():
    eventIdCount = data["EventId"].value_counts().reset_index()
    eventIdCount.columns = ['EventId', 'Frequency']

    eventIdHistogram = go.Figure(go.Bar(
        x=eventIdCount['EventId'], 
        y=eventIdCount['Frequency'],
        showlegend=False,
        text=eventIdCount['Frequency']
    ))
    eventIdHistogram.update_layout(
        height=400, 
        width=1200, 
        title_text='Histogram for EventId',
        title_font_size=24,
        xaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True),
        yaxis=dict(showgrid=False, linecolor='black', linewidth=2, mirror=True,title_text=''),
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return eventIdHistogram

