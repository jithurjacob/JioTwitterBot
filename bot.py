import tweepy, time, sys
from keys import keys
from datetime import datetime, date
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 





#enter the corresponding information from your Twitter application:
CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_KEY = keys["ACCESS_KEY"]
ACCESS_SECRET = keys["ACCESS_SECRET"]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def lambda_handler():
	api.update_with_media("jio_output.jpg", status= "@JioCare I'm done with this... https://github.com/jithurjacob/JioTwitterBot")# for AWS lamda scheduler
	print("done")
while True:
	font = ImageFont.truetype("Aaargh.ttf",40) #https://www.fontsquirrel.com/fonts/download/Aaargh
	jio_date = datetime.strptime("2-10-2016 14:00","%d-%m-%Y %H:%M")
	time_diff = (datetime.now() - jio_date ).total_seconds()
	num_days = int(time_diff/ (24*3600))
	num_hours = int((time_diff - (num_days*24*3600))/3600)
	num_minutes = int(((time_diff - (num_days*24*3600))%3600)/60)
	text = "It's been {} days, {} hours, {} minutes\nsince I got my SIM, it's still not activated.".format(num_days, num_hours, num_minutes)
	tcolor = (0,0,0)
	text_pos = (100,100)

	img = Image.open("jio_image.jpg")
	img = img.convert('RGB')
	draw = ImageDraw.Draw(img)
	draw.text(text_pos, text, fill=tcolor, font=font)
	del draw

	img.save("jio_output.jpg")#api.update_status("")
	api.update_with_media("jio_output.jpg", status= "@JioCare I'm done with this... https://github.com/jithurjacob/JioTwitterBot")
	print("Tweeted now ",datetime.now().strftime("%d-%m-%Y %H:%M"))
	time.sleep(900)#Tweet every 15 minutes

