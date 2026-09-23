import json

tallennus_data = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("save.json", "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)