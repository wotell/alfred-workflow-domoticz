import sys
from workflow import ICON_INFO, ICON_SWITCH, ICON_COLOR

import Const
import Debug
import DomoticzDeviceActions
import DomoticzHelpers

sys.path.append('./devices')
import DomoticzDevice
import GasDomoticzDevice
import ColorLightDomoticzDevice
import LightDomoticzDevice
import LuxDomoticzDevice
import MotionDomoticzDevice
import SwitchDomoticzDevice
import TempDomoticzDevice
import VoltageDomoticzDevice

def CreateDevice(room, deviceInfo):
    devicetype = deviceInfo["Type"]

    device = None
    if (devicetype == "Color Switch"):
        device = ColorLightDomoticzDevice.ColorLightDomoticzDevice(room, deviceInfo)
    elif (devicetype == "General"):
        if (deviceInfo["SubType"] == "Voltage"):
            device = VoltageDomoticzDevice.VoltageDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Light/Switch"):
        if (deviceInfo["SwitchType"] == "Motion Sensor"):
            device = MotionDomoticzDevice.MotionDomoticzDevice(room, deviceInfo)
        elif (deviceInfo["TypeImg"] == "lightbulb"):
            device = LightDomoticzDevice.LightDomoticzDevice(room, deviceInfo)
        else:
            device = SwitchDomoticzDevice.SwitchDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Lux"):
        device = LuxDomoticzDevice.LuxDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Temp"):
        device = TempDomoticzDevice.TempDomoticzDevice(room, deviceInfo)
    elif (deviceInfo["SubType"] == "Gas"):
        device = GasDomoticzDevice.GasDomoticzDevice(room, deviceInfo)
    
    if (device == None):
        device = DomoticzDevice.DomoticzDevice(room, deviceInfo)

    return device

def CreateQuery(room, device, action):
    result = "room"
    
    if (not device == None):
        if (not result == "" ): 
            result = result + " "
        result = result + "{prefix}{idx}".format(prefix=device.Prefix,idx=device.Idx)

    if (not action == None and not action.Id == None):
        if (not result == "" ): 
            result = result + " "
        result = result + "{prefix}{id}".format(prefix=action.Prefix,id=action.Id)

    return result