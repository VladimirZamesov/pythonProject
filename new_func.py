def get_result(user_param, d):
    for i, x in enumerate(d):
        if i == len(d) - 1:
            return d['last']
        elif user_param in x:
            return d[x]

