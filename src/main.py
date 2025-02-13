if __name__ == "__main__":
    """
    This script fetches Pokémon and Pokémon type information from the PokeAPI and saves the results to JSON files.
    """
    import pathlib
    from src.pokeapi.client import PokeAPIClient
    from src.pokeapi.storage import InMemoryStorage
    from src.pokeapi.service import PokeAPIService
    import json

    client = PokeAPIClient()
    storage = InMemoryStorage()
    service = PokeAPIService(client, storage)

    parent_dir = pathlib.Path(__file__).parent.resolve()

    # Fetch Pokémon info
    pokemon = service.get_pokemon("pikachu")
    pokemon_file_name = f"{parent_dir}/results/pokemon_response.json"
    with open(pokemon_file_name, "w") as pikachu_file:
        pikachu_file.write(json.dumps(pokemon))

    # Fetch Pokémon type info
    type_info = service.get_pokemon_type("electric")

    type_info_file_name = f"{parent_dir}/results/type_info_response.json"
    with open(type_info_file_name, "w") as type_info_file:
        type_info_file.write(json.dumps(type_info))
