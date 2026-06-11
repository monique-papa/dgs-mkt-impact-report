# 🤖 Cowork Setup — Exportar Dados HubSpot

Este guia mostra como configurar **Cowork** para exportar dados automaticamente do HubSpot toda semana.

---

## 📋 O que Cowork vai fazer

**TODA SEXTA 10h50min:**
1. Abre HubSpot no navegador (sua autenticação)
2. Exporta: Pipeline [DGS] (última semana)
3. Exporta: E-mail Marketing (métricas acumuladas do mês)
4. Salva os arquivos no repositório GitHub

**TODO DIA 1º DO MÊS 10h50min:**
1. Exporta: Mídia Paga (mês anterior - Meta + LinkedIn)
2. Salva no repositório

---

## 🚀 Setup no Cowork

### 1️⃣ Criar Workflow Semanal (SEXTA 10h50min)

**No Cowork:**
- Clica em **New Workflow**
- Nome: `Export HubSpot Weekly Data`
- Descrição: "Exporta pipeline + e-mail metrics toda sexta"

### 2️⃣ Configurar Schedule

- Frequência: **Weekly (Semanal)**
- Dia: **Friday (Sexta)**
- Hora: **10:50 AM**
- Timezone: **America/Sao_Paulo** (UTC-3)

### 3️⃣ Adicionar Passos

**PASSO 1: Abrir HubSpot**
```
Action: Open Website
URL: https://app.hubspot.com
Wait for page load: Yes
```

**PASSO 2: Navegar até Pipeline [DGS]**
```
Action: Click Element
Locator: [Deals ou CRM]
Wait: 2 seconds

Action: Click Element
Locator: [Pipeline]
Wait: 2 seconds

Action: Look for element containing "741556065" or "[DGS] Novos Negócios"
```

**PASSO 3: Aplicar Filtro (Última Semana)**
```
Action: Click [Filter] button
Locator: "Filter" ou "Filtro"

Action: Add filter
Property: "Created or Updated Date"
Operator: "is between"
Value: "Last 7 days"

Action: Apply filters
```

**PASSO 4: Exportar Pipeline**
```
Action: Click [Export] ou [⋯] menu
Action: Select "Export all"
Format: CSV
File name: pipeline.csv
```

**PASSO 5: Salvar no GitHub**
```
Action: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
File path: data/pipeline.csv
Commit message: "Update pipeline data - automatic export"
```

**PASSO 6: Exportar E-mail Metrics**
```
Action: Navigate to Reports
URL: https://app.hubspot.com/reports/emails
Filter: "Campaigns containing [DGS]"
Metric type: "Sent, Opened, Clicked, Delivered, Bounce, Unsubscribed"
Period: "Current month"
Export: JSON
File name: email-metrics.json
```

**PASSO 7: Push Email Data**
```
Action: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
File path: data/email-metrics.json
Commit message: "Update email metrics - automatic export"
```

---

### 4️⃣ Criar Workflow Mensal (DIA 1º 10h50min)

**No Cowork:**
- Clica em **New Workflow**
- Nome: `Export HubSpot Monthly Data`
- Descrição: "Exporta mídia paga todo dia 1º"

**Schedule:**
- Frequência: **Monthly (Mensal)**
- Dia: **1st day (Dia 1º)**
- Hora: **10:50 AM**

**Passos:**
```
Action: Open HubSpot Ads
URL: https://app.hubspot.com/ads/

Action: Filter by platform: Meta + LinkedIn
Action: Filter by period: "Previous month"

Action: Export data
Format: JSON
File name: media-paga.json

Action: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
File path: data/media-paga.json
Commit message: "Update paid media data - automatic export"
```

---

## 🔒 Autenticação

Cowork usa **sua autenticação** do navegador:
- ✅ Seguro (sem expor credenciais)
- ✅ Você apenas autoriza Cowork uma vez
- ✅ Pronto!

---

## ✅ Checklist

- [ ] Cowork instalado
- [ ] Workflow semanal criado (sexta 10h50min)
- [ ] Workflow mensal criado (dia 1º 10h50min)
- [ ] GitHub conectado no Cowork (PAT configurado)
- [ ] Primeiro export testado manualmente
- [ ] Dados aparecendo em `data/` no repositório

---

## 🆘 Troubleshooting

**Cowork não consegue exportar?**
- Verifica se consegue abrir HubSpot manualmente
- Verifica se os localizadores (selectors) estão corretos
- Testa cada passo individualmente

**Arquivo não aparece no GitHub?**
- Verifica o log do Cowork
- Verifica se o GitHub token está correto
- Testa push manual com `git`

**E-mail metrics vindo vazio?**
- HubSpot pode não mostrar todas as campanhas
- Filtra apenas `[DGS]` nas campanhas
- Pode ser necessário exportar manualmente a primeira vez

---

**Tudo ok? Agora vai pra GitHub Settings e adiciona os Secrets!** Ver `GITHUB-SETUP.md`
