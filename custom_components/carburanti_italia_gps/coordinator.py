from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

class CarburantiCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, api):
        super().__init__(hass, None, name="carburanti", update_interval=timedelta(hours=1))
        self.api = api

    async def _async_update_data(self):
        return await self.api.get_data()
