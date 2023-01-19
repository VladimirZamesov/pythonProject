def get_sector(user_param, d):
    for i, x in enumerate(d):
        return d[x] if user_param in d else d['last']

