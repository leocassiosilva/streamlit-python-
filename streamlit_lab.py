from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")
st.sidebar.image('logo.png', width=100)

st.header("Risk Prediction")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Análise Exploratória', 'Análise Comparativa','Sobre nós'], 
                         iconName=['house', 'book', 'book','person lines fill'], default_choice=0, styles = {'navtab': {'background-color':'#003781'}})

if tabs =='Home':
    st.title("Home")
    st.write('Conteudo {}'.format(tabs))

elif tabs == 'Análise Exploratória':
    st.title("Análise Exploratória")
    st.write('Conteudo {}'.format(tabs))

elif tabs == 'Análise Comparativa':
    st.title("Tom")
    st.write('Conteudo {}'.format(tabs))

elif tabs == 'Sobre nós':
    st.title("Sobre nós")
    st.write('Conteudo {}'.format(tabs))



# st.title("Simulation[tm]")
# st.write("Here is our super important simulation")

# st.sidebar.image('logo.png', width=100)
# st.sidebar.markdown("Menu")
# x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
# y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

# st.write(f"x={x} y={y}")
# values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)


# st.image('logo.png', width=100)
# st.title("Streamlit Dashboard Demo")
# bf =  pd.read_csv('./BlackFriday.csv')

# st.title("Analise de dados")

# marital_true = bf.Age.loc[bf.Marital_Status ==1].value_counts()
# marital_false = bf.Age.loc[bf.Marital_Status ==0].value_counts()

# x1 = marital_true.index
# y1 = marital_true.values

# x2 = marital_true.index
# y2 = marital_true.values

# plt.bar(x1, y1, label='Casados', width=0.4, align='edge')
# plt.bar(x2, y2, label='Não casados', width=0.4, align='edge')
# plt.legend()
# plt.title('Casados e não casados por idade')
# st.pyplot(plt)
# plt.clf()

# porc_gender = bf.Gender.value_counts(normalize=True)
# x = porc_gender.values
# plt.pie(x, labels=['Homens', 'Mulheres'], autopct='%.1f%%')
# st.pyplot(plt)
# plt.clf()

# st.title("Formulario")
# with st.form(key="include_cliente"):
#     input_name = st.text_input(label="Insira o seu nome")
#     input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
#     input_occupation = st.selectbox("Selecione sua profissão", options=["Desenvolvedor", "Musico","Desiner"])
#     input_button_submit = st.form_submit_button("Enviar dados")


