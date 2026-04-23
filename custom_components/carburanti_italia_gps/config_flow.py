import voluptuous as vol
from homeassistant import config_entries

DOMAIN = "carburanti_italia_gps"

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Carburanti GPS", data=user_input)

        schema = vol.Schema({
            vol.Required("lat"): float,
            vol.Required("lon"): float,
            vol.Required("raggio", default=10): int,
            vol.Required("fuel", default="Gasolio"): str,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
