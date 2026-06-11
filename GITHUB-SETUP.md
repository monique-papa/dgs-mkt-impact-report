# 🔐 GitHub Setup — Adicionar Secrets

Este guia mostra como adicionar seus tokens como **Secrets** no GitHub (seguro, não em texto plano).

\---

## 1️⃣ Ir para Settings do Repositório

```
https://github.com/seu-usuario/dgs-mkt-impact-report/settings
```

Ou:

* Abre o repositório
* Clica em **Settings** (aba no topo)
* Na esquerda, clica em **Secrets and variables → Actions**

\---

## 2️⃣ Criar Secret: GITHUB\_TOKEN

Clica em **New repository secret**

```
Nome: GITHUB\_TOKEN
Valor: 
```

Clica **Add secret**

\---

## 3️⃣ Criar Secret: ANTHROPIC\_API\_KEY

Clica em **New repository secret** novamente

```
Nome: ANTHROPIC\_API\_KEY
Valor: 
```

Clica **Add secret**

\---

## ✅ Pronto!

Os secrets agora estão salvos e seguros. GitHub Actions consegue acessá-los, mas você nunca vê expostos em texto plano.

\---

## 📍 Adicionar Mais Secrets (se necessário)

Se no futuro precisar adicionar mais secrets (ex: HubSpot API key):

1. **Settings → Secrets and variables → Actions**
2. **New repository secret**
3. Preenche Nome e Valor
4. **Add secret**

\---

## 🔒 Segurança

* ✅ Secrets são **criptografados**
* ✅ Não aparecem em logs
* ✅ Só acessíveis por GitHub Actions
* ✅ Você pode **revogar** a qualquer hora

\---

**Pronto para ativar GitHub Pages?** Ver `GITHUB-PAGES-SETUP.md`

