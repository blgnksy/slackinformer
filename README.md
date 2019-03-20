## Sending Slack Messages 

* Install python library

`pip install slackinformer`

* Import slackinformer module.

`from slackinformer.slackinformer import send_slack_message`


* Create content to be sent. For example: 

`content = "YOLOv3 - Last Mean Average Precision(mAP) - Epoch(" + epoch + "): " + "*" + mAP + "*"`


* Create plot path. Suppose plot path is: output/map_epoch_plot.png

`plot_path = os.path.join("output", "map_epoch_plot.png")`


* Send message

`send_slack_message(content, plot_path)`
