import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurações da página
st.set_page_config(page_title="MotionTech Solutions", layout="wide")

# Título centralizado
st.markdown("""
    <h1 style="text-align: center; color: #2E86C1;">📌 MotionTech Solutions</h1>
    <h3 style="text-align: center; color: #566573;">Plano Estratégico 2025</h3>
    <hr>
""", unsafe_allow_html=True)

# Navegação lateral
menu = st.sidebar.radio("📂 Seções", [
    "Cenário da Empresa",
    "Objetivos Estratégicos",
    "Iniciativas, KPIs e Metas SMART",
    "Papel da TI",
    "Indicadores & Simulador"
])

# Seção 1: Cenário da Empresa
if menu == "Cenário da Empresa":
    st.header("🏢 Cenário da Empresa")
    st.info("""
    **Nome:** MotionTech Solutions  
    **Missão:** Oferecer soluções tecnológicas inovadoras que transformem negócios por meio da automação inteligente.  
    **Visão:** Ser referência na América Latina como principal empresa de tecnologia para automação inteligente até 2030.  
    **Valores:**  
    - Inovação contínua  
    - Foco no cliente  
    - Ética e transparência  
    - Colaboração  
    - Excelência operacional
    """)

# Seção 2: Objetivos Estratégicos
elif menu == "Objetivos Estratégicos":
    st.header("🎯 Objetivos Estratégicos por Perspectiva (Balanced Scorecard)")
    st.table(pd.DataFrame({
        "Perspectiva": ["Financeira", "Clientes", "Processos Internos", "Aprendizado e Inovação"],
        "Objetivos": [
            "Aumentar receita recorrente; reduzir custos operacionais",
            "Aumentar satisfação e retenção; ampliar base de clientes B2B",
            "Otimizar processos e garantir alta qualidade",
            "Fomentar inovação; desenvolver competências técnicas"
        ]
    }))

# Seção 3: Iniciativas, KPIs e Metas SMART
elif menu == "Iniciativas, KPIs e Metas SMART":
    st.header("📊 Iniciativas, KPIs e Metas SMART")
    categorias = {
        "Financeira": [
            ["Aumentar receita recorrente", "Lançar novo SaaS", "MRR", "Aumentar 35% até dez/2025"],
            ["Reduzir custos operacionais", "Automatizar processos com RPA", "Custo operacional", "Reduzir 20% até set/2025"]
        ],
        "Clientes": [
            ["Aumentar satisfação", "Sistema de atendimento com IA", "NPS", "Alcançar 75 até nov/2025"],
            ["Ampliar base B2B", "Inbound Marketing segmentado", "Novos clientes", "Aumentar 40% até dez/2025"]
        ],
        "Processos Internos": [
            ["Otimizar desenvolvimento", "Metodologia ágil (Scrum)", "Lead time", "Reduzir 25% até out/2025"],
            ["Garantir alta qualidade", "Testes automatizados", "Taxa de bugs", "Reduzir 50% até nov/2025"]
        ],
        "Aprendizado e Inovação": [
            ["Fomentar inovação", "Hackathons trimestrais", "Novas ideias", "10 ideias por trimestre"],
            ["Desenvolver competências", "Certificações internas", "% equipe certificada", "80% até dez/2025"]
        ]
    }

    for categoria, metas in categorias.items():
        st.subheader(f"🔹 {categoria}")
        df = pd.DataFrame(metas, columns=["Objetivo", "Iniciativa", "KPI", "Meta SMART"])
        st.table(df)

# Seção 4: Papel da TI
elif menu == "Papel da TI":
    st.header("💻 Papel da TI como Vantagem Competitiva")
    st.success("""
    - **Automação com RPA e IA:** Eficiência e escalabilidade operacional.  
    - **Plataforma SaaS:** Receita recorrente e valor agregado.  
    - **Atendimento com IA:** Melhora experiência e reduz churn.  
    - **Gestão Ágil (Scrum, DevOps, CI/CD):** Qualidade e velocidade de entrega.  
    - **Decisões Baseadas em Dados (BI, Analytics):** Estratégia guiada por dados.
    """)

# Seção 5: Indicadores + Simulador
elif menu == "Indicadores & Simulador":
    st.header("📈 Indicador Estratégico: Novos Clientes B2B")
    st.markdown("""
    **🎯 Objetivo:** Ampliar a base de clientes B2B  
    **🧮 Fórmula de Cálculo:** Novos contratos B2B ativos - Cancelamentos  
    **📏 Unidade de Medida:** Número absoluto  
    **📅 Frequência de Coleta:** Mensal  
    **🎯 Meta SMART:** Aumentar 40% até dez/2025  
    **📶 Limiares:**  
    - 🟢 ≥ 3,5% ao mês  
    - 🟡 2% - 3,4%  
    - 🔴 < 2%
    """)
    
    st.divider()
    
    # Simulador de Desempenho
    st.header("🧪 Simulador de Desempenho: Novos Clientes B2B")

    # Entrada meta 2024
    meta_2024 = st.number_input("Novos clientes B2B em 2024:", min_value=1, value=100)
    meta_2025 = int(meta_2024 * 1.4)
    st.markdown(f"🎯 **Meta 2025:** {meta_2025} novos clientes")

    # Entradas por mês
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    dados = {mes: st.number_input(f"Novos clientes em {mes}:", min_value=0) for mes in meses}

    # Cálculo progresso
    df = pd.DataFrame.from_dict(dados, orient='index', columns=['Clientes'])
    df['Acumulado'] = df['Clientes'].cumsum()
    df['% da Meta'] = (df['Acumulado'] / meta_2025 * 100).round(1)

    # Cores
    def cor(valor): return 'green' if valor >= 40 else 'orange' if valor >= 20 else 'red'
    cores = df['% da Meta'].apply(cor)

    # Gráfico de progresso
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df.index, df['% da Meta'], color=cores)
    ax.axhline(40, color='blue', linestyle='--', label='Meta 40%')
    ax.set_ylabel('% da Meta')
    ax.set_title('Desempenho Acumulado - Clientes B2B')
    ax.legend()
    st.pyplot(fig)

    # Status final
    status_final = df['% da Meta'].iloc[-1]
    if status_final >= 40:
        st.success(f"🟢 Excelente! {status_final}% da meta alcançada.")
    elif status_final >= 20:
        st.warning(f"🟠 Atenção! {status_final}% da meta alcançada.")
    else:
        st.error(f"🔴 Crítico! {status_final}% da meta alcançada.")
