# 📊 DGS MKT Impact Report — Automação Semanal

Relatório de impacto marketing **[DGS] Novos Negócios** que atualiza automaticamente toda semana via **Cowork + Claude + GitHub**.

---

## 🎯 Como Funciona

```
TODA SEXTA 10h50min (Cowork)
   ↓
Exporta: Pipeline [DGS] + E-mail metrics
   ↓
GitHub Actions dispara automaticamente (11h)
   ↓
Claude gera o relatório HTML
   ↓
GitHub Pages publica
   ↓
Link fica live: https://seu-usuario.github.io/dgs-mkt-impact-report

TODO DIA 1º DO MÊS (Cowork)
   ↓
Exporta: Mídia Paga (mês anterior)
   ↓
Mesmo fluxo acima
```

---

## 📁 Estrutura de Arquivos

```
dgs-mkt-impact-report/
├── README.md                          # Documentação
├── generate-report.py                 # Script que gera o relatório
├── apix-data.json                     # Template APIX (você preenche)
├── data/
│   ├── pipeline.csv                   # Pipeline [DGS] (Cowork exporta)
│   ├── email-metrics.json             # E-mail metrics (Cowork exporta)
│   └── media-paga.json                # Mídia Paga (Cowork exporta)
├── .github/workflows/
│   └── generate-report.yml            # GitHub Actions (automático)
├── docs/
│   └── index.html                     # Relatório publicado
└── COWORK-SETUP.md                    # Guia Cowork
└── GITHUB-SETUP.md                    # Guia GitHub Secrets
```

---

## 🚀 Setup Rápido (5 minutos)

### 1️⃣ Criar o Repositório

```bash
# No GitHub:
# 1. Clica em "New"
# 2. Nome: dgs-mkt-impact-report
# 3. Descrição: "Relatório MKT Impact [DGS] com automação semanal"
# 4. Deixa público (GitHub Pages)
# 5. Clica "Create repository"
```

### 2️⃣ Adicionar Arquivos

Copia todos os arquivos deste guia para o repositório:
- `README.md`
- `generate-report.py`
- `apix-data.json`
- `.github/workflows/generate-report.yml`
- etc.

### 3️⃣ Adicionar Secrets

**Settings → Secrets and variables → Actions → New repository secret**

```
Nome: GITHUB_TOKEN
Valor: [seu GitHub token]

Nome: ANTHROPIC_API_KEY
Valor: [sua Anthropic API key]
```

### 4️⃣ Ativar GitHub Pages

**Settings → Pages → Source: Deploy from a branch → Branch: main**

### 5️⃣ Configurar Cowork

Ver: `COWORK-SETUP.md`

---

## 📊 O que Atualiza Automaticamente

### ✅ Toda Sexta 11h

- Pipeline [DGS] (última semana)
- E-mail Marketing (acumulado do mês)
- APIX (se você preencher `apix-data.json`)

### ✅ Todo Dia 1º às 11h

- Mídia Paga (mês anterior)
- Todas as seções acima

---

## 📝 Como Preencher APIX (Manual)

Abra `apix-data.json` e preencha quando houver evento:

```json
{
  "ativo": true,
  "evento": "APIX 2026",
  "investimento": 129360000,
  "cpl": 1848571,
  "cplq": 2537647,
  "totalLeads": 70,
  "sqlComercial": 51,
  "oportunidades": 8,
  "analise": "165 leads totais no pipeline APIX 2026..."
}
```

Salva o arquivo → GitHub atualiza o relatório automaticamente!

---

## 🔧 Como Funciona Cowork

Cowork exporta os dados toda semana:

1. **Sexta 10h50min:** Abre HubSpot → Exporta Pipeline [DGS] + E-mail
2. **Salva:** Arquivos CSV/JSON no repositório
3. **GitHub Actions:** Dispara automaticamente
4. **Claude:** Gera o HTML
5. **GitHub Pages:** Publica

Ver `COWORK-SETUP.md` para configuração detalhada.

---

## 🔐 Segurança

- ✅ Tokens guardados como **GitHub Secrets** (nunca em texto plano)
- ✅ Cowork usa **sua autenticação** (sem credenciais expostas)
- ✅ Repositório pode ser **privado** ou **público**
- ✅ Nenhum dado sensível em histórico

---

## 📋 Checklist de Setup

- [ ] Repositório criado no GitHub
- [ ] Todos os arquivos copiados
- [ ] GitHub Secrets configurados (GITHUB_TOKEN + ANTHROPIC_API_KEY)
- [ ] GitHub Pages ativado
- [ ] Cowork configurado
- [ ] Primeira execução testada
- [ ] Relatório live em GitHub Pages

---

## 🆘 Troubleshooting

**O relatório não atualiza?**
- Verifica se os Secrets estão corretos
- Verifica o log do GitHub Actions (Actions tab)
- Testa se Cowork consegue exportar dados

**Dados faltando?**
- Verifica se Cowork exportou os CSVs
- Verifica estrutura de `apix-data.json`

**GitHub Pages não funciona?**
- Settings → Pages → Branch deve ser `main`
- Verifica se tem `docs/index.html`

---

## 📞 Suporte

Dúvidas? Revisa:
- `GITHUB-SETUP.md` — Configuração GitHub
- `COWORK-SETUP.md` — Configuração Cowork
- `generate-report.py` — Código do script

---

**Criado:** junho 2026 | **Atualizado:** Toda semana automaticamente
