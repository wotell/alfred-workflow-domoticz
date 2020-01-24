import Const
import DomoticzDevice
import DomoticzDeviceActions
import DomoticzHelpers

class EnergyDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(EnergyDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Data(self):
        return "Today: {today}, Return: {delivery}".format(today=self._info["CounterToday"],delivery=self._info["CounterDelivToday"])

    def addActions(self):
        super(EnergyDomoticzDevice, self).addActions()
        self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
            title="Usage", 
            subtitle=self._info["Usage"],
            device=self,
            icon=self.Icon
        ))
