behaviour_mapping = {"default": "You are a helpful assistant."}


def get_behaviour(behaviour: str):
    if behaviour in behaviour_mapping:
        return behaviour_mapping[behaviour]
    else:
        return behaviour_mapping["default"]
