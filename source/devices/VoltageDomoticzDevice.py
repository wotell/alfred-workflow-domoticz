import Const
import DomoticzDevice
import DomoticzDeviceActions
import DomoticzHelpers

class VoltageDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(VoltageDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_Current

    def addActions(self):
        super(VoltageDomoticzDevice, self).addActions()
        self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
            title="Voltage", 
            subtitle=self.Data,
            device=self,
            icon=self.Icon
        ))

