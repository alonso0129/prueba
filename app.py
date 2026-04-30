import streamlit as st
import random

st.set_page_config(page_title="Trivia Rock Peruano", page_icon="🎸")

st.title("🎤 Trivia: Cantantes del Rock Peruano")
st.write("Responde correctamente las 5 preguntas para ganar.")

# Banco de preguntas
questions = [
    {
        "question": "¿Quién fue el vocalista principal de Frágil?",
        "correct": "Andrés Dulude",
        "options": ["Andrés Dulude", "Miki González", "Pedro Suárez-Vértiz", "Raúl Romero"]
    },
    {
        "question": "¿Quién fue el cantante de Arena Hash?",
        "correct": "Pedro Suárez-Vértiz",
        "options": ["Pedro Suárez-Vértiz", "Jhovan Tomasevich", "Daniel F", "Pelo Madueño"]
    },
    {
        "question": "¿Quién es el vocalista de Zen?",
        "correct": "Jhovan Tomasevich",
        "options": ["Jhovan Tomasevich", "Raúl Romero", "Marcello Motta", "Miki González"]
    },
    {
        "question": "¿Quién fue el líder y vocalista de Leusemia?",
        "correct": "Daniel F",
        "options": ["Daniel F", "Pelo Madueño", "Pedro Suárez-Vértiz", "Wicho García"]
    },
    {
        "question": "¿Quién es el vocalista de Mar de Copas?",
        "correct": "Wicho García",
        "options": ["Wicho García", "Miki González", "Raúl Romero", "Andrés Dulude"]
    }
]

# Mezclar preguntas solo una vez
if "quiz" not in st.session_state:
    st.session_state.quiz = questions.copy()
    for q in st.session_state.quiz:
        random.shuffle(q["options"])

score = 0
answers = []

with st.form("quiz_form"):
    for i, q in enumerate(st.session_state.quiz):
        answer = st.radio(
            f"{i+1}. {q['question']}",
            q["options"],
            key=f"q_{i}"
        )
        answers.append(answer)

    submitted = st.form_submit_button("Ver resultado")

if submitted:
    for i, q in enumerate(st.session_state.quiz):
        if answers[i] == q["correct"]:
            score += 1

    st.subheader(f"Tu puntaje: {score}/5")

    if score == 5:
        st.success("¡Excelente! Respondiste todo correctamente 🎉")
        st.balloons()
    else:
        st.warning("Sigue intentando para conseguir el puntaje perfecto.")
