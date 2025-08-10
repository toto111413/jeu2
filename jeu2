import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.title("🎯 Jeu : Clique sur la cible")

# Dimensions du jeu
canvas_width = 400
canvas_height = 300

# Position aléatoire de la cible
if "target_x" not in st.session_state:
    st.session_state.target_x = random.randint(20, canvas_width - 20)
    st.session_state.target_y = random.randint(20, canvas_height - 20)
    st.session_state.score = 0

# Affichage du canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 0, 0, 1)",
    stroke_width=1,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=canvas_height,
    width=canvas_width,
    drawing_mode="transform",  # Permet le clic
    key="canvas",
)

# Détection des clics
if canvas_result.json_data is not None and len(canvas_result.json_data["objects"]) > 0:
    click = canvas_result.json_data["objects"][-1]
    x, y = click["left"], click["top"]

    # Si clic proche de la cible → point
    if abs(x - st.session_state.target_x) < 20 and abs(y - st.session_state.target_y) < 20:
        st.session_state.score += 1
        st.session_state.target_x = random.randint(20, canvas_width - 20)
        st.session_state.target_y = random.randint(20, canvas_height - 20)
        st.success("🎯 Touché !")

# Affichage du score
st.write(f"Score : {st.session_state.score}")

# Petit rappel pour l’installer
st.caption("⚠️ Pour Streamlit Cloud : ajoutez 'streamlit-drawable-canvas' dans requirements.txt")

