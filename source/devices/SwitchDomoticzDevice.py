import DomoticzDevice

class SwitchDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(SwitchDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def On(self):
        """
        [True | False] if light is on/off
        """
        return not self._info["Data"] == "Off"

    @property
    def _Power(self):
        """
        Returns string "On" or "Off", to be used to show correct items
        """
        result = ""
        if (self.On):
            result = "On"
        else:
            result = "Off"
        return result;  