import DomoticzDevice

class LuxDomoticzDevice(DomoticzDevice.DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(LuxDomoticzDevice, self).__init__(room, deviceInfo)
