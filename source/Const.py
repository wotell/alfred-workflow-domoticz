import os

WORKFLOW_MODE = True
if "domoticz_cmdlinemode" in os.environ:
    WORKFLOW_MODE = False
BASE_WORKFLOW_FOLDER = os.path.dirname(__file__)
BASE_API_URL = "http://{serverPort}/json.htm".format(serverPort=os.environ['domoticz_address'])
BASE_WEB_URL = "http://{serverPort}/".format(serverPort=os.environ['domoticz_address'])
BASE_PATH_ICNS = "{folder}/resources/icns".format(folder=BASE_WORKFLOW_FOLDER)

class DomoticzAction:
    ON = "On"
    OFF = "Off"

    General_Status = "?type=command&param=getversion"
    Room_ListDevices = "?type=command&param=getplandevices&idx={idxRoom}"
    Device_Status = "?type=devices&rid={idx}"
    Device_ListDevices = "?type=devices&filter=all&used=true&order=Name"
    Device_Light_Switch = "?type=command&param=switchlight&idx={idxLight}&switchcmd={cmd}"

class DomoticzIcons:
    General_Back = "{basepath}/back.png".format(basepath=BASE_PATH_ICNS)
    Device_ColorLight = "{basepath}/device/RGB48_{power}.png".format(basepath=BASE_PATH_ICNS,power="{power}")
    Device_Current = "{basepath}/device/current.png".format(basepath=BASE_PATH_ICNS)
    Device_Gas = "{basepath}/device/gas.png".format(basepath=BASE_PATH_ICNS)
    Device_Light = "{basepath}/device/lightbulb-{power}.png".format(basepath=BASE_PATH_ICNS,power="{power}")
    Device_Motion = "{basepath}/device/motion-{power}.png".format(basepath=BASE_PATH_ICNS,power="{power}")
    Device_TempMin = "{basepath}/device/ice.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_0_5 = "{basepath}/device/temp-0-5.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_5_10 = "{basepath}/device/temp-5-10.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_10_15 = "{basepath}/device/temp-10-15.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_15_20 = "{basepath}/device/temp-15-20.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_20_25 = "{basepath}/device/temp-20-25.png".format(basepath=BASE_PATH_ICNS)
    Device_Temp_25_30 = "{basepath}/device/temp-25-30.png".format(basepath=BASE_PATH_ICNS)
    Device_TempMax = "{basepath}/device/temp-gt-30.png".format(basepath=BASE_PATH_ICNS)