import json
import os

from slackclient import SlackClient


def send_slack_message(channel, title="", content, img_path):
    if not os.path.isfile(img_path):
        print("File does not exist. Path: " + str(img_path))
        return

    slack_token = os.getenv("SLACK_CLIENT_API_KEY")
    sc = SlackClient(slack_token)

    response = sc.api_call(
        'files.upload',
        channels=channel,
        as_user=True,
        file=open(img_path, 'rb'),
        title=title,
        initial_comment=content
    )

    if not response['ok']:
        print("Message could not be sent to slack. Response: \n\n" + json.dumps(response, indent=4))
