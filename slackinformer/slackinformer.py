import json
import os

from slackclient import SlackClient


def send_slack_message(content, plot_path):
    if not os.path.isfile(plot_path):
        print("File does not exist. Path: " + str(plot_path))
        return

    slack_token = os.getenv("SLACK_CLIENT_API_KEY")
    sc = SlackClient(slack_token)

    response = sc.api_call(
        'files.upload',
        channels='#ml-cv-results',
        as_user=True,
        file=open(plot_path, 'rb'),
        title='Epoch vs mAP',
        initial_comment=content
    )

    if not response['ok']:
        print("Message could not be sent to slack. Response: \n\n" + json.dumps(response, indent=4))
