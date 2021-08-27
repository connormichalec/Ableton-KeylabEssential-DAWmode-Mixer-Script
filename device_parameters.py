from __future__ import absolute_import, print_function, unicode_literals

from ableton.v2.control_surface.components import DisplayingDeviceParameterComponent as DeviceParameterComponentBase

#i dont think i had to make this but idfk

class DeviceParameterComponent(DeviceParameterComponentBase):
    def __init__(self, *a, **k):
        super(DeviceParameterComponent, self).__init__(*a, **k)