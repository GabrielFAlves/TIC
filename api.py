import streamlit as st
import pandas as pd
import plotly.express as px

# Dados das distribuidoras
data = {
    "Distribuidora": [
        "Enel Brasil",
        "Grupo Energisa",
        "Companhia Energética de Minas Gerais (Cemig)",
        "Neoenergia (Iberdrola)",
        "Eletrobas (Centrais Elétricas Brasileiras S.A.)",
        "Light S.A",
        "OUTROS"
    ],
    "Área de Concessão": [
        "Estados de São Paulo (24 municípios), Rio de Janeiro (66 municípios) e Ceará (todo o estado)",
        "862 municípios em 10 estados",
        "Estado de Minas Gerais",
        "Bahia, Pernambuco, Rio Grande do Norte, São Paulo, Mato Grosso do Sul e Distrito Federal",
        "Atua em todo o território brasileiro na geração e transmissão de energia elétrica",
        "31 municípios no estado do Rio de Janeiro, incluindo a capital e Baixada Fluminense",
        "Outras regiões do Brasil"
    ],
    "Clientes Atendidos": [15, 8, 9, 16, 5.5, 4.3, 0],  # em milhões
    "Infraestrutura (km)": [62_000, 3_600, 3_300, 8_000, 74_000, 87_000, 0],  # em km
    "Participação de Mercado Brasileiro (%)": [8, 10, 9, 15, 5, 5, 48]
}

df = pd.DataFrame(data)

# Excluindo "OUTROS" dos dados exibidos na tabela e gráficos
df_sem_outros = df[df["Distribuidora"] != "OUTROS"]

# Título do aplicativo
st.title("Dashboard de Distribuidoras de Energia Elétrica no Brasil")

# Seção 1: Identificação de Variáveis
st.header("Identificação de Variáveis")

# Exibindo a tabela de dados (sem "OUTROS")
st.subheader("Dados das Distribuidoras")
st.dataframe(df_sem_outros)

# Gráfico de Clientes Atendidos (sem "OUTROS")
st.subheader("Gráfico de Clientes Atendidos")
fig = px.bar(df_sem_outros, x="Distribuidora", y="Clientes Atendidos",
             labels={"Clientes Atendidos": "Número de Clientes (milhões)"},
             title="Número de Clientes Atendidos por Distribuidora")
st.plotly_chart(fig)

# Seção 2: Análise Comparativa
st.header("Análise Comparativa")

# Gráfico de Infraestrutura (sem "OUTROS")
st.subheader("Gráfico de Infraestrutura (km de Rede)")
fig2 = px.bar(df_sem_outros, x="Distribuidora", y="Infraestrutura (km)",
              labels={"Infraestrutura (km)": "Extensão da Rede (km)"},
              title="Extensão da Rede de Distribuição por Distribuidora")
st.plotly_chart(fig2)

# Gráfico de Participação de Mercado (com "OUTROS")
st.subheader("Gráfico de Participação de Mercado (%)")
fig3 = px.pie(df, names="Distribuidora", values="Participação de Mercado Brasileiro (%)",
              title="Participação de Mercado das Distribuidoras")
st.plotly_chart(fig3)

# Seção 3: Identificação de Tendências e Padrões
st.header("Identificação de Tendências e Padrões")

st.write("""
Abaixo estão listadas algumas das principais distribuidoras de energia elétrica que atuam no Brasil. Para cada empresa, apresentamos informações relevantes como a área de concessão, o número de clientes atendidos, a extensão da infraestrutura utilizada e a participação no mercado brasileiro.

Esses dados permitem uma análise inicial da representatividade de cada distribuidora no cenário nacional de distribuição de energia elétrica.
""")

st.write("""
### Análise Comparativa

Através dos gráficos apresentados, é possível observar contrastes significativos entre as distribuidoras:

- **Clientes Atendidos:** A Neoenergia lidera em número de consumidores, com 16 milhões de clientes, seguida pela Enel Brasil com 15 milhões. Por outro lado, empresas como Light S.A e Eletrobras atendem uma base menor, mesmo atuando em áreas estratégicas.

- **Infraestrutura:** A Light S.A aparece com a maior extensão de rede (87 mil km), superando inclusive a Eletrobras, que tem uma atuação nacional. Isso mostra que, embora atenda menos clientes, a empresa cobre áreas extensas e densamente povoadas.

- **Participação de Mercado:** A distribuição de participação revela um mercado pulverizado, com diversos grupos de grande porte atuando nacionalmente. A categoria “Outros”, com 48% de participação, indica uma presença relevante de distribuidoras regionais de menor porte.

- **Maior Competitividade e Expansão de Infraestrutura:** A vitória da Engie no Leilão de Transmissão nº 02/2024 reflete o avanço de novos agentes e a expansão da malha elétrica. A movimentação de grandes grupos para novas áreas reforça o ambiente competitivo do setor.

- **Pressão de Custos no Mercado Cativo:** Estimativas apontam que o preço médio da energia pode subir cerca de 9% em 2025, o que pressiona as distribuidoras a buscar maior eficiência ou diversificar seus contratos de fornecimento.

- **Aceleração do Mercado Livre de Energia:** Frente ao aumento das tarifas no mercado regulado, cresce a migração de consumidores para o mercado livre, que oferece maior flexibilidade e negociação de preços.

- **Soluções Combinadas e Sustentabilidade:** A integração entre o mercado livre e a geração distribuída tem sido cada vez mais explorada, criando soluções híbridas que combinam economia e sustentabilidade. Essa abordagem pode gerar uma matriz energética mais eficiente e descentralizada.
""")

# Bibliografia
st.header("Bibliografia")
bibliografia = [
    ("Agência Nacional de Energia Elétrica (ANEEL). 'Distribuição — Agência Nacional de Energia Elétrica.'", "https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/distribuicao"),
    ("Agência Nacional de Energia Elétrica (ANEEL). 'ANEEL divulga desempenho e ranking das distribuidoras sobre fornecimento de energia em 2021.'", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2022/aneel-divulga-desempenho-e-ranking-das-distribuidoras-sobre-fornecimento-de-energia-em-2021"),
    ("Agência Nacional de Energia Elétrica (ANEEL). 'ANEEL divulga os resultados do desempenho das distribuidoras na continuidade do fornecimento de energia elétrica em 2022.'", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/aneel-divulga-os-resultados-do-desempenho-das-distribuidoras-na-continuidade-do-fornecimento-de-energia-eletrica-em-2022"),
    ("Aumento nos custos de aquisição de energia elétrica pelas distribuidoras", "https://www.infomoney.com.br/business/preco-de-energia-pelas-distribuidoras-tem-tendencia-de-aumento-diz-tr-solucoes/"),   
    ("Engie Brasil vence leilão de transmissão de energia", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2024/consorcio-engie-brasil-transmissao-vence-lote-1-do-leilao-de-transmissao-no-2-2024"),
    ("Migração de consumidores para o mercado livre de energia", "https://www.infomoney.com.br/business/mercado-livre-de-energia-tera-mais-de-10-milhoes-de-consumidores-ate-2024-diz-estudo/"),
    ("Integração entre mercado livre e geração distribuída", "https://www.revistaenergia.com.br/mercado-livre-de-energia-e-geracao-distribuida-uma-combinacao-eficiente/"),
    ("Plano Diretor de Negócios e Gestão PDNG 2021 - 2025", "https://www.gov.br/mme/pt-br/acesso-a-informacao/entidades/eletrobras-holding/institucional/PDNG20212025.pdf"),
    ("Regulamentação para fornecimento de energia elétrica a consumidores em baixa tensão", "https://www.light.com.br/Documentos%20Compartilhados/Normas-Tecnicas/RECON-BT%202024.pdf")
]

for item in bibliografia:
    st.write(f"- [{item[0]}]({item[1]})")import streamlit as st
import pandas as pd
import plotly.express as px

# Dados das distribuidoras
data = {
    "Distribuidora": [
        "Enel Brasil",
        "Grupo Energisa",
        "Companhia Energética de Minas Gerais (Cemig)",
        "Neoenergia (Iberdrola)",
        "Eletrobas (Centrais Elétricas Brasileiras S.A.)",
        "Light S.A",
        "OUTROS"
    ],
    "Área de Concessão": [
        "Estados de São Paulo (24 municípios), Rio de Janeiro (66 municípios) e Ceará (todo o estado)",
        "862 municípios em 10 estados",
        "Estado de Minas Gerais",
        "Bahia, Pernambuco, Rio Grande do Norte, São Paulo, Mato Grosso do Sul e Distrito Federal",
        "Atua em todo o território brasileiro na geração e transmissão de energia elétrica",
        "31 municípios no estado do Rio de Janeiro, incluindo a capital e Baixada Fluminense",
        "Outras regiões do Brasil"
    ],
    "Clientes Atendidos": [15, 8, 9, 16, 5.5, 4.3, 0],  # em milhões
    "Infraestrutura (km)": [62_000, 3_600, 3_300, 8_000, 74_000, 87_000, 0],  # em km
    "Participação de Mercado Brasileiro (%)": [8, 10, 9, 15, 5, 5, 48]
}

df = pd.DataFrame(data)

# Excluindo "OUTROS" dos dados exibidos na tabela e gráficos
df_sem_outros = df[df["Distribuidora"] != "OUTROS"]

# Título do aplicativo
st.title("Dashboard de Distribuidoras de Energia Elétrica no Brasil")

# Seção 1: Identificação de Variáveis
st.header("Identificação de Variáveis")

# Exibindo a tabela de dados (sem "OUTROS")
st.subheader("Dados das Distribuidoras")
st.dataframe(df_sem_outros)

# Gráfico de Clientes Atendidos (sem "OUTROS")
st.subheader("Gráfico de Clientes Atendidos")
fig = px.bar(df_sem_outros, x="Distribuidora", y="Clientes Atendidos",
             labels={"Clientes Atendidos": "Número de Clientes (milhões)"},
             title="Número de Clientes Atendidos por Distribuidora")
st.plotly_chart(fig)

# Seção 2: Análise Comparativa
st.header("Análise Comparativa")

# Gráfico de Infraestrutura (sem "OUTROS")
st.subheader("Gráfico de Infraestrutura (km de Rede)")
fig2 = px.bar(df_sem_outros, x="Distribuidora", y="Infraestrutura (km)",
              labels={"Infraestrutura (km)": "Extensão da Rede (km)"},
              title="Extensão da Rede de Distribuição por Distribuidora")
st.plotly_chart(fig2)

# Gráfico de Participação de Mercado (com "OUTROS")
st.subheader("Gráfico de Participação de Mercado (%)")
fig3 = px.pie(df, names="Distribuidora", values="Participação de Mercado Brasileiro (%)",
              title="Participação de Mercado das Distribuidoras")
st.plotly_chart(fig3)

# Seção 3: Identificação de Tendências e Padrões
st.header("Identificação de Tendências e Padrões")

st.write("""
Abaixo estão listadas algumas das principais distribuidoras de energia elétrica que atuam no Brasil. Para cada empresa, apresentamos informações relevantes como a área de concessão, o número de clientes atendidos, a extensão da infraestrutura utilizada e a participação no mercado brasileiro.

Esses dados permitem uma análise inicial da representatividade de cada distribuidora no cenário nacional de distribuição de energia elétrica.
""")

st.write("""
### Análise Comparativa

Através dos gráficos apresentados, é possível observar contrastes significativos entre as distribuidoras:

- **Clientes Atendidos:** A Neoenergia lidera em número de consumidores, com 16 milhões de clientes, seguida pela Enel Brasil com 15 milhões. Por outro lado, empresas como Light S.A e Eletrobras atendem uma base menor, mesmo atuando em áreas estratégicas.

- **Infraestrutura:** A Light S.A aparece com a maior extensão de rede (87 mil km), superando inclusive a Eletrobras, que tem uma atuação nacional. Isso mostra que, embora atenda menos clientes, a empresa cobre áreas extensas e densamente povoadas.

- **Participação de Mercado:** A distribuição de participação revela um mercado pulverizado, com diversos grupos de grande porte atuando nacionalmente. A categoria “Outros”, com 48% de participação, indica uma presença relevante de distribuidoras regionais de menor porte.

- **Maior Competitividade e Expansão de Infraestrutura:** A vitória da Engie no Leilão de Transmissão nº 02/2024 reflete o avanço de novos agentes e a expansão da malha elétrica. A movimentação de grandes grupos para novas áreas reforça o ambiente competitivo do setor.

- **Pressão de Custos no Mercado Cativo:** Estimativas apontam que o preço médio da energia pode subir cerca de 9% em 2025, o que pressiona as distribuidoras a buscar maior eficiência ou diversificar seus contratos de fornecimento.

- **Aceleração do Mercado Livre de Energia:** Frente ao aumento das tarifas no mercado regulado, cresce a migração de consumidores para o mercado livre, que oferece maior flexibilidade e negociação de preços.

- **Soluções Combinadas e Sustentabilidade:** A integração entre o mercado livre e a geração distribuída tem sido cada vez mais explorada, criando soluções híbridas que combinam economia e sustentabilidade. Essa abordagem pode gerar uma matriz energética mais eficiente e descentralizada.
""")

# Bibliografia
st.header("Bibliografia")
bibliografia = [
    ("Agência Nacional de Energia Elétrica (ANEEL). 'Distribuição — Agência Nacional de Energia Elétrica.'", "https://www.gov.br/aneel/pt-br/centrais-de-conteudos/relatorios-e-indicadores/distribuicao"),
    ("Agência Nacional de Energia Elétrica (ANEEL). 'ANEEL divulga desempenho e ranking das distribuidoras sobre fornecimento de energia em 2021.'", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2022/aneel-divulga-desempenho-e-ranking-das-distribuidoras-sobre-fornecimento-de-energia-em-2021"),
    ("Agência Nacional de Energia Elétrica (ANEEL). 'ANEEL divulga os resultados do desempenho das distribuidoras na continuidade do fornecimento de energia elétrica em 2022.'", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2023/aneel-divulga-os-resultados-do-desempenho-das-distribuidoras-na-continuidade-do-fornecimento-de-energia-eletrica-em-2022"),
    ("Aumento nos custos de aquisição de energia elétrica pelas distribuidoras", "https://www.infomoney.com.br/business/preco-de-energia-pelas-distribuidoras-tem-tendencia-de-aumento-diz-tr-solucoes/"),   
    ("Engie Brasil vence leilão de transmissão de energia", "https://www.gov.br/aneel/pt-br/assuntos/noticias/2024/consorcio-engie-brasil-transmissao-vence-lote-1-do-leilao-de-transmissao-no-2-2024"),
    ("Migração de consumidores para o mercado livre de energia", "https://www.infomoney.com.br/business/mercado-livre-de-energia-tera-mais-de-10-milhoes-de-consumidores-ate-2024-diz-estudo/"),
    ("Integração entre mercado livre e geração distribuída", "https://www.revistaenergia.com.br/mercado-livre-de-energia-e-geracao-distribuida-uma-combinacao-eficiente/"),
    ("Plano Diretor de Negócios e Gestão PDNG 2021 - 2025", "https://www.gov.br/mme/pt-br/acesso-a-informacao/entidades/eletrobras-holding/institucional/PDNG20212025.pdf"),
    ("Regulamentação para fornecimento de energia elétrica a consumidores em baixa tensão", "https://www.light.com.br/Documentos%20Compartilhados/Normas-Tecnicas/RECON-BT%202024.pdf")
]

for item in bibliografia:
    st.write(f"- [{item[0]}]({item[1]})")
