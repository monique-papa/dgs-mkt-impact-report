# 🚀 Quick Start — Implementação em 30 minutos

Guia rápido para colocar a automação em produção.

---

## ⏱️ Timeline

```
0-5min:   Criar repositório no GitHub
5-10min:  Copiar arquivos
10-15min: Adicionar Secrets
15-20min: Ativar GitHub Pages
20-30min: Configurar Cowork
```

---

## PASSO 1: Criar Repositório (5 min)

1. Va em **github.com**
2. Clica **New** (botão verde)
3. Preenche:
   - **Repository name:** `dgs-mkt-impact-report`
   - **Description:** "Relatório MKT Impact [DGS] com automação semanal"
   - **Public** (deixa assim)
   - **Add a README.md** (deixa desmarcado, vamos adicionar)
4. Clica **Create repository**

---

## PASSO 2: Adicionar Arquivos (5 min)

No repositório criado, clica **Add file → Create new file**

Cria os seguintes arquivos (pode copiar do guia de setup):

```
README.md
├── generate-report.py
├── apix-data.json
├── GITHUB-SETUP.md
├── COWORK-SETUP.md
├── GITHUB-PAGES-SETUP.md
├── .github/workflows/generate-report.yml
├── data/
│   ├── pipeline.csv
│   ├── email-metrics.json
│   └── media-paga.json
└── docs/
    └── index.html (copia do relatório HTML que criamos)
```

**Dica:** Você pode fazer upload de múltiplos arquivos de uma vez se usar um ZIP.

---

## PASSO 3: Adicionar GitHub Secrets (5 min)

1. **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**

Adiciona 2 secrets:

```
GITHUB_TOKEN = [seu GitHub token]
ANTHROPIC_API_KEY = [sua Anthropic API key]
```

---

## PASSO 4: Ativar GitHub Pages (3 min)

1. **Settings** → **Pages**
2. **Source:** `main` / `/docs`
3. **Save**

Sua URL será: `https://seu-usuario.github.io/dgs-mkt-impact-report`

---

## PASSO 5: Configurar Cowork (12 min)

1. Abre **Cowork**
2. Cria 2 workflows:
   - **Semanal** (sexta 10h50min) — Pipeline + E-mail
   - **Mensal** (dia 1º 10h50min) — Mídia Paga
3. Configure os passos conforme `COWORK-SETUP.md`

---

## ✅ Checklist Final

- [ ] Repositório criado
- [ ] Arquivos adicionados
- [ ] Secrets configurados
- [ ] GitHub Pages ativado
- [ ] Cowork workflows criados
- [ ] Primeira execução testada

---

## 🧪 Testar

1. **No Cowork:** Roda manualmente o workflow semanal
2. **No GitHub:** Verifica se o `docs/index.html` foi atualizado
3. **No navegador:** Abre `https://seu-usuario.github.io/dgs-mkt-impact-report`
4. **Se ok:** ✨ Pronto! Automação ativa!

---

## 🆘 Problemas?

| Problema | Solução |
|----------|---------|
| Secrets não funcionam | Verifica nome exato: `GITHUB_TOKEN` e `ANTHROPIC_API_KEY` |
| Cowork não exporta | Testa manualmente abrir HubSpot, verifica seletores |
| GitHub Pages não atualiza | Vai em Settings → Pages, verifica se está habilitado |
| Relatório em branco | Verifica se `data/pipeline.csv` tem dados |

---

## 📞 Suporte

- `README.md` — Documentação completa
- `COWORK-SETUP.md` — Detalhes Cowork
- `GITHUB-SETUP.md` — Detalhes GitHub

**Tudo funcionando? 🎉 Relatório automático ativo!**
