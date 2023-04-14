# файл dicts.py
def get_val(collection, key, default='git'):
    if key in collection:
        return collection[key]
    else:
        return default


data = {"vcs": "mercurial"}


print(get_val(data, "vcs"))
print(get_val(data, "vcs", "git"))
print(get_val({}, "vcs", "bazaar"))


