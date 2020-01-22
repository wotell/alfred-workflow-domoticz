import Const
import LightDomoticzDevice

class ColorLightDomoticzDevice(LightDomoticzDevice.LightDomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(ColorLightDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_ColorLight.format(power=self._Power)

    @property
    def Data(self):
        return self._info["Color"]

    @property
    def Name(self):
        return "{name} ({power})".format(name=self._info["Name"], power=self._Power)
