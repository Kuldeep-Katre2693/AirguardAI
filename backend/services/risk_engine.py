AQI_LEVELS = [

    (0,50,"Good"),

    (51,100,"Satisfactory"),

    (101,200,"Moderate"),

    (201,300,"Poor"),

    (301,400,"Very Poor"),

    (401,500,"Severe")

]
def get_aqi_category(aqi):

    for low, high, label in AQI_LEVELS:

        if low <= aqi <= high:

            return label

    return "Hazardous"
def calculate_risk(aqi):

    if aqi <= 50:

        return {

            "children":10,

            "elderly":10,

            "asthma":20

        }

    elif aqi <=100:

        return {

            "children":20,

            "elderly":20,

            "asthma":40

        }

    elif aqi<=200:

        return {

            "children":60,

            "elderly":70,

            "asthma":85

        }

    elif aqi<=300:

        return {

            "children":85,

            "elderly":90,

            "asthma":95

        }

    else:

        return {

            "children":100,

            "elderly":100,

            "asthma":100

        }
def recommendation(aqi):

    if aqi<=50:

        return "Enjoy outdoor activities."

    elif aqi<=100:

        return "Sensitive people should limit prolonged exposure."

    elif aqi<=200:

        return "Wear a mask outdoors and reduce outdoor exercise."

    elif aqi<=300:

        return "Stay indoors whenever possible."

    else:

        return "Avoid outdoor activities. Air purifier recommended."