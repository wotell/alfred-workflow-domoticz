import Const

def write(message):
    if (not Const.WORKFLOW_MODE):
        print message
