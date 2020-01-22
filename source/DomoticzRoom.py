import Debug
import DomoticzDevice
import DomoticzHelpers

class DomoticzRoom:
    Prefix = "room"
    _devices = []

    def parse(self, roomDevicesReply, statusDevicesReply):
        """
        Parse all devices in room (roomDevicesReply). Map it together with device-status in statusDevicesReply
        """

        Debug.write("Parse room-devices")
        for roomDevice in roomDevicesReply['result']:
            self._devices.append(self._map(roomDevice, statusDevicesReply))

    def _map(self, roomDevice, statusDevicesReply):
        matchedStatusDevice = None
        for statusDevice in statusDevicesReply['result']:
            if (roomDevice['devidx'] == statusDevice['idx']):
                return DomoticzHelpers.CreateDevice(self, statusDevice)
            
    def toWorkflow(self, wf):
        for device in self._devices:
            device.toWorkflow(wf)