import os
import shutil

base = r'C:\Users\Usuário\Desktop\hope'

# Renomeia 'imagens' para 'images'
pasta_antiga = os.path.join(base, 'imagens')
pasta_nova = os.path.join(base, 'images')

if os.path.exists(pasta_antiga):
    os.rename(pasta_antiga, pasta_nova)
    print(f"✅ Renomeado: imagens → images")
else:
    print("❌ Pasta 'imagens' não encontrada")