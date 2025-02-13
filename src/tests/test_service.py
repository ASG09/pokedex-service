import pytest
from src.pokeapi.client import PokeAPIClient
from src.pokeapi.storage import InMemoryStorage
from src.pokeapi.service import PokeAPIService


@pytest.fixture
def client():
    return PokeAPIClient()


@pytest.fixture
def storage():
    return InMemoryStorage()


@pytest.fixture
def service(client, storage):
    return PokeAPIService(client, storage)


def test_get_pokemon(service, storage):
    response = service.get_pokemon("pikachu")
    assert response is not None
    assert "name" in response
    assert response["name"] == "pikachu"
    assert storage.get("pokemon_pikachu").get("name") == "pikachu"


def test_get_pokemon_type(service, storage):
    response = service.get_pokemon_type("electric")
    assert response is not None
    assert "name" in response
    assert response["name"] == "electric"
    assert storage.get("type_electric").get("name") == "electric"
