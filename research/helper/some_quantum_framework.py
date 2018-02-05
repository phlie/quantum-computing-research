# This helper file is going to be an easier way of writing out Q-Code, kind of
# like a Quantum Computing Framework.

from qiskit import QuantumProgram, QISKitError, RegisterSizeError
import math
import get_nth_qubit as gnq  # The helper function used in the Quantum Decoding

class SomeFramework:
    """A Quantum Computing Framework"""
    backend = 'local_qasm_simulator'

    def __init__(self, number_of_qubits=0, circuit_name='some_circuit', shots=1024, loops=1):
        """The initial setup of the Quantum Program"""
        self.number_of_qubits = number_of_qubits
        self.shots = shots
        self.circuit_name = circuit_name
        self.loops = loops
        self.generate_layout_of_circuit()
        self.setup_quantum_program()

    def generate_layout_of_circuit(self):
        """Creates the arrangement of the quantum circuit"""
        self.circuit_layout = {
        'circuits': [{
            'name': self.circuit_name,
            'quantum_registers': [{
                'name': 'qr',
                'size': self.number_of_qubits
            }],
            'classical_registers': [{
                'name': 'cr',
                'size': self.number_of_qubits
            }]}],
        }

    def setup_quantum_program(self):
        """Setups the Quantum Circuit for a given program."""
        print("Setting up quantum program...")
        self.qp = QuantumProgram(specs=self.circuit_layout)
        self.qc = self.qp.get_circuit(self.circuit_name)
        
        self.qr = self.qp.get_quantum_register('qr')
        self.cr = self.qp.get_classical_register('cr')
        print("Quantum Circuit '", self.circuit_name, " compossed of ", self.number_of_qubits, " Qubits and the same Classical Registers, setup!!!")

    def quantum_gates(self):
        """Used to setup the quantum circuit's gates"""
        print("Implementing gates...")
        # self.qc.h(self.qr[0])
        # self.qc.h(self.qr[1])
        print("Gates implemented!")

    def setup_results(self):
        """Gets the array of results"""
        print("Getting the results...")
        for qubit in range(self.number_of_qubits):
            self.qc.measure(self.qr[qubit], self.cr[qubit])
        self.out = self.qp.execute(self.circuit_name, backend=self.backend, shots=self.shots )
        self.result = self.out.get_counts(self.circuit_name)
        if self.result != False:
            print("Got the results!!!")
        else:
            print("Error getting the results")
        return self.result

    def get_results(self):
        """Gets the individual Qubit's total amount of 1s"""
        print("Getting the amount of 1's of each Qubit...")
        output = []        # Saves the output

        # Loop through all the Qubits to get the total amount of 1's for each Qubit
        for current_qubit in range(self.number_of_qubits):  # For each Q in the circuit, loop through
            possible_results = []                # We want to initialize this to nil
            current_bit_result = 0;              # Each itteration start fresh

            # Use the helper function to get an array of possible arrangements of the classical registers
            possible_results = gnq.init_bit_find(self.number_of_qubits, current_qubit)
            # print("PR: ", possible_results)

            # For all the possible results, loop through and ...
            for r in range(len(possible_results)):
                if possible_results[r] in self.result:  # If the current possible result is in results
                    current_bit_result += self.result[possible_results[r]]  # Add to the total 1's for that Q

            # Outputs the amount of 1's from MSB to LSB for each individual Qubit
            output.insert(0, current_bit_result)
        self.total_amount_of_ones = output
        print("Got the results: ", self.total_amount_of_ones)
        return self.total_amount_of_ones

    def setup_and_run_complete_circuit(self):
        """Runs a complete quantum program"""
        self.setup_quantum_program()
        self.quantum_gates()
        self.setup_results()
        return self.get_results()

    def run_circuit(self):
        self.setup_results()
        return self.get_results()

    
    def how_many_qubits(self):
        """Returns how many Qubits there are in the circuit"""
        return self.number_of_qubits

    def insert_h_gate(self, qubit_index):
        """Makes an H-Gate where specified"""
        self.qc.h(self.qr[qubit_index])

C = SomeFramework(3, "my_circuit")

C.insert_h_gate(0)
C.insert_h_gate(1)
C.insert_h_gate(2)

C.run_circuit()

# def add_gates_to_qubits(gate_to_add, initial_qubit, end_qubit=0):
#     print("Gate: ", gate_to_add, " added to ", initial_qubit, " and ", end_qubit)


# add_gates_to_qubits('X', 1)p
# add_gates_to_qubits('X', 2, 3)
