from src.api import getWeatherData, sendMessage
from src.util import processData, createMessage
import schedule
import time


def main():
    def working():
        data = getWeatherData(['56.1629','10.2039'])
        weatherBlocks = data['list']

        processedData = processData(weatherBlocks)

        message = createMessage(processedData)    

        sendMessage(message)

    schedule.every().day.at("06:00").do(working)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    main()