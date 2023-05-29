def online_count(data):
    return list(data.values()).count("online")

print(online_count({'Alice': 'online', 'Bob': 'offline', 'Eve': 'online'}))