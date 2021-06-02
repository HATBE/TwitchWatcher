import requests;
import time;
import subprocess as notification
from playsound import playsound

oauth = "<token>"
clientid = "<your clientid>"
streamer = "<streamer name>"

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': clientid,
    'Authorization': 'OAuth ' + oauth,
}

while(True):
    response = requests.get('https://api.twitch.tv/kraken/streams/followed', headers=headers)
    data = response.json()

    for i in range (0, len(data['streams'])): 

        if(data["streams"][i]["channel"]["name"] == streamer):
            if(data["streams"][i]["stream_type"] == "live"):
                notification.Popen(['notify-send', "Twitch Watcher", '-i', "twitch.png", streamer + " ist Online mit " + data["streams"][i]["channel"]["status"]])
                playsound("mixkit-bell-notification-933.wav")
                exit(1)
                
    time.sleep(60)
