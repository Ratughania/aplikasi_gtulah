import streamlit as st

st.header('Bilangan')
st.write('ini adalah aplikasi untuk menentukan bilangan genap atau ganjil')

import streamlit as st



# Number input widget
number = st.number_input("Masukkan sebuah angka")

# Display the current number
st.write("Angka yang dimasukkan:", number)

# Determine if the number is even or odd
if number % 2 == 0:
    st.write(f"Bilangan {number} adalah bilangan genap.")
else:
    st.write(f"Bilangan {number} adalah bilangan ganjil.")

