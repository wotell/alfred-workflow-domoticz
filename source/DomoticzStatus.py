from workflow import ICON_INFO

import Debug

class DomoticzStatus:
    _items = []

    def parse(self, reply):
        for key in reply.__iter__():
            self._items.append({"key": key, "value": reply[key]})
    
    def debug(self):    
        for item in self._items:
            Debug.write("'{key}': '{value}'".format(key=item["key"], value=item["value"]))

    def toWorkflow(self, wf):
        for item in self._items:
            wf.add_item(
                title=item["key"],
                subtitle=str(item["value"]),
                icon=ICON_INFO
            )
        
