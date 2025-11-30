from ultralytics import YOLO
import torch
import gc

def treino_leve():
    """Treino otimizado para não travar"""
    
    print("\n" + "="*70)
    print("🚀 TREINO LEVE E ESTÁVEL")
    print("="*70)
    
    # Limpa memória
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    # Verifica GPU
    print("\n🖥️  INFORMAÇÕES DO SISTEMA:")
    print(f"  GPU disponível: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  Memória GPU: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
    
    # Configurações LEVES
    print("\n⚙️  CONFIGURAÇÕES OTIMIZADAS:")
    print("  • Batch: 8 (reduzido, usa menos memória)")
    print("  • Workers: 4 (reduzido)")
    print("  • Imgsz: 416 (menor, mais rápido)")
    print("  • Cache: False (economia de RAM)")
    print("  • Device: 0 se GPU, cpu se não tiver")
    
    model = YOLO('yolo11n.pt')
    
    # Detecta device
    device = '0' if torch.cuda.is_available() else 'cpu'
    print(f"  • Usando: {device}")
    
    print("\n⏱️  Iniciando treino...")
    print("─"*70)
    
    try:
        results = model.train(
            data='data.yaml',
            
            # Configurações leves
            epochs=500,
            imgsz=416,          # Menor = mais leve
            batch=8,            # Reduzido
            workers=4,          # Reduzido
            device=device,
            cache=False,        # Não cachear (economiza RAM)
            
            # Paciência
            patience=25,
            
            # Augmentation moderado
            hsv_h=0.01,
            hsv_s=0.5,
            hsv_v=0.3,
            degrees=10,
            translate=0.1,
            scale=0.3,
            flipud=0.5,
            fliplr=0.5,
            mosaic=0.8,         # Reduzido
            mixup=0.1,          # Reduzido
            
            # Otimização
            optimizer='AdamW',
            lr0=0.001,
            lrf=0.01,
            warmup_epochs=2,
            
            # Salvar frequentemente
            save=True,
            save_period=10,     # Salva a cada 10 epochs
            plots=True,
            verbose=True,
            
            # Evitar travamento
            amp=False,          # Desativa mixed precision (mais estável)
            rect=False,         # Desativa rect training
            single_cls=False
        )
        
        print("\n✅ TREINO COMPLETO!")
        print(f"📊 Modelo salvo em: runs/detect/train/weights/best.pt")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  TREINO INTERROMPIDO PELO USUÁRIO!")
        print("💾 Progresso salvo automaticamente")
        
    except Exception as e:
        print(f"\n\n❌ ERRO DURANTE O TREINO:")
        print(f"   {type(e).__name__}: {e}")
        print("\n💡 SOLUÇÕES:")
        print("   1. Reduza o batch ainda mais (tente batch=4)")
        print("   2. Reduza o imgsz (tente imgsz=320)")
        print("   3. Use device='cpu' se a GPU estiver dando problema")
        print("   4. Verifique se há imagens corrompidas no dataset")
    
    finally:
        # Limpa memória
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

if __name__ == "__main__":
    treino_leve()