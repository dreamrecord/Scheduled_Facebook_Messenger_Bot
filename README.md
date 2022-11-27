# Scheduled_Facebook_Messenger_Bot
This is a pretty straight forward and simple bot that sends out an automatic message at specific time of day or week
You should use Cron job for scheduling purposes but you can also use python function i wrote which i dont recommend because you have to leave your script running all the time.

## Update
### [2022-11-27] Prepare message beforehand and send at exact time
All user-specific inputs are moved to config.json.
- "contact" is the contact user id which could be found in messenger URL.

Usage:
```
python3 scheduled_messenger_bot.py config.json
```
