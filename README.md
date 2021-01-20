# Twilio Messaging Bot
 Uses Ngrok and Flask to recieve sms message contents from a registered Twilio phone number to send back a response.

So far includes 2 commands: time, and weather.

weather requests the weather from the openweathermap api for a hard-coded city. The openweathermap api key needs to be configured before running.
https://openweathermap.org/current

After the python script is run, open **Terminal** and type 
>ngrok http 5000

5000, being whatever port the Flask application runs on.

Next, your twilio number must be configured for port forwarding to Ngrok,

![Screenshot of my Ngrok configuration](/Screenshots/ngrok.jpg)

Notice the forwarding link

![Screenshot of my Twilio forwarding configuration](/Screenshots/twilio.jpg)

Notice the messaging forwarding link and "/sms"

<img width="300" src="https://github.com/andreytakhtamirov/Twilio-Messaging-Bot/blob/main/Screenshots/messages.jpg">

Screenshot of the bot responding to messages
