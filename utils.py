import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def preprocessData(data):
    timeFormat = '%Y%m%d-%H:%M:%S:%f'
    data['Time'] = pd.to_datetime(data['Time'], format=timeFormat)

    data['Date'] = data['Time'].dt.day
    data.sort_values('Time',ascending=True,inplace=True)

    return data
def calculateLogTimeSpan():
    data = pd.read_csv('HealthApp_2k.log_structured.csv',index_col='LineId')
    data = preprocessData(data)

    timeFrame = data['Time'].to_list()
    startTime = timeFrame[0]
    endTime = timeFrame[-1]
    totalTimeForLogs = timeFrame[-1] - timeFrame[0]


    StartDate = startTime.strftime('%Y-%m-%d')
    endDate = endTime.strftime('%Y-%m-%d')

    startTime = startTime.strftime('%Y-%m-%d %H:%M:%S')
    endTime = endTime.strftime('%Y-%m-%d %H:%M:%S')

    days = totalTimeForLogs.days
    hours, remainder = divmod(totalTimeForLogs.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"total Time considered in the logs is {days} days {hours} hours {minutes} minutes and {seconds} secondsStarting at {startTime} and Ending at {endTime}Dates covered in the logs {','.join(map(str, list(data['Date'].unique())))} in the year {''.join(map(str, list(data['Time'].dt.year.unique())))}",StartDate,endDate

def generateData(data:pd.DataFrame,eventId:str,splitString:str,listIndex:int,columnToCreate:str) -> pd.DataFrame:
    def splitContent(row):
        return int(row.split(splitString)[listIndex])
    data = data[data['EventId']==eventId]
    data[columnToCreate] = data['Content'].apply(splitContent)

    return data
    
def generateScreenStatusData(data):
    data['statusChange'] = 0

    data.loc[data['EventId'] == 'E41', 'statusChange'] = 1
    data.loc[data['EventId'] == 'E40', 'statusChange'] = -1

    data['screenStatus'] = data['statusChange'].cumsum().clip(lower=0)

    data.drop('statusChange', axis=1, inplace=True)
    data['yVal'] = 'Screen Status'
    data['ScreenStatusCat'] = data['screenStatus'].apply(lambda x: 'Screen On' if x > 0 else 'Screen Off')

    data['timeShifted'] = data['Time'].shift(-1)

    data['duration'] = (data['timeShifted'] - data['Time']).dt.total_seconds() /60

    return data