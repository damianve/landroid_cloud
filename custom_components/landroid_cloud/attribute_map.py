"""Attribute map used by Landroid Cloud integration."""
from __future__ import annotations

ATTR_MAP = {
    "default": {
        "state": {
            "id": "cloud_id",
            "blade_time": "total_blade_time",
            "blade_time_current": "current_blade_time",
            "blade_work_time_reset_at": "blade_time_reset",
            "battery_voltage": "battery_voltage",
            "battery_temperature": "battery_temperature",
            "battery_charge_cycle": "total_charge_cycles",
            "battery_charge_cycle_current": "current_charge_cycles",
            "battery_charge_cycles_reset_at": "charge_cycles_reset",
            "work_time": "work_time",
            "distance": "distance",
            "updated": "last_update",
            "rssi": "rssi",
            "yaw": "yaw",
            "roll": "roll",
            "pitch": "pitch",
            "gps_latitude": "latitude",
            "gps_longitude": "longitude",
            "rain_delay": "rain_delay",
            "rain_sensor_triggered": "rain_sensor_triggered",
            "rain_delay_time_remaining": "rain_delay_remaining",
            "firmware": "firmware_version",
            "serial": "serial",
            "mac": "mac",
            "partymode_enabled": "partymode_enabled",
            "mowing_zone": "mowing_zone",
            "locked": "locked",
            "online": "online",
            "accessories": "accessories",
            "zone": "zone",
            "zone_probability": "zone_probability",
            "schedule_mower_active": "schedule_enabled",
            "schedule_variation": "time_extension",
            "schedules": "schedules",
            "error": "error_id"
        },
        "icon": "mdi:robot-mower",
    },
}
