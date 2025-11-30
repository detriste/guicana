from ultralytics import YOLO
import os
from pathlib import Path

def listar_modelos():
    """Lista todos os modelos treinados disponíveis"""
    runs_path = Path('runs/detect')

    if not runs_path.exists():
        return []

    modelos = []
    for pasta in sorted(runs_path.iterdir()):
        if pasta.is_dir() and pasta.name.startswith('train'):
            best_pt = pasta / 'weights' / 'best.pt'
            if best_pt.exists():
                try:
                    tamanho = best_pt.stat().st_size / (1024 * 1024)
                    modelos.append({
                        'pasta': pasta.name,
                        'caminho': str(best_pt),
                        'tamanho': tamanho
                    })
                except:
                    pass
    return modelos


def escolher_modelo():
    """Permite escolher qual modelo usar"""
    print("\n" + "=" * 70)
    print("🦋 DETECTOR DE LAGARTAS - ESCOLHER MODELO")
    print("=" * 70)

    modelos = listar_modelos()

    if not modelos:
        print("\n❌ Nenhum modelo treinado encontrado!")
        print("💡 Execute o treino primeiro.")
        return None

    print(f"\n📦 MODELOS DISPONÍVEIS ({len(modelos)}):")
    print("─" * 70)
    for i, modelo in enumerate(modelos, 1):
        print(f"{i}. {modelo['pasta']}")
        print(f"   📁 {modelo['caminho']}")
        print(f"   💾 Tamanho: {modelo['tamanho']:.1f} MB\n")

    while True:
        escolha = input(f"➜ Escolha um modelo (1-{len(modelos)}) ou ENTER para o primeiro: ").strip()
        if escolha == "":
            idx = 0
            break
        try:
            idx = int(escolha) - 1
            if 0 <= idx < len(modelos):
                break
        except:
            pass
        print("❌ Escolha inválida.")

    modelo_escolhido = modelos[idx]['caminho']
    print(f"\n✅ Usando modelo: {modelos[idx]['pasta']}")
    return YOLO(modelo_escolhido)


def detectar_imagem(model, caminho_imagem):
    """Realiza a detecção em uma imagem"""
    if not os.path.exists(caminho_imagem):
        print(f"❌ Arquivo não encontrado: {caminho_imagem}")
        return

    print("\n🔍 Executando predição com confiança mínima de 0.10 ...")
    results = model.predict(source=caminho_imagem, conf=0.1, verbose=False, save=True)

    for result in results:
        boxes = result.boxes
        print(f"\n{'─' * 60}")
        print(f"🔍 {len(boxes)} detecção(ões) encontradas")

        if len(boxes) == 0:
            print("❓ Nenhum objeto detectado — tente ajustar o ângulo, luz ou aumentar o treino.")
        else:
            print("\n📋 Detecções:")
            for i, box in enumerate(boxes):
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                classe = model.names[cls]
                print(f"  [{i + 1}] Classe: {classe} | Confiança: {conf:.2%}")

            # Melhor detecção
            best_idx = boxes.conf.argmax()
            cls = int(boxes[best_idx].cls[0])
            conf = float(boxes[best_idx].conf[0])
            classe = model.names[cls]

            print("\n✅ RESULTADO FINAL:")
            if classe == 'diatraea_saccharalis':
                print(f"🐛 Lagarta detectada: {classe} ({conf:.1%})")
            else:
                print(f"❓ Detectado como '{classe}' ({conf:.1%})")

        print(f"\n💾 Imagem anotada salva em: {result.save_dir}")
        print(f"{'─' * 60}\n")


def main():
    model = escolher_modelo()
    if not model:
        return

    print("\n🔍 Digite o caminho da imagem (ou ENTER para usar a imagem enviada):")
    caminho = input("➜ ").strip().strip('"').strip("'")

    if caminho == "":
        caminho = "cae17237-4633-4701-b6cf-88eea3738151.png"

    detectar_imagem(model, caminho)


if __name__ == "__main__":
    main()
