import streamlit as st
import matplotlib.pyplot as plt
import random

st.title("🎯 Jeu : Trouve la cible")

# Dimensions
width, height = 10, 8

# Position cible
if "target" not in st.session_state:
    st.session_state.target = (random.randint(1, width-1), random.randint(1, height-1))
    st.session_state.score = 0

# Clic simulé via sélection coordonnée
x_click = st.slider("Position X", 0, width, 0)
y_click = st.slider("Position Y", 0, height, 0)

if st.button("Tirer"):
    if (x_click, y_click) == st.session_state.target:
        st.success("🎯 Touché ! +1 point")
        st.session_state.score += 1
        st.session_state.target = (random.randint(1, width-1), random.randint(1, height-1))
    else:
        st.warning("Raté...")

# Affichage graphique
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_xticks(range(width+1))
ax.set_yticks(range(height+1))
ax.grid(True)

# Cible
ax.plot(st.session_state.target[0], st.session_state.target[1], "ro", markersize=15)
# Tir
ax.plot(x_click, y_click, "bx", markersize=10)

st.pyplot(fig)

st.write(f"Score : {st.session_state.score}")


