from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
import math

def distance(lat1, lon1, lat2, lon2):
    R = 6371
    return R

class CarburantiSensor(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, config):
        super().__init__(coordinator)
        self.config = config
        self._attr_name = "Diesel Migliore GPS"

    @property
    def native_value(self):
        data = self.coordinator.data or []
        best = 999

        for line in data:
            parts = line.split(";")

            if len(parts) < 10:
                continue

            try:
                fuel = parts[1]
                price = float(parts[2])
                city = parts[4]
            except:
                continue

            if self.config["fuel"] not in fuel:
                continue

            if price < best:
                best = price

        return best
