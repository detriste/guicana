import os
import glob

base = r'C:\Users\Usuário\Desktop\hope'

# Remove todos os arquivos .cache
cache_patterns = [
    os.path.join(base, 'imagens', 'train', '*.cache'),
    os.path.join(base, 'imagens', 'val', '*.cache'),
    os.path.join(base, '*.cache'),
    os.path.join(base, 'imagens', '*.cache'),
]

print("🗑️  REMOVENDO TODOS OS CACHES...\n")

for pattern in cache_patterns:
    for cache_file in glob.glob(pattern):
        try:
            os.remove(cache_file)
            print(f"✅ Removido: {cache_file}")
        except Exception as e:
            print(f"❌ Erro ao remover {cache_file}: {e}")

# Também remove o diretório runs se existir
runs_dir = os.path.join(base, 'runs')
if os.path.exists(runs_dir):
    import shutil
    try:
        shutil.rmtree(runs_dir)
        print(f"\n✅ Removido diretório: {runs_dir}")
    except Exception as e:
        print(f"\n❌ Erro ao remover {runs_dir}: {e}")

print("\n✅ LIMPEZA CONCLUÍDA!")