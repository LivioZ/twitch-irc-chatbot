# Twitch IRC Chatbot
Customizable implementation of a Twitch chatbot using the IRC protocol.

## Usage
Create a file named `secrets.json` and paste this:
```
{
  "chatbot_pass": "your_oauth_code"
}
```
where `your_oauth_code` is the code returned by https://twitchapps.com/tmi/ (connect with the account that the bot will use).

In the `chatbot.py` file edit:
* `channel` to the channel you want to connect, a channel is a `#` followed by a full lower case streamer name, for example: `#lirik`
* `botnick` to the full lower case name of the account of the bot (the same you used to generate the oauth code)

Customize the code in the while loop to do whatever you want, to be sure that you are processing a normal message just put this in the code that reads the message:
```python
if 'PRIVMSG' in text and channel in text and your_conditions:
```

### Notes
[Twitch IRC chatbot guide](https://dev.twitch.tv/docs/irc/guide)