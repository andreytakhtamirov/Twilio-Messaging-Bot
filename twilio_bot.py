import time
import urllib

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# set this to your openweathermap api key
api_key = "YOUR_KEY"

base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Waterloo"
KELVIN_TO_CELSIUS = 273.15


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    print(incoming_msg)

    # return the weather
    if "weather" in incoming_msg:
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            # arrange the return string
            quote = "The weather is: " + str(weather_description) + "\nTemperature: " + str(round(current_temperature -
                KELVIN_TO_CELSIUS, 0)) + " C" + "\nHumidity: " + str(current_humidity)
        else:
            quote = "City Not Found "

        msg.body(quote)
        responded = True

    # return the current time (HH:MM:SS)
    if "time" in incoming_msg:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        msg.body("The current time is: " + current_time)
        responded = True

    if not responded:
        msg.body(ask_wolfram(question=incoming_msg))
    return str(resp)


def ask_wolfram(question) -> str:
    appid = "YOUR_KEY"
    query = urllib.parse.quote_plus(question)
    query_url = f"http://api.wolframalpha.com/v1/result?" \
                f"appid={appid}" \
                f"&input={query}" \
                f"&format=plaintext"

    r = requests.get(query_url)
    print(r.text)
    return r.text


if __name__ == "__main__":
    app.run(debug=True)
