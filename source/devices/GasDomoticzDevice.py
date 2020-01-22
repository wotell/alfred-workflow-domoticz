import Const
import DomoticzDevice
import DomoticzDeviceActions

class GasDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(GasDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_Gas

    @property
    def Data(self):
        return self._info["CounterToday"] + " " + self._info["Data"]

    def addActions(self):
        super(GasDomoticzDevice, self).addActions()
        self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
            title="Gas", 
            subtitle=self.Data,
            device=self,
            icon=self.Icon
        ))