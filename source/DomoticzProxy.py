import json
import urllib2
import base64

import Const
import Debug
import DomoticzDevice
import DomoticzHelpers
import DomoticzRoom
import DomoticzStatus

class DomoticzProxy:
    _baseUrl = ""
    _authorization = ""

    def getRoom(self, idxRoom):
        roomDevicesReply = self._get("{baseurl}{action}".format(baseurl=self._baseUrl, action=Const.DomoticzAction.Room_ListDevices.format(idxRoom=idxRoom)))
        statusDevicesReply = self._get("{baseurl}{action}".format(baseurl=self._baseUrl, action=Const.DomoticzAction.Device_ListDevices.format(idxRoom=idxRoom)))

        room = DomoticzRoom.DomoticzRoom()
        room.parse(roomDevicesReply, statusDevicesReply)
        return room

    def getStatus(self):
        """
        Get Domoticz-status
        """
        url = "{baseurl}{action}".format(baseurl=self._baseUrl, action=Const.DomoticzAction.General_Status)
        reply = self._get(url)
        status = DomoticzStatus.DomoticzStatus()
        status.parse(reply)
        return status

    def getDevice(self, deviceIdx):
        url = "{baseurl}{action}".format(baseurl=self._baseUrl, action=Const.DomoticzAction.Device_Status.format(idx=deviceIdx))
        reply = self._get(url)
        return DomoticzHelpers.CreateDevice(None, reply["result"][0])

    def getAction(self, action):
        url = "{baseurl}{action}".format(baseurl=self._baseUrl, action=action)
        reply = self._get(url)
        return (reply["status"] == "OK")

    def _get(self, url):
        Debug.write("Get " + url)
        request = urllib2.Request(url, headers={"Authorization" : self._authorization})
        return json.loads(urllib2.urlopen(request).read())

    def __init__(self, serverPort, username, password):
        self._baseUrl = Const.BASE_URL.format(username=username,password=password,serverPort=serverPort)
        self._authorization = "Basic " + base64.b64encode(username + ":" + password)