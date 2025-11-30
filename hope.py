from pathlib import Path
from collections import Counter

def debug_avancado():
    """Analisa o conteúdo real das labels e mostra estatísticas"""
    
    print("\n" + "="*70)
    print("🔍 DEBUG AVANÇADO - ANÁLISE COMPLETA")
    print("="*70)
    
    base_path = Path("C:/Users/Usuário/Desktop/hope")
    
    # Analisa labels de treino
    train_labels = list((base_path / "labels" / "train").glob("*.txt"))
    
    print(f"\n📁 Analisando {len(train_labels)} arquivos de TREINO")
    print("─"*70)
    
    contador_classes = Counter()
    total_anotacoes = 0
    arquivos_analisados = 0
    
    print("\n📄 PRIMEIROS 10 ARQUIVOS:")
    for i, label_file in enumerate(train_labels[:10]):
        with open(label_file, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
            linhas = conteudo.split('\n') if conteudo else []
            
            print(f"\n{i+1}. {label_file.name}")
            if linhas and linhas[0]:
                for linha in linhas:
                    if linha.strip():
                        print(f"   → {linha}")
                        classe = linha.split()[0]
                        try:
                            classe_num = int(classe)
                            contador_classes[classe_num] += 1
                        except:
                            print(f"   ⚠️  ERRO: '{classe}' não é um número!")
            else:
                print("   (vazio)")
    
    # Conta TODAS as anotações
    print("\n\n📊 CONTAGEM COMPLETA DE TODAS AS LABELS:")
    print("─"*70)
    
    contador_classes = Counter()
    arquivos_vazios = 0
    arquivos_com_erro = []
    
    for label_file in train_labels:
        try:
            with open(label_file, 'r', encoding='utf-8') as f:
                conteudo = f.read().strip()
                if not conteudo:
                    arquivos_vazios += 1
                    continue
                
                linhas = conteudo.split('\n')
                for linha in linhas:
                    if linha.strip():
                        partes = linha.split()
                        if partes:
                            try:
                                classe = int(partes[0])
                                contador_classes[classe] += 1
                                total_anotacoes += 1
                            except ValueError:
                                arquivos_com_erro.append(f"{label_file.name}: '{partes[0]}'")
                
                arquivos_analisados += 1
        except Exception as e:
            print(f"❌ Erro ao ler {label_file.name}: {e}")
    
    print(f"Total de arquivos: {len(train_labels)}")
    print(f"Arquivos vazios: {arquivos_vazios}")
    print(f"Arquivos analisados: {arquivos_analisados}")
    print(f"\nTotal de anotações: {total_anotacoes}")
    print(f"\nDistribuição por classe:")
    print(f"  Classe 0 (diatraea_saccharalis): {contador_classes.get(0, 0)}")
    print(f"  Classe 1 (desconhecido): {contador_classes.get(1, 0)}")
    
    if arquivos_com_erro:
        print(f"\n⚠️  ARQUIVOS COM ERRO ({len(arquivos_com_erro)}):")
        for erro in arquivos_com_erro[:5]:
            print(f"   {erro}")
    
    # Análise do problema
    print("\n" + "="*70)
    print("🎯 DIAGNÓSTICO")
    print("="*70)
    
    if contador_classes.get(0, 0) == 0:
        print("🚨 PROBLEMA CRÍTICO:")
        print("   Não existem anotações da classe 0 (diatraea_saccharalis)!")
        print("   Todas as suas imagens estão anotadas como classe 1 (desconhecido)")
        print("\n💡 SOLUÇÃO:")
        print("   1. Verifique se você anotou as imagens corretamente")
        print("   2. As imagens de diatraea_saccharalis devem ter classe '0' nas labels")
        print("   3. Reanote as imagens ou corrija as labels manualmente")
    elif contador_classes.get(1, 0) > contador_classes.get(0, 0) * 10:
        print("⚠️  DESBALANCEAMENTO EXTREMO:")
        print(f"   Classe 1: {contador_classes.get(1, 0)} anotações")
        print(f"   Classe 0: {contador_classes.get(0, 0)} anotações")
        print(f"   Proporção: {contador_classes.get(1, 0) / max(contador_classes.get(0, 0), 1):.1f}:1")
        print("\n💡 Isso pode fazer o modelo sempre prever 'desconhecido'")
    else:
        print("✅ Labels parecem estar corretas!")
        print(f"   Classe 0: {contador_classes.get(0, 0)} anotações")
        print(f"   Classe 1: {contador_classes.get(1, 0)} anotações")
        print("\n🔄 PRÓXIMO PASSO: Retreine o modelo")
    
    print("="*70)

if __name__ == "__main__":
    debug_avancado()