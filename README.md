# Symptom Checker Chatbot

A command-line chatbot that analyses reported symptoms in Norwegian and suggests appropriate action — from rest at home to seeking immediate care.

Built by **Hanne Emaus** — informatics student (robotics & AI) at the University of Oslo, with a background in medicine and clinical nursing.

---

## Why I built this

I wanted to combine two worlds I know well: healthcare and programming. This project is a first step toward AI tools that can bridge the gap between medical knowledge and people who need clear, accessible guidance.

The logic is rule-based (no ML model), which keeps it transparent and easy to understand — a deliberate choice for a health context where explainability matters.

---

## What it does

- Parses free-text symptom descriptions in Norwegian
- Matches against a database of 10 common symptoms
- Rates severity (1–3) and gives tailored advice
- Tracks all symptoms across a conversation session
- Produces a session summary on exit

---

## How to run

Requires Python 3.10+. No external libraries needed.

```bash
python symptom_checker.py
```

Example session:

```
Du: jeg har feber og hodepine
Bot: Jeg registrerte følgende symptomer:

  Feber [●●○]
  → Hvil, drikk mye og mål temperaturen. Over 39°C → lege.

  Hodepine [●○○]
  → Prøv paracetamol og hvile. Vedvarer → lege.

Observer symptomene nøye. Kontakt lege hvis de forverres.
Samlet alvorlighetsgrad: Moderat – observer nøye, kontakt lege ved forverring
```

---

## Project structure

```
symptom_checker.py   # Main logic + CLI interface
README.md            # This file
```

---

## Skills demonstrated

- Object-oriented Python (class with methods and state)
- Dictionary-based knowledge representation
- String processing and keyword matching
- Control flow and severity aggregation
- Norwegian-language NLP (rule-based)

---

## What's next

- [ ] Upgrade matching with fuzzy search or a small NLP model
- [ ] Add more symptoms and multi-symptom interaction rules
- [ ] Build a simple web interface with Flask or Streamlit
- [ ] Integrate with an LLM API for more natural conversation

---

## Disclaimer

This is a student learning project. It is **not** a medical device and should not be used for actual medical decisions. Always consult a qualified healthcare professional.
