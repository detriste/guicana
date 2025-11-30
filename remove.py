from pathlib import Path

def remover_backups():
    """Remove todos os arquivos .bak criados pelos scripts anteriores"""
    
    print("\n" + "="*70)
    print("🧹 REMOVENDO ARQUIVOS DE BACKUP")
    print("="*70)
    
    base_path = Path("C:/Users/Usuário/Desktop/hope")
    
    pastas = [
        base_path / "labels" / "train",
        base_path / "labels" / "val"
    ]
    
    total_removidos = 0
    
    for pasta in pastas:
        if not pasta.exists():
            print(f"\n⚠️  Pasta não encontrada: {pasta}")
            continue
        
        print(f"\n📁 Limpando: {pasta}")
        
        # Remove .bak
        backups = list(pasta.glob("*.bak"))
        for backup in backups:
            print(f"   ❌ Removendo: {backup.name}")
            backup.unlink()
            total_removidos += 1
        
        # Remove train.cache se existir
        cache = pasta / "train.cache"
        if cache.exists():
            print(f"   ❌ Removendo cache: {cache.name}")
            cache.unlink()
            total_removidos += 1
    
    # Remove cache da raiz também
    cache_raiz = base_path / "labels" / "train.cache"
    if cache_raiz.exists():
        print(f"\n   ❌ Removendo: {cache_raiz}")
        cache_raiz.unlink()
        total_removidos += 1
    
    print("\n" + "─"*70)
    print(f"✅ {total_removidos} arquivo(s) removido(s)")
    print("="*70)
    
    # Mostra o que sobrou
    print("\n📋 ARQUIVOS RESTANTES:")
    for pasta in pastas:
        if pasta.exists():
            arquivos = list(pasta.glob("*.txt"))
            print(f"\n{pasta}:")
            print(f"  Total: {len(arquivos)} arquivos .txt")
            if len(arquivos) <= 5:
                for arq in arquivos:
                    print(f"    • {arq.name}")
            else:
                print(f"    • {arquivos[0].name}")
                print(f"    • {arquivos[1].name}")
                print(f"    • ...")
                print(f"    • {arquivos[-1].name}")

if __name__ == "__main__":
    remover_backups()