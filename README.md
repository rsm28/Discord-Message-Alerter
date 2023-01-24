# Discord Message Alerter

A small Discord bot intended for alerting a user to messages sent in specific servers whilst using the "Do Not Disturb" status on Discord. Direct messages are sent from the bot to the host - these are significantly more visible on the taskbar than having to open the client to check for unread messages.

## Other features

### !recipe & !instructions

#### !recipe

Send a list of ingredients delimited by newlines (\n), receive a response of 5 recipes back, using OpenAI's Curie model.

#### !instructions

Send a recipe name, receive a response detailing the necessary instructions, using OpenAI's Curie model.

## Requirements

```
openai
discord.py
```

## config.json

In the root folder, create a config.json file, and format it as such:

```json
    "token": "[bot token]",
    "user_id": "[user id]",
    "openai_api_key": "[openai api key]
```
