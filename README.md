# 🚗 Smart Parking Kiosk System (DFA-Based)

## 📌 Overview

This project implements a **parking kiosk system** using **Python**, designed as part of a **Theory of Computation** assignment.

It demonstrates core concepts such as:

* Deterministic Finite Automata (DFA)
* Quintuple formal definition
* Regular Expressions
* Time and Space Complexity analysis

---

## ⚙️ Features

* Simulates a parking kiosk workflow
* DFA-based state transitions
* Input validation using Regular Expressions
* Modular Python implementation
* Theoretical analysis included

---

## 🧠 Theory Concepts Applied

### 1. Deterministic Finite Automaton (DFA)

The system is modeled using a DFA where:

* Each state represents a stage in the parking process
* Transitions depend on user input (e.g. entry, payment, exit)

### 2. Quintuple Representation

The DFA is formally defined as:

(Q, Σ, δ, q0, F)

* **Q**: Set of states
* **Σ**: Input alphabet
* **δ**: Transition function
* **q0**: Initial state
* **F**: Accepting states

---

### 3. Regular Expressions

Used for:

* Validating user inputs (e.g. vehicle number, ticket ID)
* Ensuring correct format before processing

---

### 4. Complexity Analysis

* **Time Complexity**: O(n) depending on input length
* **Space Complexity**: O(1) for state tracking

---

## 📁 Project Structure

```
├── parking_system.py
├── documentation.pdf
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/yourusername/smart-parking-dfa-python.git
```

2. Navigate to the folder:

```
cd smart-parking-dfa-python
```

3. Run the program:

```
python parking_system.py
```

---

## 🎯 Purpose

This project was developed to bridge **theoretical computer science concepts** with **practical implementation**, showcasing how automata theory can be applied to real-world systems.

---

## 📌 Future Improvements

* GUI interface for better usability
* Database integration
* Extended automata (NFA → DFA conversion)

---

## 👤 Author

[Your Name]

---

## 📜 License

This project is for educational purposes.
