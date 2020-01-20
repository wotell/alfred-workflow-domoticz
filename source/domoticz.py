import os
import sys
from workflow import Workflow, ICON_ERROR, ICON_INFO

import Const
import Debug
import DomoticzHelpers
import DomoticzProxy

class Arguments:
    Show_DomoticzStatus = False
    Show_Room = False
    Show_Info = False
    DeviceIdx = ""
    ActionId = ""

    @property
    def ShowDevice(self):
        return (not self.DeviceIdx == "")

    @property
    def ExecuteAction(self):
        return (not self.ActionId == "")

    @classmethod
    def Parse(self, argv):
        result = Arguments()
        for arg in argv:
            if (arg == "status"):
                result.Show_DomoticzStatus = True
            elif (arg == "room"):
                result.Show_Room = True
            elif (str(arg).startswith("idx:")):
                result.DeviceIdx = str(arg).replace("idx:", "")
            elif (str(arg).startswith("action:")):
                result.ActionId = str(arg).replace("action:", "")
            elif (arg == "info"):
                result.Show_Info = True

        if (not result.Show_DomoticzStatus and not result.DeviceIdx and not result.ActionId):
            self.Show_Room = True # fallback to show-room when nothing is asked
        return result


def main(self):
    Debug.write("start")
    address = os.environ['domoticz_address']
    username = os.environ['domoticz_username']
    password = os.environ['domoticz_password']
    idxRoom = os.environ['domoticz_idxRoom']
    proxy = DomoticzProxy.DomoticzProxy(address, username, password)

    args = Arguments.Parse(sys.argv)
    if (args.ShowDevice):
        device = proxy.getDevice(args.DeviceIdx)
        if (args.Show_Info):
            device.infoToWorkflow(wf)
        else:
            if (args.ExecuteAction):
                action = device.getAction(args.ActionId)
                if (not action == None):
                    actionStatus = proxy.getAction(action.Action)
                    action.notify(actionStatus)
                device = proxy.getDevice(args.DeviceIdx) # Update device after executing action
            device.backToRoomActionToWorkflow(wf)
            device.actionsToWorkflow(wf)
            wf.add_item(
                title="Info",
                subtitle="show all data for device",
                icon=ICON_INFO,
                valid=False,
                autocomplete=DomoticzHelpers.CreateQuery(device.Room, device, None) + " info"
            )
    elif (args.Show_Room):
        room = proxy.getRoom(idxRoom)
        room.toWorkflow(wf)
    elif (args.Show_DomoticzStatus):
        status = proxy.getStatus()
        status.toWorkflow(wf)
    
    wf.send_feedback()
    Debug.write("end")

if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))