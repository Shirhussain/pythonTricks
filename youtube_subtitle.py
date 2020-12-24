import json


#with this program you can convert json file of youtube subtitle to a betify text 
#first open the video and goto inspect or press(F12) then network after that click on caption button and you can see a new file is oppen in 
# netwook so then right clik then open in new tab and save that json file afther that with this line of code you can read and 
#easly convert to text 
with open("timedtext.json") as f:
    data = json.load(f)



for d in data["events"]:
    print(d["segs"][0]["utf8"].replace("\n"," "))

 
# for dlownloading form youtube you can download by this tricks
# 1: add `ss` befor youtube.com or add `pwn` 
# 2: you can use youtube-dl also wihich i highly recommand  
