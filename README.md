## Sending Slack Messages 

* Install python library

`pip install slackinformer`

* Export Slack API Key Environment Variable as SLACK_CLIENT_API_KEY

`export SLACK_CLIENT_API_KEY=<YOUR_API_KEY>`

* Import slackinformer module.

`from slackinformer.slackinformer import send_slack_message`


* Create content to be sent. For example: 

`content = "YOLOv3 - Last Mean Average Precision(mAP) - Epoch(" + epoch + "): " + "*" + mAP + "*"`


* Create plot path. Suppose plot path is: output/map_epoch_plot.png

`img_path = os.path.join("output", "map_epoch_plot.png")`


* Send message

`send_slack_message(channel="#general", title="Image Title" content, img_path)`
