
# Function to check all the data and determine what clothes to wear
def processData(data):
    clothes = {
        'Hat': False,
        'Sweater': False,
        'Jacket': False,
        'Gloves': False,
        'Rain Coat': False,
        'Snow Jacket': False,
        'Wind Jacket': False,
        'Inside': False
    }
    whatWeather = {}
    averageTemp = 0
    averageFeel = 0
    averageWind = 0
    for block in data:

        ## TODO
        # Hazardius Weather conditions

        ## Checking for special weather conditions
        # Checking if snow
        if block['weather'][0]['main'] == 'Snow':

            for clothing, value in clothes.items():
                if clothing == 'Snow Jacket':
                    clothes[clothing] = True
                else:
                    clothes[clothing] = False

        # Checking if rain
        if block['weather'][0]['main'] == 'rain' or block['weather'][0]['main'] == 'drizzle':

            # If there is snow the same day then dont run this
            if clothes['Snow Jacket'] == False:
                
                for clothing, value in clothes.items():
                    if clothing == 'Rain Coat':
                        clothes[clothing] = True
                    else:
                        clothes[clothing] = False

        # Checking if there is hard wind
        if block['wind']['speed'] > 19:

            if clothes['Snow Jacket'] == False or clothes['Rain Coat'] == False:

                for clothing, value in clothes.items():
                    if clothing == 'Wind Jacket':
                        clothes[clothing] = True
                    else:
                        clothes[clothing] = False

        ## Checking for temperatures

        # Checking if there is need for a regular Jacket
        if block['main']['temp'] > -5 and block['main']['temp'] < 15:

            if not clothes['Wind Jacket'] or not clothes['Rain Coat'] or not clothes['Snow Jacket']:

                for clothing, value in clothes.items():
                    if clothing == 'Jacket':
                        clothes[clothing] = True
                    else:
                        clothes[clothing] = False

        if block['main']['temp'] < 20:
            clothes['Sweater'] = True

        if block['main']['temp'] < 15:
            clothes['Gloves'] = True
            clothes['Hat'] = True        
        
        # Getting descriptive text values
        if block['weather'][0]['description'] in whatWeather:
            whatWeather[block['weather'][0]['description']] += 1
        else:
            whatWeather[block['weather'][0]['description']] = 1

        # Getting the temperatures
        averageTemp += int(block['main']['temp'])
        averageFeel += int(block['main']['feels_like'])
        averageWind += int(block['wind']['speed'])


    # choosing key with highest value
    weatherDesc = max(whatWeather, key=whatWeather.get)

    # Averageing temparatures and indexing in a dict
    temperatures = {
        'temp': round(averageTemp/3),
        'feel': round(averageFeel/3),
        'wind': round(averageWind/3),
    }

    # setting up the processed data to a list

    processedData = [clothes, weatherDesc, temperatures]
    return processedData

def createMessage(data):

    # Creating message to send to phone
    message = f"It's going to be {data[1]} today.\nThe temperature is {data[2]['temp']}°, but feels like {data[2]['feel']}°. \nThe wind is blowing at {data[2]['wind']} meters per second. \nThe Clothes for this weather is:"
    for clothing, value in data[0].items():
        if value:
            message += f" {clothing},"
    return message
