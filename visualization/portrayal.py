def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",  # Bentuk agen, bisa juga "rect" (persegi)
        "Filled": "true",   # Agen akan diwarnai
        "r": 0.5,           # Radius lingkaran (hanya untuk "circle")
        "Layer": 0          # Layer rendering agen
    }

    # Tentukan warna berdasarkan status agen
    if agent.health_status == "healthy":
        portrayal["Color"] = "green"
    elif agent.health_status == "infected":
        portrayal["Color"] = "red"
    elif agent.health_status == "recovered":
        portrayal["Color"] = "blue"
    else:
        portrayal["Color"] = "gray"  # Warna default jika status tidak dikenali

    return portrayal
