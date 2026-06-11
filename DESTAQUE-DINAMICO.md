# 🎯 Usando o Destaque Dinâmico

O bloco DESTAQUE agora é **100% personalizável** e muda todo mês conforme você quiser!

---

## Como Funciona

```
VOCÊ (toda sexta ou quando quiser)
  → Edita destaque-mes.json
  → Preenche o destaque real do mês

SEXTA 11h (Claude gera relatório)
  → Lê destaque-mes.json
  → Monta bloco DESTAQUE dinamicamente
  → Publica no GitHub Pages

RESULTADO: Bloco DESTAQUE sempre alinhado com o que foi importante!
```

---

## Preenchendo o Destaque Mensal

Abra `destaque-mes.json` e preencha com o que foi realmente importante:

### Exemplo 1: Crescimento no Pipeline

```json
{
  "mes": "Junho 2026",
  "titulo": "Crescimento de 45% no Pipeline [DGS]",
  "tipo": "pipeline",
  "metricas": {
    "Maio": "500 deals",
    "Junho": "725 deals",
    "Crescimento": "+225 (+45%)"
  },
  "descricao": "Maior crescimento desde janeiro. Resultado do aumento de prospecção ativa e melhor qualidade de leads da APIX.",
  "acao_recomendada": "Manter cadência de prospecção e aumentar follow-up em fases MQL para não perder momentum"
}
```

### Exemplo 2: Campanha de E-mail Bem-Sucedida

```json
{
  "mes": "Julho 2026",
  "titulo": "Campanha de E-mail com 35% de Taxa de Clique",
  "tipo": "email",
  "metricas": {
    "Taxa Abertura": "28%",
    "Taxa Clique": "35%",
    "Contatos Gerados": "142"
  },
  "descricao": "Campanha sobre 'Engenharia de Software Agêntica' obteve 35% de taxa de clique, triplicando a média mensal.",
  "acao_recomendada": "Replicar estrutura do e-mail em outras campanhas e testar A/B com diferentes assuntos"
}
```

### Exemplo 3: Evento (APIX)

```json
{
  "mes": "Maio 2026",
  "titulo": "Evento APIX 2026 — Investimento R$ 129,4M",
  "tipo": "evento",
  "metricas": {
    "Leads Gerados": "70",
    "SQL Comercial": "51",
    "CPL": "R$ 1,85M"
  },
  "descricao": "Presença na APIX 2026 resultou em 70 leads qualificados com bom custo de aquisição.",
  "acao_recomendada": "Avaliar ROI completo do evento ao final de Q2"
}
```

---

## Campos Disponíveis

| Campo | Tipo | Obrigatório? | Exemplo |
|-------|------|-------------|---------|
| `mes` | String | ✅ Sim | "Junho 2026" |
| `titulo` | String | ✅ Sim | "Crescimento de 45% no Pipeline" |
| `tipo` | String | ⚠️ Opcional | "pipeline", "email", "media_paga", "evento", "customizado" |
| `metricas` | Object | ⚠️ Opcional | `{ "Métrica": "Valor" }` |
| `descricao` | String | ✅ Sim | Descrição detalhada do destaque |
| `acao_recomendada` | String | ⚠️ Opcional | Ação sugerida |

---

## Passo a Passo: Atualizar Destaque

1. **No GitHub:**
   - Vai pro seu repositório
   - Procura o arquivo `destaque-mes.json`
   - Clica no arquivo
   - Clica no ícone de **lápis (Edit)**

2. **Edita os dados:**
   ```json
   {
     "mes": "Seu mês",
     "titulo": "O que foi realmente importante",
     "metricas": { ... },
     "descricao": "Por quê foi importante",
     "acao_recomendada": "O que fazer próximo"
   }
   ```

3. **Clica "Commit changes"** (verde)

4. **Na próxima execução (sexta 11h):**
   - Claude lê seu destaque
   - Monta o bloco especial
   - Publica no GitHub Pages

---

## Exemplos de Destaques Mensais

### Mês com Evento
```
"titulo": "APIX 2026 — 70 leads qualificados"
```

### Mês com Crescimento
```
"titulo": "Crescimento de 45% no Pipeline [DGS]"
```

### Mês com Performance de E-mail
```
"titulo": "Campanha 'Agência Agentica' — 35% de Taxa de Clique"
```

### Mês com Deal Importante
```
"titulo": "Deal Fechado com Cielo — R$ 500k"
```

### Mês com Mudança Estratégica
```
"titulo": "Lançamento de Novo Posicionamento em Agência Agentica"
```

---

## ⚡ Dica Rápida

Se não preencher `destaque-mes.json`:
- ✅ Se tiver APIX ativo → Usa APIX como destaque
- ✅ Se não tiver → Deixa espaço vazio no relatório
- ✅ Você sempre consegue editar depois

---

## 🎯 Checklist

- [ ] Entendi como funciona o destaque dinâmico
- [ ] Sei como editar `destaque-mes.json`
- [ ] Vou preencher o destaque todo mês com o que foi realmente importante
- [ ] Pronto para automação ativa!

---

**Tudo claro?** Próximo passo: **Configurar Cowork!** 🚀
