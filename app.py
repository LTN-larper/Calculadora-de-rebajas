
st.title(
    "La Calculadora de Rebajas")
st.markdown("Introduce el precio y descuento del producto para calcular el precio final")

# 2. Entrada de Datos (En la barra lateral)
st.sidebar.header("Tus Datos")
descuento = st.sidebar.number_input("descuento (%)", min_value=0, max_value=100, value=60)
precio_original = st.sidebar.slider("Coste del producto ($)", 1.00, 100.0, 50.0)

# 3. Botón de Cálculo
if st.button("Calcular ahora el precio final"):
   
    # 4. Lógica Matemática
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
    # 5. Mostrar Resultado con ESTILO
    col1, col2 = st.columns(2)

    st.metric(label="El precio final es:", value=f"{precio_final:.2f} $")
    if descuento > 50.0:
            st.warning("Más del 50%")
            st.write("¡Menudo Chollo!.")
    if descuento >=20:
            st.write("Es una oferta buena")
    if descuento < 10.0:
            st.write("No vale la pena")
       
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' Precio_{final} = Precio_{original} \times \left(1 - \frac{Descuento}{100}\right)''')
