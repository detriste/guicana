from ultralytics import YOLO
import numpy as np

# 🔹 Caminho do modelo YOLO
modelo_path = r"C:\Users\Usuário\Desktop\hope\runs\detect\train6\weights\best.pt"

# 🔹 Caminho da imagem que você quer testar
imagem_path = r"C:\Users\Usuário\Desktop\hope\images\train\fotos1.jpg"

print("📦 Carregando modelo YOLO...")
model = YOLO(modelo_path)
print("✅ Modelo carregado com sucesso!")

print(f"🔍 Rodando predição em: {imagem_path}")
results = model.predict(source=imagem_path, conf=0.01)

# 🔹 Pega as detecções
detections = results[0].boxes

if len(detections) > 0:
    confs = detections.conf.cpu().numpy()
    print("\n📊 Estatísticas de Confiabilidade:")
    print(f" - Total de detecções: {len(confs)}")
    print(f" - Confiança média: {np.mean(confs)*100:.2f}%")
    print(f" - Confiança máxima: {np.max(confs)*100:.2f}%")
    print(f" - Confiança mínima: {np.min(confs)*100:.2f}%")
else:
    print("\n⚠️ Nenhum objeto detectado acima do limite de confiança definido.")
