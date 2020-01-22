import Const
import DomoticzDevice

class TempDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(TempDomoticzDevice, self).__init__(room, deviceInfo)

    @property
    def Temp(self):
        return self._info["Temp"]

    @property
    def Icon(self):
        if (self.Temp < 0):
            return Const.DomoticzIcons.Device_TempMin
        elif (self.Temp <= 5):
            return Const.DomoticzIcons.Device_Temp_0_5
        elif (self.Temp <= 10):
            return Const.DomoticzIcons.Device_Temp_5_10
        elif (self.Temp <= 15):
            return Const.DomoticzIcons.Device_Temp_10_15
        elif (self.Temp <= 20):
            return Const.DomoticzIcons.Device_Temp_15_20
        elif (self.Temp <= 25):
            return Const.DomoticzIcons.Device_Temp_20_25
        elif (self.Temp <= 30):
            return Const.DomoticzIcons.Device_Temp_25_30
        elif (self.Temp > 30):
            return Const.DomoticzIcons.Device_TempMax
        else:
            return super.Icon
