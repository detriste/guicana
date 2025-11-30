from ultralytics import YOLO
from datetime import datetime
from pathlib import Path
import os

def testar_modelo(modelo_path, imagem_path):
    modelo_path = Path(modelo_path)
    imagem_path = Path(imagem_path)

    log_path = Path.cwd() / f"diagnostico_yolo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    with open(log_path, "w", encoding="utf-8") as log:
        log.write("=== DIAGNÓSTICO YOLO ===\n")
        log.write(f"Data/Hora: {datetime.now()}\n")
        log.write(f"Modelo: {modelo_path}\n")
        log.write(f"Imagem: {imagem_path}\n")
        log.write("=" * 60 + "\n\n")

        try:
            if not modelo_path.exists():
                raise FileNotFoundError(f"Modelo não encontrado: {modelo_path}")

            if not imagem_path.exists():
                raise FileNotFoundError(f"Imagem não encontrada: {imagem_path}")

            # Carregar modelo
            log.write("📦 Carregando modelo YOLO...\n")
            model = YOLO(str(modelo_path))
            log.write("✅ Modelo carregado com sucesso!\n")

            # Mostrar classes
            log.write(f"📋 Classes detectáveis: {model.names}\n\n")

            # Fazer predição
            log.write("🔍 Executando predição...\n")
            results = model.predict(source=str(imagem_path), conf=0.15, save=True)

            for result in results:
                boxes = result.boxes
                log.write(f"\n🔹 {len(boxes)} detecção(ões) encontradas\n")
                if len(boxes) == 0:
                    log.write("❌ Nenhum objeto detectado.\n")
                else:
                    for box in boxes:
                        cls = int(box.cls[0])
                        conf = float(box.conf[0])
                        label = model.names[cls]
                        log.write(f" - {label}: {conf:.1%}\n")

            log.write("\n✅ Diagnóstico concluído!\n")

        except Exception as e:
            log.write(f"\n💥 ERRO DETECTADO 💥\n{e}\n")

    print(f"\n📋 Diagnóstico salvo em: {log_path}")
    print("💡 Envie o conteúdo do log aqui para eu analisar!")

if __name__ == "__main__":
    modelo = input("Digite o caminho do modelo (.pt): ").strip().strip('"')
    imagem = input("Digite o caminho da imagem (.jpg ou .png): ").strip().strip('"')
    testar_modelo(modelo, imagem)
