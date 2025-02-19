from homeassistant.components.binary_sensor import (BinarySensorDeviceClass,
                                                    BinarySensorEntity)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .device import (DelonghiDeviceEntity)

from .const import DOMAIN


async def async_setup_entry(
        hass: HomeAssistant, entry: ConfigEntry,
        async_add_entities: AddEntitiesCallback):
    delongh_device = hass.data[DOMAIN][entry.unique_id]
    async_add_entities([
        DelongiPrimadonnaDescaleSensor(delongh_device, hass),
        DelongiPrimadonnaFilterSensor(delongh_device, hass),
    ])
    return True


class DelongiPrimadonnaDescaleSensor(DelonghiDeviceEntity, BinarySensorEntity):
    """
    Shows if the device needs descaling
    """
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_name = 'Descaling'

    @property
    def native_value(self):
        return self.device.service

    @property
    def is_on(self) -> bool:
        return False  # bool((self.device.service >> 3) % 2)

    @property
    def icon(self):
        result = 'mdi:dishwasher'
        # if self.is_on():
        #     result = 'mdi:dishwasher-alert'
        return result


class DelongiPrimadonnaFilterSensor(
        DelonghiDeviceEntity,
        BinarySensorEntity):
    """
    Shows if the filter need to be changed
    """
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_name = 'Filter'

    @property
    def native_value(self):
        return self.device.service

    @property
    def is_on(self) -> bool:
        return False  # bool((self.device.service >> 4) % 2)

    @property
    def icon(self):
        result = 'mdi:filter'
        # if self.is_on():
        #     result = 'mdi:filter-off'
        return result
