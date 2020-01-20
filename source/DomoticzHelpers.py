def CreateQuery(room, device, action):
    result = "room"
    
    if (not device == None):
        if (not result == "" ): 
            result = result + " "
        result = result + "{prefix}{idx}".format(prefix=device.Prefix,idx=device.Idx)

    if (not action == None):
        if (not result == "" ): 
            result = result + " "
        result = result + "{prefix}{id}".format(prefix=action.Prefix,id=action.Id)

    return result