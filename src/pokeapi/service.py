from src.pokeapi.client import PokeAPIClient
from src.pokeapi.storage import InMemoryStorage
from typing import Any, Optional


class PokeAPIService:
    def __init__(self, client: PokeAPIClient, storage: InMemoryStorage) -> None:
        self.client = client
        self.storage = storage

    def get_pokemon(self, name_or_id: str) -> Optional[dict[str, Any]]:
        """Fetch Pokemon details and cache result."""
        cache_key = f"pokemon_{name_or_id}"
        cached = self.storage.get(cache_key)
        if cached:
            return cached

        response_data = self.client.get(f"pokemon/{name_or_id}")
        if response_data:
            self.storage.set(cache_key, response_data)
        return response_data

    def get_pokemon_type(self, type_name: str) -> Optional[dict[str, Any]]:
        """Fetch Pokemon type details and cache result."""
        cache_key = f"type_{type_name}"
        cached = self.storage.get(cache_key)
        if cached:
            return cached

        response_data = self.client.get(f"type/{type_name}")
        if response_data:
            self.storage.set(cache_key, response_data)
        return response_data
