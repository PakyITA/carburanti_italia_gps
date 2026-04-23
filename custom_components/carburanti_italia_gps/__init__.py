from .api import CarburantiAPI
from .coordinator import CarburantiCoordinator

DOMAIN = "carburanti_italia_gps"

async def async_setup_entry(hass, entry):
    api = CarburantiAPI()
    coordinator = CarburantiCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True
