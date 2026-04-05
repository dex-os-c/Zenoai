# Zenoai
Ai that uses the quantum computing 

> The `index.html` file works **standalone** – all classical demos and simulated quantum animations run inside your browser.  
> The optional backend adds **real Qiskit quantum circuit execution** on slide 5.

---

## 🖥️ Running the Presentation

### 1. Without the quantum backend (quick, no installation)

Simply double‑click `index.html` or serve it with any local HTTP server:

```bash
# Using Python 3
python -m http.server 8000
# Then open http://localhost:8000
# Zeno AI – Quantum‑Accelerated Search

**Interactive presentation for NCSS.AI'26**  
*PMC Tech College – Mechatronics Engineering*

> Classical AI checks N items. Quantum AI checks √N. This demo shows how.

---

## ✨ Features

| Slide | Feature | What it does |
|-------|---------|---------------|
| 1 | Intro | Project title, team, and the core analogy |
| 2 | Quantum Computer | Explains superposition, qubits, Bloch sphere – with live Qiskit code example |
| 3 | Zeno Effect | Animated arrow that “freezes” when measured frequently (the Quantum Zeno effect) |
| 4 | Classical Search | Real grid of 100 numbers – scans one by one with timing (O(N)) |
| 5 | Quantum Search | Grover’s algorithm simulation – shows amplitude amplification and probability growth (O(√N)) |
| 6 | AI Applications | Face recognition, fraud detection, drug discovery, LLM retrieval – speedup numbers |
| 7 | Realistic Approach | Honest limitations, what works today, and roadmap to fault‑tolerant quantum AI |
| 8 | Thank You | One‑line summary, open for questions |

---

## 🚀 Run It

1. **Open `index.html`** in any browser (double‑click or serve locally).  
   All demos work instantly – no installation needed.

2. **Optional – real quantum backend** (Slide 5 uses real Qiskit circuits):  
   ```bash
   pip install flask flask-cors qiskit qiskit-aer numpy
   python quantum_backend.py
