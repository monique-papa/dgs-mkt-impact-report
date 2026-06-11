# 🤖 Cowork Setup — Guia Pronto para Usar

Siga este guia passo a passo. Está tudo detalhadinho!

---

## 📋 WORKFLOW 1: SEMANAL (Sexta 10h50min)

### Passo 1: Criar Workflow

1. Abra **Cowork**
2. Clica **New Workflow** (ou + New)
3. **Nome:** `DGS - Export Pipeline & Email (Semanal)`
4. **Descrição:** "Exporta pipeline [DGS] + e-mail metrics toda sexta"

### Passo 2: Configurar Schedule

1. Clica **Schedule**
2. **Frequência:** Weekly (Semanal)
3. **Dia:** Friday (Sexta)
4. **Hora:** 10:50 AM
5. **Timezone:** America/Sao_Paulo

### Passo 3: Adicionar Passos

#### PASSO 1: Abrir HubSpot

```
Action Type: Open Website
URL: https://app.hubspot.com
Wait for page load: Yes (3 seconds)
```

#### PASSO 2: Ir para Deals

```
Action Type: Click
Element: Procura por "Deals" ou "CRM" no menu esquerdo
Wait: 2 seconds
```

#### PASSO 3: Selecionar Pipeline [DGS]

```
Action Type: Click
Element: Procura pelo pipeline "[DGS] Novos Negócios" ou "741556065"
Wait: 2 seconds
```

#### PASSO 4: Aplicar Filtro - Última Semana

```
Action Type: Click
Element: Botão "Filter" ou "Filtro"
Wait: 1 second

Action Type: Click
Element: "Add filter" ou "Adicionar filtro"

Action Type: Select
Field: "Created or Updated Date" (ou "Data de criação ou atualização")
Operator: "is between" (ou "está entre")
Value: "Last 7 days" (ou "Últimos 7 dias")

Action Type: Click
Element: "Apply" ou "Aplicar"
Wait: 2 seconds
```

#### PASSO 5: Exportar Pipeline como CSV

```
Action Type: Click
Element: Menu (⋯) ou "Export" button
Wait: 1 second

Action Type: Click
Element: "Export all" ou "Exportar tudo"

Action Type: Select
Format: CSV

Action Type: Type
Field: "Filename"
Value: "pipeline.csv"

Action Type: Click
Element: "Export" ou "Baixar"
Wait: 3 seconds
```

#### PASSO 6: Ir para E-mail Metrics

```
Action Type: Navigate
URL: https://app.hubspot.com/reports/emails

Wait: 2 seconds
```

#### PASSO 7: Filtrar por Campanhas [DGS]

```
Action Type: Click
Element: "Filter" ou "Filtro"

Action Type: Click
Element: "Add filter"

Action Type: Select
Field: "Campaign Name" (ou "Nome da Campanha")
Operator: "contains" (ou "contém")
Value: "[DGS]"

Action Type: Click
Element: "Apply"
Wait: 2 seconds
```

#### PASSO 8: Exportar E-mail Metrics

```
Action Type: Click
Element: "Export" ou "⋯ menu"

Action Type: Select
Format: CSV ou JSON

Action Type: Type
Filename: "email-metrics.csv"

Action Type: Click
Element: "Export"
Wait: 3 seconds
```

#### PASSO 9: Fazer Git Push (Pipeline)

```
Action Type: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
Local File Path: ~/Downloads/pipeline.csv
Remote File Path: data/pipeline.csv
Commit Message: "Update pipeline data - automatic export"
```

#### PASSO 10: Fazer Git Push (E-mail)

```
Action Type: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
Local File Path: ~/Downloads/email-metrics.csv
Remote File Path: data/email-metrics.json
Commit Message: "Update email metrics - automatic export"
```

---

## 📋 WORKFLOW 2: MENSAL (Dia 1º 10h50min)

### Passo 1: Criar Workflow

1. **Nome:** `DGS - Export Paid Media (Mensal)`
2. **Descrição:** "Exporta mídia paga [Meta + LinkedIn] todo dia 1º"

### Passo 2: Configurar Schedule

1. **Frequência:** Monthly (Mensal)
2. **Dia:** 1st day (Dia 1º)
3. **Hora:** 10:50 AM
4. **Timezone:** America/Sao_Paulo

### Passo 3: Adicionar Passos

#### PASSO 1: Abrir HubSpot Ads

```
Action Type: Open Website
URL: https://app.hubspot.com/ads/
Wait: 3 seconds
```

#### PASSO 2: Filtrar por Meta + LinkedIn

```
Action Type: Click
Element: "Filter" ou "Filtro"

Action Type: Select
Platform: "Meta" (Facebook + Instagram)

Action Type: Click
Element: "Add" para adicionar LinkedIn também
```

#### PASSO 3: Filtrar por Período

```
Action Type: Select
Period: "Last month" (Mês anterior)
```

#### PASSO 4: Exportar Dados

```
Action Type: Click
Element: "Export" ou "Download"

Action Type: Select
Format: CSV ou JSON

Action Type: Type
Filename: "media-paga.csv"

Action Type: Click
Element: "Export"
Wait: 3 seconds
```

#### PASSO 5: Fazer Git Push

```
Action Type: Git Push
Repository: seu-usuario/dgs-mkt-impact-report
Branch: main
Local File Path: ~/Downloads/media-paga.csv
Remote File Path: data/media-paga.json
Commit Message: "Update paid media data - automatic export"
```

---

## ✅ Checklist Final

- [ ] Workflow 1 criado (Semanal)
- [ ] Workflow 2 criado (Mensal)
- [ ] Ambos com schedules corretos
- [ ] GitHub credentials configuradas no Cowork
- [ ] Primeira execução testada manualmente

---

## 🆘 Se der erro:

**"Não encontra o elemento"**
- Os seletores podem variar de acordo com sua conta HubSpot
- Teste manualmente abrindo HubSpot e vendo exatamente qual é o nome do botão/campo

**"Git Push falha"**
- Verifica se o GitHub token está correto no Cowork
- Testa fazer push manual com git

**"Arquivo não salva corretamente"**
- Verifica se o caminho do arquivo está correto
- Testa baixar manualmente e salvar em ~/Downloads

---

**Consegue configurar os 2 workflows no Cowork?** 👍

Depois vamos testar tudo junto!
