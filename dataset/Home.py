import streamlit as st
from PIL import Image

st.set_page_config(
  page_title="Home",
  page_icon="📊"
)

#image_path = '/Users/natha/dataset/'
image = Image.open('logoindia.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('### Fastest Delivery in Town')
st.sidebar.markdown("""___""")

st.write("# Curry Company Growth Dashboard")
st.markdown(
    """
    Growth Dashboard foi construida para acompanhar as metricas de desempenho dos Entregadores e Restaurante
    ### Como utilizar esse Growth Dashboard
    - Visão Empresa:
      - Visão Gerencial: Métricas gerais de comportamento.
      - Visão Tática: Indicadores semanais de crescimento.
      - Visão Geográfica:Insights de geolocalização.
    - Visão Restaurante:  
      - Indicadores semanais de crescimento dos restaurantes
  
   """ )
