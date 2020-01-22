import Const
import SwitchDomoticzDevice

class MotionDomoticzDevice(SwitchDomoticzDevice.SwitchDomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(MotionDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_Motion.format(power=self._Power)
