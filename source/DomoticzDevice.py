from workflow import ICON_INFO, ICON_SWITCH, ICON_COLOR

import Const
import Debug
import DomoticzDeviceActions
import DomoticzHelpers

class DomoticzDevice(object):
    Prefix = "idx:"
    Room = None
    _info = None
    _actions = []

    def __init__(self, room, deviceInfo):
        self.Room = room
        self._info = deviceInfo
        self._actions = []

    @property
    def Idx(self):
        return self._info["idx"]

    @property
    def Data(self):
        return self._info["Data"]

    @property
    def Name(self):
        return self._info["Name"]

    @property
    def Icon(self):
        return "{icondir}/device/{typeimg}.png".format(icondir=Const.BASE_PATH_ICNS, typeimg=self._info["TypeImg"])

    @property
    def Actions(self):
        return self._actions

    def getAction(self, actionId):
        for action in self.Actions:
            if (action.Id == actionId):
                return action
        return None

    def toWorkflow(self, wf):
        wf.add_item(
            title=self.Name,
            subtitle=str(self.Data),
            icon=self.Icon,
            valid=False,
            autocomplete=DomoticzHelpers.CreateQuery(self.Room, self, None)
        )

    def actionsToWorkflow(self, wf):
        for action in self.Actions:
            action.toWorkflow(self, wf)

    def infoToWorkflow(self, wf):
        wf.add_item(
            title="Back",
            subtitle="",
            icon=Const.DomoticzIcons.General_Back,
            valid=False,
            autocomplete=DomoticzHelpers.CreateQuery(self.Room, self, None)
        )
        for info in self._info:
            Debug.write(str(info) + ": " + str(self._info[info]))
            wf.add_item(
                title=str(info),
                subtitle=str(self._info[info]),
                icon=ICON_INFO,
                valid=False
            )

    def backToRoomActionToWorkflow(self, wf):
        wf.add_item(
            title="Room",
            subtitle="Show all devices",
            icon=Const.DomoticzIcons.General_Back,
            valid=False,
            autocomplete=DomoticzHelpers.CreateQuery(self.Room, None, None)
        )

class LightDomoticzDevice(DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(LightDomoticzDevice, self).__init__(room, deviceInfo)
        self.addActions()

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

    @property
    def Icon(self):
        return Const.DomoticzIcons.Device_Light.format(power=self._Power)

    def addActions(self):
        Debug.write("Adding actions...")
        if (self.On):
            self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
                id="switchOff", 
                title="Switch Off", 
                subtitle="", 
                action=Const.DomoticzAction.Device_Light_Switch.format(idxLight=self.Idx,cmd=Const.DomoticzAction.OFF),
                notify=self._info["Name"] + " Light off",
                device=self
            ))
        else:
            self.Actions.append(DomoticzDeviceActions.DomoticzDeviceAction(
                id="switchOn", 
                title="Switch On", 
                subtitle="", 
                action=Const.DomoticzAction.Device_Light_Switch.format(idxLight=self.Idx,cmd=Const.DomoticzAction.ON),
                notify=self._info["Name"] + " Light on",
                device=self
            ))

class ColorLightDomoticzDevice(LightDomoticzDevice):
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
        

class TempDomoticzDevice(DomoticzDevice):
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

class LuxDomoticzDevice(DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(LuxDomoticzDevice, self).__init__(room, deviceInfo)

class SensorDomoticzDevice(DomoticzDevice):
    def __init__(self, room, deviceInfo):
        super(SensorDomoticzDevice, self).__init__(room, deviceInfo)

def CreateDevice(room, deviceInfo):
    devicetype = deviceInfo["Type"]

    device = None
    if (devicetype == "Color Switch"):
        device = ColorLightDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Light/Switch"):
        device = LightDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Lux"):
        device = LuxDomoticzDevice(room, deviceInfo)
    elif (devicetype == "Temp"):
        device = TempDomoticzDevice(room, deviceInfo)
    else:
        device = DomoticzDevice(room, deviceInfo)
    return device
    