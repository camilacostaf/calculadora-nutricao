import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora Nutricional", page_icon="🍎")

st.title("🍎 Calculadora Clínica - Nutrição")
st.write("Insira os dados do paciente abaixo para calcular as métricas automaticamente.")

st.divider() # Linha para separar as seções

# Criando colunas para organizar o formulário
col1, col2 = st.columns(2)

with col1:
    genero = st.selectbox("Gênero", ["Feminino", "Masculino"])
    idade = st.number_input("Idade (anos)", min_value=1, max_value=120, value=30, step=1)

with col2:
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    # Aqui a altura entra em cm para facilitar a fórmula de Harris-Benedict
    altura_cm = st.number_input("Altura (cm)", min_value=50, max_value=250, value=170, step=1)

st.divider()

# Botão para executar os cálculos
if st.button("Calcular Resultados", type="primary"):
    
    # 1. Cálculo do IMC (precisa converter altura para metros)
    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)
    
    # Classificação básica do IMC
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

    # Exibindo os resultados na tela de forma elegante
    st.subheader("Resultados do Paciente")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric(label="IMC", value=f"{imc:.2f}", delta=classificacao_imc, delta_color="off")
        
    with res_col2:
        st.metric(label="Taxa Metabólica Basal (TMB)", value=f"{tmb:.0f} kcal")
        

    st.success("Cálculos realizados com sucesso!")
