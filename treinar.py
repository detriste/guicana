from ultralytics import YOLO

# Cria o modelo
model = YOLO('yolov8n.pt')

# Treina com cache DESABILITADO
results = model.train(
    data='data.yaml',
    epochs=1,
    imgsz=640,
    batch=16,
    cache=False,  # IMPORTANTE: desabilita cache
    workers=0,    # IMPORTANTE: força single-thread
    verbose=True
)

print("\n✅ Treinamento concluído!")
print(f"Resultados salvos em: {results.save_dir}")