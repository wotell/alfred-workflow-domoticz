from workflow import ICON_INFO

import Const
import Debug
import DomoticzHelpers

class DomoticzDevice(object):
    """
    Base-class for all devices.
    """
    Prefix = "idx:" # used in workflow to identify device-idx
    Room = None
    _info = None
    _actions = []

    def __init__(self, room, deviceInfo):
        self.Room = room
        self._info = deviceInfo
        self._actions = []
        self.addActions()

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
            autocomplete=DomoticzHelpers.CreateQuery(self.Room, self, None),
        )

    def actionsToWorkflow(self, wf):
        for action in self.Actions:
            action.toWorkflow(self, wf)

    def infoToWorkflow(self, wf):
        wf.add_item(
            title="Back to " + self.Name,
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
            title=u"Room   <-   " + self.Name,
            subtitle="Show all devices",
            icon=Const.DomoticzIcons.General_Back,
            valid=False,
            autocomplete=DomoticzHelpers.CreateQuery(self.Room, None, None)
        )

    def addActions(self):
        pass