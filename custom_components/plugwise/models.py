"""Models for the Plugwise integration."""
from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_MOTION,
    BinarySensorEntityDescription,
)
from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    SensorEntityDescription,
)
from homeassistant.components.switch import DEVICE_CLASS_OUTLET, SwitchEntityDescription
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    ENERGY_KILO_WATT_HOUR,
    ILLUMINANCE,
    POWER_WATT,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    TIME_MILLISECONDS,
)
from homeassistant.helpers.entity import EntityDescription
from homeassistant.components.humidifier.const import ATTR_HUMIDITY

from .const import (
    BATTERY,
    CURRENT_TEMP,
    DEVICE_STATE,
    DHW_COMF_MODE,
    DHW_STATE,
    EL_CONSUMED,
    EL_CONSUMED_INTERVAL,
    EL_CONSUMED_OFF_PEAK_CUMULATIVE,
    EL_CONSUMED_OFF_PEAK_INTERVAL,
    EL_CONSUMED_OFF_PEAK_POINT,
    EL_CONSUMED_PEAK_CUMULATIVE,
    EL_CONSUMED_PEAK_INTERVAL,
    EL_CONSUMED_PEAK_POINT,
    EL_CONSUMED_POINT,
    EL_PRODUCED,
    EL_PRODUCED_INTERVAL,
    EL_PRODUCED_OFF_PEAK_CUMULATIVE,
    EL_PRODUCED_OFF_PEAK_INTERVAL,
    EL_PRODUCED_OFF_PEAK_POINT,
    EL_PRODUCED_PEAK_CUMULATIVE,
    EL_PRODUCED_PEAK_INTERVAL,
    EL_PRODUCED_PEAK_POINT,
    EL_PRODUCED_POINT,
    FLAME_STATE,
    GAS_CONSUMED_CUMULATIVE,
    GAS_CONSUMED_INTERVAL,
    HUMIDITY,
    INTENDED_BOILER_TEMP,
    LOCK,
    MOD_LEVEL,
    NET_EL_CUMULATIVE,
    NET_EL_POINT,
    OUTDOOR_TEMP,
    RELAY,
    RETURN_TEMP,
    SMILE,
    SLAVE_BOILER_STATE,
    STICK,
    TARGET_TEMP,
    TEMP_DIFF,
    USB_MOTION_ID,
    USB_RELAY_ID,
    VALVE_POS,
    WATER_PRESSURE,
    WATER_TEMP,
)


@dataclass
class PlugwiseRequiredKeysMixin:
    """Mixin for required keys."""

    state_request_method: str
    plugwise_api: str


@dataclass
class PlugwiseEntityDescription(EntityDescription, PlugwiseRequiredKeysMixin):
    """Generic Plugwise entity description."""


@dataclass
class PlugwiseSensorEntityDescription(
    SensorEntityDescription, PlugwiseEntityDescription
):
    """Describes Plugwise sensor entity."""

    should_poll: bool = False


@dataclass
class PlugwiseSwitchEntityDescription(
    SwitchEntityDescription, PlugwiseEntityDescription
):
    """Describes Plugwise switch entity."""

    should_poll: bool = False


@dataclass
class PlugwiseBinarySensorEntityDescription(
    BinarySensorEntityDescription, PlugwiseEntityDescription
):
    """Describes Plugwise binary sensor entity."""

    should_poll: bool = False


PW_SENSOR_TYPES: tuple[PlugwiseSensorEntityDescription, ...] = (
    PlugwiseSensorEntityDescription(
        key="power_1s",
        plugwise_api=STICK,
        name="Power usage",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        state_request_method="current_power_usage",
    ),
    PlugwiseSensorEntityDescription(
        key="energy_consumption_today",
        plugwise_api=STICK,
        name="Energy consumption today",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="energy_consumption_today",
    ),
    PlugwiseSensorEntityDescription(
        key="ping",
        plugwise_api=STICK,
        name="Ping roundtrip",
        icon="mdi:speedometer",
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TIME_MILLISECONDS,
        state_request_method="ping",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_8s",
        plugwise_api=STICK,
        name="Power usage 8 seconds",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        state_request_method="current_power_usage_8_sec",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="RSSI_in",
        plugwise_api=STICK,
        name="Inbound RSSI",
        device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        state_request_method="rssi_in",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="RSSI_out",
        plugwise_api=STICK,
        name="Outbound RSSI",
        device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        state_request_method="rssi_out",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_con_cur_hour",
        plugwise_api=STICK,
        name="Power consumption current hour",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="power_consumption_current_hour",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_prod_cur_hour",
        plugwise_api=STICK,
        name="Power production current hour",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="power_production_current_hour",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_con_today",
        plugwise_api=STICK,
        name="Power consumption today",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="power_consumption_today",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_con_prev_hour",
        plugwise_api=STICK,
        name="Power consumption previous hour",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="power_consumption_previous_hour",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key="power_con_yesterday",
        plugwise_api=STICK,
        name="Power consumption yesterday",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        state_request_method="power_consumption_yesterday",
        entity_registry_enabled_default=False,
    ),
    PlugwiseSensorEntityDescription(
        key=BATTERY,
        plugwise_api=SMILE,
        name="Battery",
        device_class=DEVICE_CLASS_BATTERY,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=PERCENTAGE,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=CURRENT_TEMP,
        plugwise_api=SMILE,
        name="Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=DEVICE_STATE,
        plugwise_api=SMILE,
        state_class=STATE_CLASS_MEASUREMENT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED,
        plugwise_api=SMILE,
        name="Electricity Consumed",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Consumed Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_OFF_PEAK_CUMULATIVE,
        plugwise_api=SMILE,
        name="Electricity Consumed Off Peak Cumulative",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_OFF_PEAK_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Consumed Off Peak Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_OFF_PEAK_POINT,
        plugwise_api=SMILE,
        name="Electricity Consumed Off Peak Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_PEAK_CUMULATIVE,
        plugwise_api=SMILE,
        name="Electricity Consumed Peak Cumulative",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_PEAK_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Consumed Peak Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_PEAK_POINT,
        plugwise_api=SMILE,
        name="Electricity Consumed Peak Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_CONSUMED_POINT,
        plugwise_api=SMILE,
        name="Electricity Consumed Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED,
        plugwise_api=SMILE,
        name="Electricity Produced",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Produced Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_OFF_PEAK_CUMULATIVE,
        plugwise_api=SMILE,
        name="Electricity Produced Off Peak Cumulative",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_OFF_PEAK_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Produced Off Peak Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_OFF_PEAK_POINT,
        plugwise_api=SMILE,
        name="Electricity Produced Off Peak Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_PEAK_CUMULATIVE,
        plugwise_api=SMILE,
        name="Electricity Produced Peak Cumulative",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_PEAK_INTERVAL,
        plugwise_api=SMILE,
        name="Electricity Produced Peak Interval",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_PEAK_POINT,
        plugwise_api=SMILE,
        name="Electricity Produced Peak Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=EL_PRODUCED_POINT,
        plugwise_api=SMILE,
        name="Electricity Produced Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=GAS_CONSUMED_CUMULATIVE,
        plugwise_api=SMILE,
        name="Gas Consumed Cumulative",
        device_class=DEVICE_CLASS_GAS,
        state_class=STATE_CLASS_TOTAL_INCREASING,
        native_unit_of_measurement=VOLUME_CUBIC_METERS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=GAS_CONSUMED_INTERVAL,
        plugwise_api=SMILE,
        name="Gas Consumed Interval",
        device_class=DEVICE_CLASS_GAS,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=VOLUME_CUBIC_METERS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=HUMIDITY,
        plugwise_api=SMILE,
        name="Relative Humidity",
        device_class=DEVICE_CLASS_HUMIDITY,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=PERCENTAGE,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=ILLUMINANCE,
        plugwise_api=SMILE,
        name="Relative Humidity",
        device_class=DEVICE_CLASS_ILLUMINANCE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=UNIT_LUMEN,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=INTENDED_BOILER_TEMP,
        plugwise_api=SMILE,
        name="Intended Boiler Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=MOD_LEVEL,
        plugwise_api=SMILE,
        name="Modulation Level",
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=PERCENTAGE,
        icon="mdi:percent",
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=NET_EL_CUMULATIVE,
        plugwise_api=SMILE,
        name="Net Electricity Cumulative",
        device_class=DEVICE_CLASS_ENERGY,
        state_class=STATE_CLASS_TOTAL,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=NET_EL_POINT,
        plugwise_api=SMILE,
        name="Net Electricity Point",
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=POWER_WATT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=OUTDOOR_TEMP,
        plugwise_api=SMILE,
        name="Outdoor Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=RETURN_TEMP,
        plugwise_api=SMILE,
        name="Return Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=TARGET_TEMP,
        plugwise_api=SMILE,
        name="Setpoint",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=TEMP_DIFF,
        plugwise_api=SMILE,
        name="Temperature Difference",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_KELVIN,
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=VALVE_POS,
        plugwise_api=SMILE,
        name="Valve Position",
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=PERCENTAGE,
        icon="mdi:valve",
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=WATER_PRESSURE,
        plugwise_api=SMILE,
        name="Water Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        state_class=STATE_CLASS_MEASUREMENT,
        should_poll=True,
    ),
    PlugwiseSensorEntityDescription(
        key=WATER_TEMP,
        plugwise_api=SMILE,
        name="Water Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        native_unit_of_measurement=TEMP_CELSIUS,
        should_poll=True,
    ),
)

PW_SWITCH_TYPES: tuple[PlugwiseSwitchEntityDescription, ...] = (
    PlugwiseSwitchEntityDescription(
        key=USB_RELAY_ID,
        plugwise_api=STICK,
        device_class=DEVICE_CLASS_OUTLET,
        name="Relay state",
        state_request_method="relay_state",
    ),
    PlugwiseSwitchEntityDescription(
        key=DHW_COMF_MODE,
        plugwise_api=SMILE,
        device_class=DEVICE_CLASS_SWITCH,
        name="DHW Comfort Mode",
        should_poll=True,
    ),
    PlugwiseSwitchEntityDescription(
        key=LOCK,
        plugwise_api=SMILE,
        device_class=DEVICE_CLASS_SWITCH,
        name="Lock",
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseSwitchEntityDescription(
        key=RELAY,
        plugwise_api=SMILE,
        device_class=DEVICE_CLASS_SWITCH,
        should_poll=True,
    ),
)

PW_BINARY_SENSOR_TYPES: tuple[PlugwiseBinarySensorEntityDescription, ...] = (
    PlugwiseBinarySensorEntityDescription(
        key=USB_MOTION_ID,
        plugwise_api=STICK,
        name="Motion",
        device_class=DEVICE_CLASS_MOTION,
        state_request_method="motion",
    ),
    PlugwiseBinarySensorEntityDescription(
        key=DHW_STATE,
        plugwise_api=SMILE,
        name="DHW State",
        should_poll=True,
    ),
    PlugwiseBinarySensorEntityDescription(
        key=FLAME_STATE,
        plugwise_api=SMILE,
        name="Flame State",
        should_poll=True,
    ),
    PlugwiseBinarySensorEntityDescription(
        key=PW_NOTIFICATION,
        plugwise_api=SMILE,
        name="Plugwise Notification",
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
    PlugwiseBinarySensorEntityDescription(
        key=SLAVE_BOILER_STATE,
        plugwise_api=SMILE,
        name="Slave Boiler State",
        entity_registry_enabled_default=False,
        should_poll=True,
    ),
)
