from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import clamp, listens
from ableton.v2.control_surface import ParameterInfo
from ableton.v2.control_surface.components import DeviceComponent as DeviceComponentBase



#Custom device component, allows parameters to automap, need this because DeviceComponent is abstract class

class DeviceComponent(DeviceComponentBase):
    __events__ = (u'bank',)

    def __init__(self, *a, **k):
        super(DeviceComponent, self).__init__(*a, **k)
        self.__on_bank_changed.subject = self._device_bank_registry

    def _set_device(self, device):
        super(DeviceComponent, self)._set_device(device)

    def _create_parameter_info(self, parameter, name):
        return ParameterInfo(parameter=parameter, name=name, default_encoder_sensitivity=1.0)