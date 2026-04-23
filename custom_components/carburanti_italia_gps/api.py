import aiohttp

URL = "https://www.mimit.gov.it/images/exportCSV/prezzo_alle_8.csv"

class CarburantiAPI:
    async def get_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                text = await resp.text()
                return text.split("\n")
