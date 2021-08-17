Python Desktop Notifier using Plyer module ::-->>

A desktop notifier is a simple application which produces a notification message in form of a pop-up message on desktop. We will be using plyer module for the same.


Module Needed:

1. time: This module works with the time object and is installed by default

2. Plyer: Plyer module is used to access the features of the hardware. This module does not comes built-in with Python. We need to install it externally. To install this module type the below command in the terminal.

pip install plyer 

Approach:

Step 1) Import the notification class from the plyer module

from plyer import notification

Step 2) After that you just need to call the notify method of this class.

Syntax: 
notification.notify(
    title=”,
    message=”,
    app_name=”,
    app_icon=”,
    timeout=10,
    ticker=”,
    toast=False
)

Example :->

import time
from plyer import notification


if __name__=="__main__":

		notification.notify(
			title = "HEADING HERE",
			message=" DESCRIPTION HERE" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)
