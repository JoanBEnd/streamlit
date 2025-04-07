
import streamlit as st

st.write("Hola mundo, bienvenidos al curso de streamlit!")
st.write(123456)
st.write({"nombre": "joan",
          "apellido": "paredes"})

st.write([1, 2, 3, 4, 5])
st.write((1, 2, 3, 4, 5))
st.write(True)

mi_dict ={
          "nombre": "joan",
          "apellido": "paredes"
          } 

st.markdown(f"""
<div style="border: 2px solid white; padding: 10px; border-radius: 5px;">
    <h1>mostrar diccionario</h1>
            {mi_dict}
</div>
""", unsafe_allow_html=True)

#Sumar numeros de manera directa

25+15

45*15

