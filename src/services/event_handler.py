import asyncio
import json

from src.database import DatabaseService
from src.services import logger
from config.settings import Settings


from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from slack_sdk import WebClient


eventApp = AsyncApp(token=Settings.SLACK_BOT_TOKEN)
handler = AsyncSocketModeHandler
client = WebClient(token=Settings.SLACK_BOT_TOKEN)


@eventApp.event("app_mention")
async def handle_app_mention_events(event, say):
    content = await handle_event(event)
    await say(content)


@eventApp.event("message")
async def handle_message(event, say):
    await handle_event(event)


@eventApp.event("reaction_added")
async def handle_reaction_added_events(event, say):
    await handle_event(event)


@eventApp.event("reaction_removed")
async def handle_reaction_removed_events(event, say):
    await handle_event(event)


@eventApp.event("team_join")
async def handle_team_join_events(event, say):
    await handle_event(event)


@eventApp.event("user_change")
async def handle_user_change_events(event, say):
    await handle_event(event)


@eventApp.command("/hi")
async def handle_some_command(ack, body, say):
    response = client.conversations_open(users=["U1234567890"])
    dm_channel = response["channel"]["id"]

    # Step 2: Send message in DM
    client.chat_postMessage(
        channel=dm_channel,
        text="Hey 👋 this is a private DM with the bot!",  # TODO: Add logic to handle command
    )


async def handle_event(event: dict):

    databaseService = DatabaseService()
    await databaseService.connect()
    eventType = event.get("type")

    import json

    with open("ref/event.json", "w") as f:
        json.dump(event, f)

    if eventType == "message":
        if event.get("channel_type") == "im":
            user = event.get("user")
            text = event.get("text")
            channel = event.get("channel")
            ts = event.get("ts")
            channelData = client.conversations_info(channel=channel)
            await databaseService.create_channel(channelData.get("channel"))
            await databaseService.create_message(event, channel)
            logger.info(f"[{channel}] {user}: {text} ({ts})")
        elif "subtype" not in event:
            user = event.get("user")
            text = event.get("text")
            channel = event.get("channel")
            ts = event.get("ts")
            await databaseService.create_message(event, channel)
            logger.info(f"[{channel}] {user}: {text} ({ts})")
        elif event.get("subtype") == "message_deleted":
            previous_message = event.get("previous_message")
            await databaseService.delete_message(previous_message.get("ts"))
            logger.info(f"Message deleted: {previous_message.get("ts")}")
        elif event.get("subtype") == "message_changed":
            message = event.get("message")
            messageData = {
                "isEdited": True,
                "editedAt": message.get("edited", {}).get("ts"),
                "editedBy": message.get("edited", {}).get("user"),
                "text": message.get("text"),
            }

            await databaseService.update_message(message.get("ts"), messageData)
            logger.info(f"Message changed: {message.get("ts")}")

    elif eventType == "app_mention":
        user = event.get("user")
        response = client.conversations_open(users=user)

        return "Hi"  # TODO: Add logic to handle app mention
    elif eventType == "reaction_added":
        messageId = event.get("item").get("ts")
        reactionsData = [
            {
                "name": event.get("reaction"),
                "users": [event.get("user")],
                "messageId": messageId,
            }
        ]
        await databaseService._create_reactions(messageId, reactionsData)
        logger.info(
            f"Reaction {event.get("reaction")} added to {messageId}: {event.get("user")}"
        )
    elif eventType == "reaction_removed":
        messageId = event.get("item").get("ts")
        reactionsData = [
            {
                "name": event.get("reaction"),
                "users": [event.get("user")],
                "messageId": messageId,
            }
        ]
        await databaseService._delete_reactions(messageId, reactionsData)
        logger.info(
            f"Reaction {event.get("reaction")} removed from {messageId}: {event.get("user")}"
        )
    elif eventType == "team_join":
        user = event.get("user")
        await databaseService.create_user(user)
    elif eventType == "user_change":
        user = event.get("user")
        await databaseService.create_user(user)
    else:
        logger.debug(f"Unhandled event: {eventType}")
