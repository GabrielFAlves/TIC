import streamlit as st
import pandas as pd
import plotly.express as px

# Dados simulados com base em relatórios reais
data = {
    "Indicador": [
        "Clientes Atendidos (milhões)",
        "Perdas de Energia (%)",
        "Investimentos em 2023 (R$ mi)",
        "Satisfação do Consumidor (IASC)",
        "DEC (horas)",
        "FEC (nº interrupções)"
    ],
    "Light S.A.": [4.3, 17.5, 1200, 55.2, 14.2, 6.3],
    "Enel Rio": [3.0, 12.8, 900, 60.7, 10.8, 5.1]
}

df = pd.DataFrame(data)

# Título
st.title("Comparativo entre Distribuidoras de Energia no RJ")
st.markdown("### Análise entre **Light S.A.** e **Enel Distribuição Rio**")

# Tabela
st.subheader("📋 Tabela Comparativa")
st.dataframe(df.set_index("Indicador"))

# Gráficos
st.subheader("📊 Gráficos Comparativos")

# Transpor para facilitar os gráficos
df_plot = df.set_index("Indicador").T.reset_index().rename(columns={"index": "Distribuidora"})

# Gráfico de barras para cada indicador
for indicador in df["Indicador"]:
    fig = px.bar(df_plot, x="Distribuidora", y=indicador,
                 title=f"{indicador} por Distribuidora",
                 text_auto=True)
    st.plotly_chart(fig)

# Análise final
st.subheader("📌 Conclusão")
st.write("""
Mesmo com áreas de atuação diferentes no estado do Rio de Janeiro, a comparação entre Light e Enel Rio mostra diferenças significativas:

- **Enel Rio** tem melhor desempenho em satisfação do cliente, menos perdas e melhores índices DEC/FEC.
- **Light S.A.** atende mais clientes, mas tem maiores perdas e piores indicadores de continuidade.
- O cenário aponta pressão competitiva indireta, com influência no mercado livre e futuras renovações de concessão.
""")

# Fontes
st.subheader("🔗 Fontes")
st.markdown("""
- [Relatórios ANEEL – Desempenho das Distribuidoras](https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/aneel-divulga-os-resultados-do-desempenho-das-distribuidoras-na-continuidade-do-fornecimento-de-energia-eletrica-em-2022)
- [Portal da Light](https://www.light.com.br/)
- [Portal da Enel Rio](https://www.enel.com.br/)
- [Consulta Pública nº 021/2023 – ANEEL](https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/aneel-abre-consulta-publica-sobre-revisao-da-concessao-da-light)
""")
