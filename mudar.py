import os
from pathlib import Path

def renomear_imagens_para_labels(pasta_imagens, pasta_labels):
    """Renomeia imagens para corresponder aos labels existentes"""
    
    # Lista todos os labels (exceto classes.txt)
    labels = sorted([f for f in os.listdir(pasta_labels) 
                     if f.endswith('.txt') and f != 'classes.txt'])
    
    # Lista todas as imagens
    imagens = sorted([f for f in os.listdir(pasta_imagens) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    print(f"\n{'='*60}")
    print(f"Pasta: {pasta_imagens}")
    print(f"Labels encontrados: {len(labels)}")
    print(f"Imagens encontradas: {len(imagens)}")
    print(f"{'='*60}\n")
    
    if len(labels) != len(imagens):
        print(f"⚠️  AVISO: Quantidade diferente!")
        print(f"   Labels: {len(labels)}")
        print(f"   Imagens: {len(imagens)}")
        resposta = input("\nContinuar mesmo assim? (s/n): ")
        if resposta.lower() != 's':
            return
    
    # Renomeia as imagens
    for i, (img, lbl) in enumerate(zip(imagens, labels)):
        # Pega a extensão da imagem original
        ext = os.path.splitext(img)[1]
        
        # Nome do label sem .txt
        novo_nome = os.path.splitext(lbl)[0] + ext
        
        caminho_antigo = os.path.join(pasta_imagens, img)
        caminho_novo = os.path.join(pasta_imagens, novo_nome)
        
        # Se já tem o nome correto, pula
        if caminho_antigo == caminho_novo:
            print(f"   ✓ {img} (já correto)")
            continue
        
        # Renomeia
        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"   ✅ {img} → {novo_nome}")
        except Exception as e:
            print(f"   ❌ Erro ao renomear {img}: {e}")
    
    print(f"\n{'='*60}")
    print("✅ Renomeação concluída!")
    print(f"{'='*60}\n")

# Caminhos
base = r'C:\Users\Usuário\Desktop\hope'

# Renomeia TRAIN
print("\n🔄 RENOMEANDO TRAIN...")
renomear_imagens_para_labels(
    os.path.join(base, 'imagens', 'train'),
    os.path.join(base, 'labels', 'train')
)

# Renomeia VAL
print("\n🔄 RENOMEANDO VAL...")
renomear_imagens_para_labels(
    os.path.join(base, 'imagens', 'val'),
    os.path.join(base, 'labels', 'val')
)

print("\n✅ TODAS AS IMAGENS RENOMEADAS!")
print("\nAgora execute:")
print("1. python detectar_imagem.py  (para limpar caches)")
print("2. python treinar.py  (para treinar o modelo)")