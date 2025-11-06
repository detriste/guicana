# Verifique um label de exemplo
with open(r'C:\Users\Usuário\Desktop\hope\labels\train\fotos1.txt', 'r') as f:
    content = f.read()
    if content.strip():
        print("✅ Label tem conteúdo:")
        print(content)
    else:
        print("❌ Label está VAZIO!")