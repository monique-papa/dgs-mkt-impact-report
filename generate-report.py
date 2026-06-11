#!/usr/bin/env python3
"""
DGS MKT Impact Report Generator
Gera o relatório semanal/mensal automaticamente usando Claude API
Lê dados automáticos (pipeline, e-mail, mídia) + dados manuais (destaque, customizações)
"""

import os
import json
import csv
from datetime import datetime
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

def read_csv(filename):
    """Lê arquivo CSV e retorna dados"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def read_json(filename):
    """Lê arquivo JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def load_data():
    """Carrega todos os dados necessários"""
    data = {
        "pipeline": read_csv("data/pipeline.csv"),
        "email_metrics": read_json("data/email-metrics.json"),
        "media_paga": read_json("data/media-paga.json"),
        "destaque": read_json("destaque-mes.json"),
        "apix": read_json("apix-data.json")
    }
    return data

def generate_report_with_claude(data):
    """Gera o relatório HTML usando Claude com dados dinâmicos"""
    
    # Formata o destaque para o prompt
    destaque_info = ""
    if data['destaque'] and data['destaque'].get('mes'):
        destaque_info = f"""
DESTAQUE DO MÊS (DINÂMICO - PREENCHER TODO MÊS):
- Mês: {data['destaque'].get('mes', 'N/A')}
- Título: {data['destaque'].get('titulo', 'N/A')}
- Tipo: {data['destaque'].get('tipo', 'geral')}
- Métricas: {json.dumps(data['destaque'].get('metricas', {}), ensure_ascii=False)}
- Descrição: {data['destaque'].get('descricao', '')}
- Ação recomendada: {data['destaque'].get('acao_recomendada', '')}
"""
    
    # Prepara o prompt com os dados
    prompt = f"""
Você é um especialista em análise de marketing B2B. Seu trabalho é gerar um relatório HTML profissional e executivo.

DADOS PARA O RELATÓRIO:

1. PIPELINE [DGS]:
{json.dumps(data['pipeline'], ensure_ascii=False, indent=2)}

2. E-MAIL MARKETING (métricas acumuladas do mês):
{json.dumps(data['email_metrics'], ensure_ascii=False, indent=2)}

3. MÍDIA PAGA (Meta + LinkedIn):
{json.dumps(data['media_paga'], ensure_ascii=False, indent=2)}

{destaque_info}

4. APIX (se houver evento):
{json.dumps(data['apix'], ensure_ascii=False, indent=2)}

INSTRUÇÕES:
- Gere um relatório HTML completo e profissional
- Use o template em `/mnt/user-data/outputs/mkt-impact-dgs-maio-2026-ceo-ready.html` como referência visual
- IMPORTANTE: Se houver dados em "DESTAQUE DO MÊS", crie um bloco especial com essas informações
- O bloco DESTAQUE deve ser dinâmico e refletir exatamente o que foi preenchido
- Se NÃO houver destaque, use APIX (se ativo)
- Se nenhum dos dois, deixe um espaço para o usuário preencher
- Mantenha a estrutura: Resumo Executivo → Destaque → Pipeline → Inteligência Comercial → Marketing Performance
- Atualize as datas para hoje: {datetime.now().strftime('%d/%m/%Y')}
- Use cores: navy (#0d1b2a), gold (#e8a800), green (#1a7a45), blue (#378ADD)
- Gere HTML limpo, bem formatado, pronto para produção
- Inclua gráficos/barras visuais para dados numéricos

O relatório será publicado em GitHub Pages.

Retorne APENAS o HTML (sem explicações, sem markdown).
"""

    print("🤖 Gerando relatório com Claude...", flush=True)
    if data['destaque'] and data['destaque'].get('titulo'):
        print(f"📊 Destaque do mês: {data['destaque'].get('titulo')}", flush=True)
    
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return response.content[0].text

def save_report(html_content):
    """Salva o relatório HTML"""
    os.makedirs("docs", exist_ok=True)
    
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ Relatório salvo em docs/index.html", flush=True)

def main():
    """Função principal"""
    print("📊 DGS MKT Impact Report Generator", flush=True)
    print(f"⏰ Executado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", flush=True)
    print("-" * 50, flush=True)
    
    # Carrega dados
    print("📥 Carregando dados...", flush=True)
    data = load_data()
    
    # Valida dados
    if not data['pipeline'] and not data['email_metrics']:
        print("⚠️  Nenhum dado encontrado! Verifica se os CSVs/JSONs existem.", flush=True)
        return
    
    print(f"✅ Pipeline: {len(data['pipeline'])} deals", flush=True)
    print(f"✅ E-mail: {len(data['email_metrics'])} métricas", flush=True)
    print(f"✅ Mídia Paga: {len(data['media_paga'])} dados", flush=True)
    
    if data['destaque'] and data['destaque'].get('mes'):
        print(f"✅ Destaque: {data['destaque'].get('titulo', 'N/A')}", flush=True)
    
    # Gera relatório
    html = generate_report_with_claude(data)
    
    # Salva
    save_report(html)
    
    print("-" * 50, flush=True)
    print("✨ Relatório gerado com sucesso!", flush=True)
    print("📍 Disponível em: docs/index.html", flush=True)

if __name__ == "__main__":
    main()
