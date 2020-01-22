import sys
from workflow import notify

import Debug
sys.path.append('./devices')
import DomoticzDevice
import DomoticzHelpers

class DomoticzDeviceAction:
    Prefix = "action:"
    Id = None
    Device = None
    Title = None
    Subtitle = None
    Action = None
    Notify = None
    Icon = None

    def __init__(self, title, id="", subtitle = "", action = None, notify = None, device = None, icon = None):
        self.Id = id
        self.Device = device
        self.Title = title
        self.Subtitle = subtitle
        self.Action = action
        self.Notify = notify
        self.Icon = icon

    def notify(self, sucess):
        if (not self.Notify == None):
            if (sucess):
                notify.notify("Sucess: " + self.Notify)
            else:
                notify.notify("Fail: " + self.Notify)

    def toWorkflow(self, device, wf):
        Debug.write("Action->Workflow: " + self.Title)
        wf.add_item(
            title=self.Title,
            subtitle=str(self.Subtitle),
            autocomplete=DomoticzHelpers.CreateQuery(None if self.Device == None else self.Device.Room, self.Device, self),
            valid=False,
            icon=self.Icon
        )        
