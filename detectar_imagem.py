import os

caches = [
    r'C:\Users\Usuário\Desktop\hope\imagens\train.cache',
    r'C:\Users\Usuário\Desktop\hope\imagens\val.cache'
]

for cache in caches:
    if os.path.exists(cache):
        os.remove(cache)
        print(f"✅ Cache removido: {cache}")