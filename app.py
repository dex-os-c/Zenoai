from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from math import pi, sqrt, asin

app = Flask(__name__)
CORS(app)

@app.route('/grover', methods=['POST'])
def grover():
    data = request.get_json()
    target = data.get('target', 73)          # 1..100
    n_qubits = 7                             # 2^7 = 128 states (covers 100)
    N = 2**n_qubits
    
    # Map target to a state index (just use the number itself, 1-indexed)
    target_state = target - 1                # 0..99
    
    # Grover iterations
    iterations = int(pi/4 * sqrt(N))
    
    # Build circuit
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))
    
    # Oracle for target_state (binary)
    binary = format(target_state, f'0{n_qubits}b')
    for i, bit in enumerate(reversed(binary)):
        if bit == '0':
            qc.x(i)
    qc.h(n_qubits-1)
    qc.mcx(list(range(n_qubits-1)), n_qubits-1)
    qc.h(n_qubits-1)
    for i, bit in enumerate(reversed(binary)):
        if bit == '0':
            qc.x(i)
    
    # Diffuser
    def diffuser(qc, n):
        qc.h(range(n))
        qc.x(range(n))
        qc.h(n-1)
        qc.mcx(list(range(n-1)), n-1)
        qc.h(n-1)
        qc.x(range(n))
        qc.h(range(n))
    
    for _ in range(iterations):
        # Re-apply oracle (same as above – simplified; in real code you'd refactor)
        # We'll just re-run the oracle lines (copy for brevity)
        binary = format(target_state, f'0{n_qubits}b')
        for i, bit in enumerate(reversed(binary)):
            if bit == '0':
                qc.x(i)
        qc.h(n_qubits-1)
        qc.mcx(list(range(n_qubits-1)), n_qubits-1)
        qc.h(n_qubits-1)
        for i, bit in enumerate(reversed(binary)):
            if bit == '0':
                qc.x(i)
        diffuser(qc, n_qubits)
    
    qc.measure(range(n_qubits), range(n_qubits))
    
    # Simulate
    backend = Aer.get_backend('qasm_simulator')
    transpiled = transpile(qc, backend)
    job = backend.run(transpiled, shots=1024)
    counts = job.result().get_counts()
    
    # Find most frequent state
    most_freq = max(counts, key=counts.get)
    found_index = int(most_freq, 2) + 1      # back to 1..100
    
    return jsonify({
        'found': found_index,
        'iterations': iterations,
        'counts': counts,
        'target': target
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
