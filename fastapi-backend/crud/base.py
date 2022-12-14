Store = [
    {
        "id": "1",
        "name": "Store 1",
        "description": "Store 1 description",
        "address": "Store 1 address",
        "city": "Store 1 city",
        "state": "Store 1 state",
        "zipcode": "Store 1 zipcode",
    }
]


def create():
    return {"message": "Item Created"}


from config.redis_config import redis_client as RC


def create_record(record_key: str, record: dict) -> None:
    """
    Set the values in the Redis database using the keys and values from the
    specified dictionary and assign the dictionary to the specified key.

    :param record_key: The key to use for the dictionary
    :param record: The dictionary containing the keys and values to store in
                   the Redis database

    :RC is the redis client
    """
    RC.hmset(record_key, record)
