from workflow import notify

import Debug
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

    def __init__(self, id, title, subtitle, action, notify = None, device = None):
        self.Id = id
        self.Device = device
        self.Title = title
        self.Subtitle = subtitle
        self.Action = action
        self.Notify = notify

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
            valid=False
        )        
