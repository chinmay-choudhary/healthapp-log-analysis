from utils import calculateLogTimeSpan
STEP_FIG_DESC='Line plot of total steps taken over the time period with a reset a few miliseconds into the second day.'
STEP_FIG_PER_DATE_DESC='Bar Plot showing the total steps taken each day'
CALORIE_FIG_DESC='Plot of total calories over the time period. Looking at the below plot one issue that arises is that the total calory count is abnormaly high for an individual as the values are > 1*10^5 as the normal daily calorie intake of a human is 1200-3000, we can also see that the value is not accumulated over the whole timeframe of the logs as the totalCalories value is reset to 0 at midnight'
STANDUP_FIG_DESC='Histograms of measuring the amount of times a user stood up during a time interval of 10 minutes'
SCREEN_STATUS_TIME_DESC='The screen status vs time with a 1 representing that sceen was on and a 0 representing that the screen was off'
TIMELINE_VIEW_DESC='The timeline view of the screen status with screen off shown in blue and screen on shown in red'
COMPONENT_GRAPH_DESC='Histogram showing frequency of component being used. Looking at the graph we conclude that the most used components is STEP_LSC being used 710 and the least used components are Step_ScreenUtil,Step_ScreenUtil, and Step_NotificationUtil being used 1 time'
EVENT_ID_GRAPH_DESC='Histogram showing frequency of event id being invoked. Looking at the graph conclude that Event E39 was invoked 273 times being the most invoked'
STEPS_EVENT_ID='E22'
STEP_LIST_SPLIT_INDEX=1
STEP_SPLIT_STRING='##'
CALORIE_EVENT_ID='E4'
CALORIE_LIST_SPLIT_INDEX=-1
CALORIE_SPLIT_STRING='='
ACTIVE_EVENT_ID='E42'
ACTIVE_LIST_SPLIT_INDEX=-1
ACTIVE_SPLIT_STRING=' '
APP_DESC=f"This dashboard provides an analysis of log data for a health app in which {calculateLogTimeSpan()}"