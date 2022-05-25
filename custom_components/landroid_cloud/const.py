"""Constants used by Landroid Cloud integration."""
from __future__ import annotations

from homeassistant.components.vacuum import (
    STATE_DOCKED,
    STATE_RETURNING,
)

from pyworxcloud.clouds import CLOUDS as api_clouds

# Startup banner
STARTUP = """
-------------------------------------------------------------------
Landroid Cloud integration

Version: %s
This is a custom integration
If you have any issues with this you need to open an issue here:
https://github.com/mtrab/landroid_cloud/issues
-------------------------------------------------------------------
"""

# Some defaults
DEFAULT_NAME = "landroid"
DOMAIN = "landroid_cloud"
PLATFORM = "vacuum"
UPDATE_SIGNAL = "landroid_cloud_update"

# Service consts
SERVICE_POLL = "poll"
SERVICE_CONFIG = "config"
SERVICE_PARTYMODE = "partymode"
SERVICE_SETZONE = "setzone"
SERVICE_LOCK = "lock"
SERVICE_RESTART = "restart"
SERVICE_EDGECUT = "edgecut"
SERVICE_OTS = "ots"

# Extra states
STATE_INITIALIZING = "Initializing"
STATE_OFFLINE = "Offline"
STATE_RAINDELAY = "Rain delay"

# Attributes
ATTR_MULTIZONE_DISTANCES = "multizone_distances"
ATTR_MULTIZONE_PROBABILITIES = "multizone_probabilities"
ATTR_RAINDELAY = "raindelay"
ATTR_TIMEEXTENSION = "timeextension"
ATTR_ZONE = "zone"
ATTR_BOUNDARY = "boundary"
ATTR_RUNTIME = "runtime"

# Available cloud vendors
CLOUDS = []
for cloud in api_clouds:
    CLOUDS.append(cloud.capitalize())

LANDROID_TO_HA_STATEMAP = {
    "home": STATE_DOCKED,
    "going home": STATE_RETURNING,
}
