import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Nutricional", page_icon="🍎", layout="wide")

st.title("🍎 Calculadora Clínica - Nutrição")
st.write("Insira os dados do paciente abaixo para calcular as métricas.")

st.divider()

# Criando colunas para organizar o formulário
col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox("Gênero", ["Feminino", "Masculino"])
    idade = st.number_input("Idade (anos)", min_value=1, max_value=120, value=30, step=1)
    
    # NOVO: Nível de Atividade Física (Fator NAF)
    atividade = st.selectbox("Nível de Atividade Física (NAF)", [
        "Sedentário (1,2)", 
        "Pouca (1,375)", 
        "Moderada (1,55)", 
        "Intensa (1,725)", 
        "Muito intensa (1,9)"
    ])

with col2:
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    altura_cm = st.number_input("Altura (cm)", min_value=50, max_value=250, value=170, step=1)

st.divider()

# Botão para executar os cálculos
if st.button("Calcular Resultados", type="primary"):
    
    # 1. Cálculo do IMC
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)
    
    classificacao_imc = ""
    if imc < 18.5: classificacao_imc = "Abaixo do peso"
    elif imc < 24.9: classificacao_imc = "Peso normal"
    elif imc < 29.9: classificacao_imc = "Sobrepeso"
    else: classificacao_imc = "Obesidade"

    # 2. Cálculo da TMB (Harris-Benedict)
    if genero == "Masculino":
        tmb = 66.5 + (13.75 * peso) + (5.0 * altura_cm) - (6.77 * idade)
    else:
        tmb = 655.1 + (9.56 * peso) + (1.85 * altura_cm) - (4.68 * idade)

    # 3. Cálculo do Gasto Energético Base (GEB)
    fatores_naf = {
        "Sedentário (1,2)": 1.2,
        "Pouca (1,375)": 1.375,
        "Moderada (1,55)": 1.55,
        "Intensa (1,725)": 1.725,
        "Muito intensa (1,9)": 1.9
    }
    
    # Busca o número correspondente à opção que ela selecionou
    fator_escolhido = fatores_naf[atividade] 
    get = tmb * fator_escolhido

    # Exibindo os resultados
    st.subheader("Resultados do Paciente")
    
    # Agora temos 3 colunas de resultados
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(label="IMC", value=f"{imc:.2f}", delta=classificacao_imc, delta_color="off")
        
    with res_col2:
        st.metric(label="Taxa Metabólica Basal", value=f"{tmb:.0f} kcal")
        
    with res_col3:
        st.metric(label="Gasto Energético Total", value=f"{get:.0f} kcal", delta="TMB x NAF", delta_color="off")
        
    st.success("Cálculos realizados com sucesso!")

