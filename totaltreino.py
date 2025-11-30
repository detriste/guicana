from ultralytics import YOLO
import torch
import gc

def treino_leve():
    """Treino leve, rápido e estável para PCs comuns"""
    
    print("\n" + "="*70)
    print("🚀 TREINO LEVE E OTIMIZADO")
    print("="*70)
    
    # -----------------------------------------
    # 🔄 Limpeza de memória
    # -----------------------------------------
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    # -----------------------------------------
    # 🖥️  Informações do sistema
    # -----------------------------------------
    print("\n🖥️  INFORMAÇÕES DO SISTEMA:")
    gpu_ok = torch.cuda.is_available()
    print(f"  GPU disponível: {gpu_ok}")
    
    if gpu_ok:
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  Memória GPU: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
    
    # Detecta o melhor device
    device = '0' if gpu_ok else 'cpu'
    
    # -----------------------------------------
    # ⚙️  Configurações do treino
    # -----------------------------------------
    print("\n⚙️  CONFIGURAÇÕES USADAS:")
    print("  • Epochs: 80")
    print("  • Image size: 384")
    print("  • Batch size: 4")
    print("  • Workers: 2")
    print("  • Cache: True")
    print("  • Otimizador: AdamW")
    print("  • Cosine LR: Ativado")
    print(f"  • Device: {device}")
    
    # -----------------------------------------
    # 📦 Carrega modelo
    # -----------------------------------------
    model = YOLO('yolo11n.pt')
    
    print("\n⏱️  Iniciando treino...")
    print("─"*70)
    
    try:
        results = model.train(
            data='data.yaml',

            # -----------------------------------------
            # 🟢 CONFIGURAÇÕES LEVES E OTIMIZADAS
            # -----------------------------------------
            epochs=500,
            imgsz=384,
            batch=4,
            workers=2,
            device=device,
            cache=True,
            optimizer="AdamW",
            cos_lr=True,

            # -----------------------------------------
            # 🎯 Early stopping
            # -----------------------------------------
            patience=25,

            # -----------------------------------------
            # 🎨 Data Augmentation moderado
            # -----------------------------------------
            hsv_h=0.01,
            hsv_s=0.5,
            hsv_v=0.3,
            degrees=10,
            translate=0.1,
            scale=0.3,
            flipud=0.5,
            fliplr=0.5,
            mosaic=0.8,
            mixup=0.1,

            # -----------------------------------------
            # 🔧 Hiperparâmetros
            # -----------------------------------------
            lr0=0.001,
            lrf=0.01,
            warmup_epochs=2,

            # -----------------------------------------
            # 💾 Salvamento e logs
            # -----------------------------------------
            save=True,
            save_period=10,
            plots=True,
            verbose=True,

            # -----------------------------------------
            # 🔒 Evitar travamentos
            # -----------------------------------------
            amp=False,
            rect=False,
            single_cls=False
        )
        
        print("\n\n✅ TREINO COMPLETO!")
        print(f"📊 Modelo salvo em: runs/detect/train/weights/best.pt")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Treino interrompido pelo usuário.")
        print("💾 Progresso salvo automaticamente.")

    except Exception as e:
        print("\n\n❌ ERRO DURANTE O TREINO:")
        print(f"   {type(e).__name__}: {e}")
        print("\n💡 Sugestões:")
        print("   1. Reduza batch para 2")
        print("   2. Reduza imgsz para 320")
        print("   3. Use device='cpu' se a GPU estiver com problema")
        print("   4. Verifique imagens corrompidas")

    finally:
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

if __name__ == "__main__":
    treino_leve()
