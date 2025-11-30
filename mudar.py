from ultralytics import YOLO
import os
from pathlib import Path

def debug_completo():
    """Debug completo do modelo e dataset"""
    
    print("\n" + "="*70)
    print("🔍 DEBUG COMPLETO DO MODELO")
    print("="*70)
    
    # 1. Verifica o modelo
    modelo = 'runs/detect/train/weights/best.pt'
    
    if not os.path.exists(modelo):
        print("\n❌ ERRO: Modelo não encontrado!")
        print(f"   Procurando em: {os.path.abspath(modelo)}")
        return
    
    print(f"\n✅ Modelo encontrado: {modelo}")
    
    # Carrega o modelo
    model = YOLO(modelo)
    
    # 2. Informações do modelo
    print("\n" + "─"*70)
    print("📊 INFORMAÇÕES DO MODELO")
    print("─"*70)
    print(f"Classes treinadas: {model.names}")
    print(f"Número de classes: {len(model.names)}")
    
    # 3. Verifica o dataset
    print("\n" + "─"*70)
    print("📁 ESTRUTURA DO DATASET")
    print("─"*70)
    
    base_path = Path("C:/Users/Usuário/Desktop/hope")
    
    # Conta imagens
    train_images = list((base_path / "images" / "train").glob("*.jpg")) + \
                   list((base_path / "images" / "train").glob("*.png"))
    val_images = list((base_path / "images" / "val").glob("*.jpg")) + \
                 list((base_path / "images" / "val").glob("*.png"))
    
    print(f"Imagens de treino: {len(train_images)}")
    print(f"Imagens de validação: {len(val_images)}")
    
    # Conta labels
    train_labels = list((base_path / "labels" / "train").glob("*.txt"))
    val_labels = list((base_path / "labels" / "val").glob("*.txt"))
    
    print(f"Labels de treino: {len(train_labels)}")
    print(f"Labels de validação: {len(val_labels)}")
    
    # 4. Analisa as labels
    print("\n" + "─"*70)
    print("🏷️  ANÁLISE DAS LABELS (primeiros 10 arquivos)")
    print("─"*70)
    
    classe_0 = 0  # diatraea_saccharalis
    classe_1 = 0  # desconhecido
    
    print("\nLabels de treino:")
    for i, label_file in enumerate(train_labels[:10]):
        with open(label_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                classe = int(line.split()[0])
                if classe == 0:
                    classe_0 += 1
                elif classe == 1:
                    classe_1 += 1
            print(f"  {label_file.name}: {len(lines)} anotação(ões) - {lines[0].strip() if lines else 'vazio'}")
    
    # Conta todas as labels
    print(f"\n📊 Total de anotações em TREINO:")
    for label_file in train_labels:
        with open(label_file, 'r') as f:
            for line in f.readlines():
                classe = int(line.split()[0])
                if classe == 0:
                    classe_0 += 1
                elif classe == 1:
                    classe_1 += 1
    
    print(f"   Classe 0 (diatraea_saccharalis): {classe_0}")
    print(f"   Classe 1 (desconhecido): {classe_1}")
    
    if classe_0 == 0:
        print("\n⚠️  PROBLEMA ENCONTRADO: Nenhuma anotação da classe 'diatraea_saccharalis'!")
        print("   Todas as suas labels estão marcadas como classe 1 (desconhecido)")
    
    # 5. Testa uma predição
    print("\n" + "─"*70)
    print("🧪 TESTE DE PREDIÇÃO")
    print("─"*70)
    
    if train_images:
        test_img = train_images[0]
        print(f"\nTestando com: {test_img.name}")
        
        results = model.predict(
            source=str(test_img),
            conf=0.01,  # Muito baixo para pegar qualquer coisa
            verbose=False
        )
        
        for result in results:
            boxes = result.boxes
            print(f"\nDetecções encontradas: {len(boxes)}")
            
            if len(boxes) > 0:
                for i, box in enumerate(boxes):
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    coords = box.xyxy[0].tolist()
                    print(f"  [{i+1}] Classe: {model.names[cls]} ({cls}) | Confiança: {conf:.1%}")
                    print(f"      Coordenadas: {[f'{c:.1f}' for c in coords]}")
            else:
                print("  ❌ Nenhuma detecção (mesmo com confiança 0.01)")
    
    print("\n" + "="*70)
    print("✅ DEBUG COMPLETO")
    print("="*70)

if __name__ == "__main__":
    debug_completo()