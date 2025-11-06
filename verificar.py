import os

# Verifique os labels de validação
labels_val = r'C:\Users\Usuário\Desktop\hope\labels\val'

print("=== VERIFICANDO LABELS DE VALIDAÇÃO ===\n")

txt_files = [f for f in os.listdir(labels_val) if f.endswith('.txt') and f != 'classes.txt']

for txt in txt_files[:5]:  # Verifica os 5 primeiros
    filepath = os.path.join(labels_val, txt)
    with open(filepath, 'r') as f:
        content = f.read()
        
    print(f"📄 {txt}:")
    if content.strip():
        print(f"   ✅ Conteúdo: {content[:100]}")  # Primeiros 100 caracteres
    else:
        print(f"   ❌ VAZIO!")
    print()

# Conte quantos estão vazios
empty_count = 0
total_count = len(txt_files)

for txt in txt_files:
    filepath = os.path.join(labels_val, txt)
    with open(filepath, 'r') as f:
        if not f.read().strip():
            empty_count += 1

print(f"\n📊 Resumo:")
print(f"   Total de labels: {total_count}")
print(f"   Labels vazios: {empty_count}")
print(f"   Labels com anotações: {total_count - empty_count}")

