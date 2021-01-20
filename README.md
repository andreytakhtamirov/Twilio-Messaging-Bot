# Twilio Messaging Bot
Uses Ngrok and Flask to receive sms message contents from a registered Twilio phone number to send back a response.
 
This program opens up the possibility of receiving internet-updated content through sms!

### Background

During the summer I wanted to step back from social media and reduce my online presence in general. I switched my SIM card to an old Blackberry Curve, which was out of support for my carrier's data services, but still could receive phone calls/text messages. However I still wanted to be able to check some frequently looked up information like the weather, time, and my email notifications, so I made this program. 

As of now, 2 commands are included: *time*, which sends back the current time, and *weather*, which sends back the details about the weather. (Examples of both can be found in the screenshot below).

More functionality can be added in the future, adding more commands for things like an sms-based search engine (utilizing Google's RESTful API), or a command to save some text sent in a message to the cloud. There are many other possible features!

It works by using Twilio, which provides a phone number and reroutes all received messages to ngrok, which then calls the Flask webpage to process the message and send back a response.

### Directions for Operation

*weather* requests the weather from the openweathermap api for a hard-coded city. The openweathermap api key needs to be configured before running.
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
