from utils import calculateLogTimeSpan
STEP_FIG_DESC='Line plot of total steps taken over the time period with a reset a few miliseconds into the second day.'
STEP_FIG_PER_DATE_DESC='Bar Plot showing the total steps taken each day'
CALORIE_FIG_DESC='line chart shows the calorie count over time, with a stable high count that drastically drops at midnight.There was a consistent calorie count that abruptly decreased, possibly due to a reset in the counting at the start of a new day. Looking at the below plot one issue that arises is that the total calory count is abnormaly high for an individual as the values are > 1*10^5 as the normal daily calorie intake of a human is 1200-3000, we can also see that the value is not accumulated over the whole timeframe of the logs as the totalCalories value is reset to 0 at midnight'
STANDUP_FIG_DESC='Histograms of measuring the amount of times a user stood up during a time interval of 10 minutes. Standup occurrences were high early in the monitoring period and then showed variability, which reflects the user"s physical activity patterns'
SCREEN_STATUS_TIME_DESC='A line chart that shows the screen status over time, alternating between on and off, with a longer period of on status just before midnight. The screen status changes frequently, suggesting active use, with a notable period of inactivity towards the end of the observed timeframe.'
TIMELINE_VIEW_DESC='This timeline alternates between red and blue bars to indicate the screen being off (red) and on (blue) throughout the observed period. The screen"s on-off pattern is quite regular, which may indicate a pattern in user behavior or an automated process.'
COMPONENT_GRAPH_DESC='Histogram showing frequency of component being used. A few components are used significantly more often than others, indicating a potential area of focus for optimization or error checking'
EVENT_ID_GRAPH_DESC='Histogram showing frequency of event id being invoked. The event distribution is heavily skewed towards a few specific Event IDs.'
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