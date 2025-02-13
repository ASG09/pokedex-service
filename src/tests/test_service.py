import pytest
from src.pokeapi.client import PokeAPIClient
from src.pokeapi.storage import InMemoryStorage
from src.pokeapi.service import PokeAPIService
from typing import Any


@pytest.fixture
def client() -> PokeAPIClient:
    return PokeAPIClient()


@pytest.fixture
def storage() -> InMemoryStorage:
    return InMemoryStorage()


@pytest.fixture
def service(client: PokeAPIClient, storage: InMemoryStorage) -> PokeAPIService:
    return PokeAPIService(client, storage)


def test_get_pokemon(service: PokeAPIService, storage: InMemoryStorage) -> None:
    response = service.get_pokemon("pikachu")
    assert response is not None
    assert "name" in response
    assert response["name"] == "pikachu"


def test_pokemon_storage(service: PokeAPIService, storage: InMemoryStorage) -> None:
    service.get_pokemon("pikachu")
    pikachu_data: Any = storage.get("pokemon_pikachu")
    assert pikachu_data is not None
    assert isinstance(pikachu_data, dict)
    assert pikachu_data.get("name") == "pikachu"
    storage.clear()
    pikachu_data = storage.get("pokemon_pikachu")
    assert pikachu_data is None


def test_get_pokemon_type(service: PokeAPIService, storage: InMemoryStorage) -> None:
    response = service.get_pokemon_type("electric")
    assert response is not None
    assert "name" in response
    assert response["name"] == "electric"


def test_pokemon_type_storage(service: PokeAPIService, storage: InMemoryStorage) -> None:
    service.get_pokemon_type("electric")
    electric_data: Any = storage.get("pokemon_type_electric")
    assert electric_data is not None
    assert isinstance(electric_data, dict)
    assert electric_data.get("name") == "electric"
    storage.clear()
    electric_data = storage.get("pokemon_type_electric")
    assert electric_data is None
