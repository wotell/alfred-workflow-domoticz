import Const
import DomoticzDeviceActions
import SwitchDomoticzDevice

class LightDomoticzDevice(SwitchDomoticzDevice.SwitchDomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(LightDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_Light.format(power=self._Power)

    def addActions(self):
        super(LightDomoticzDevice, self).addActions()
        if (self.On):
            self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
                id="switchOff", 
                title="Switch Off", 
                subtitle="", 
                action=Const.DomoticzAction.Device_Light_Switch.format(idxLight=self.Idx,cmd=Const.DomoticzAction.OFF),
                notify=self._info["Name"] + " Light off",
                device=self,
                icon = Const.DomoticzIcons.Device_Light.format(power="Off")
            ))
        else:
            self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
                id="switchOn", 
                title="Switch On", 
                subtitle="", 
                action=Const.DomoticzAction.Device_Light_Switch.format(idxLight=self.Idx,cmd=Const.DomoticzAction.ON),
                notify=self._info["Name"] + " Light on",
                device=self,
                icon = Const.DomoticzIcons.Device_Light.format(power="On")
            ))
