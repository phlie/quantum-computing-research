# This helper file is going to be an easier way of writing out Q-Code, kind of
# like a Quantum Computing Framework.

from qiskit import QuantumProgram, QISKitError, RegisterSizeError
import math
import helper.get_nth_qubit as gnq  # The helper function used in the Quantum Decoding
import helper.bit_decoder as bd

class SomeFramework:
    """A Quantum Computing Framework"""
    backend = 'local_qasm_simulator'

    def __init__(self, number_of_qubits=1, circuit_name='some_circuit', shots=1024):
        """The initial setup of the Quantum Program"""
        self.number_of_qubits = number_of_qubits  # Used to store the amount of Qubits in a circuit
        self.shots = shots                        # The amount of possibilities of 1's and 0's
        self.circuit_name = circuit_name          # The circuit name
        self.generate_layout_of_circuit()
        self.setup_quantum_program()

#=============================
# QUANTUM CIRCUIT FUNCTIONS
#=============================

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
                'size': self.number_of_qubits  # Has a classical register to measure each Qubit
            }]}],
        }

    def setup_quantum_program(self):
        """Setups the Quantum Circuit for a given program."""
        self.print_status("\n Setting up quantum program...")
        self.qp = QuantumProgram(specs=self.circuit_layout)  # Sets up the quantum program
        self.qc = self.qp.get_circuit(self.circuit_name)     # Creates the quantum circuit layout

        self.qr = self.qp.get_quantum_register('qr')         # Gets the Qubit registers
        self.cr = self.qp.get_classical_register('cr')       # Gets the classical registers
        self.print_operation("Quantum Circuit '" + self.circuit_name + "' compossed of " + str(self.number_of_qubits) + " Qubits and the same Classical Registers, setup!!!\n")

    def quantum_gates(self):
        """Used to setup the quantum circuit's gates"""
        self.print_status("Implementing gates...")
        self.qc.h(self.qr[0])
        self.qc.h(self.qr[1])
        self.print_operation("Gates implemented!\n")

    def setup_results(self):
        """Gets the array of results"""
        self.print_status("Getting the results...")
        # Measures all the qubits and assigns them a classical register
        for qubit in range(self.number_of_qubits):
            self.qc.measure(self.qr[qubit], self.cr[qubit])
        # Executes the quantum circuit
        self.out = self.qp.execute(self.circuit_name, backend=self.backend, shots=self.shots )
        # Gets the total results array
        self.result = self.out.get_counts(self.circuit_name)
        if self.result != False:
            self.print_operation("Got the results!!!\n")
        else:
            self.print_error("Error getting the results\n")
        return self.result

    def get_results(self):
        """Gets the individual Qubit's total amount of 1s"""
        self.print_status("Getting the amount of 1's of each Qubit...")
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

            # Outputs the amount of 1's from LSB to MSB for each individual Qubit
            output.append(current_bit_result)
        self.total_amount_of_ones = output
        self.print_operation("Got the amount of 1s: ")
        print(self.total_amount_of_ones, "\n")
        return self.total_amount_of_ones

    def setup_and_run_complete_circuit(self):
        """Runs a complete quantum program"""
        self.setup_quantum_program()
        self.quantum_gates()
        self.setup_results()
        return self.get_results()

    def run_circuit(self):
        self.setup_results()
        self.results = self.get_results()
        return self.results

    def how_many_qubits(self):
        """Returns how many Qubits there are in the circuit"""
        return self.number_of_qubits

#=============================
# GATE FUNCTIONS
#=============================

    def h_gate(self, qubit_index):
        """Makes an H-Gate where specified"""
        if isinstance(qubit_index, int):
            self.qc.h(self.qr[qubit_index])
        elif isinstance(qubit_index, list):
            for qubit in qubit_index:
                self.qc.h(self.qr[qubit])
        else:
            self.print_error("Error creating H-Gate, neither a list or number as input")

    def u3_gate(self, qubit_index=0, theta=0.0, phi=0.0, lam=0.0):
        """Creates a U3 Rotation Gate"""
        self.qc.u3(theta, phi, lam, self.qr[qubit_index])

    def barrier_gate(self):
        """Setups a barrier gate"""
        self.qc.barrier()

#=============================
# OUTPUT FUNCTIONS
#=============================

    def output_test(self, data_in, data_out):
        """Compares the output results"""
        if data_in  == data_out:
            self.print_operation("Output Correct")
            print()
        else:
            self.print_error("Output Incorrect")
            print()

    def create_lookup(self, num_bits):
        """Creates a lookup table used for Qubit storage"""
        self.bit_lookup = bd.generate_lookup(num_bits)
        return self.bit_lookup

    def decode_qubit(self, which_qubit, num_bits):
        """Retrieves the bits that were stored"""
        self.decoded_qubit = bd.decoder(self.results[which_qubit], self.shots, num_bits)
        return self.decoded_qubit

    def setup_in_classic_gate_mode(self, input_bits):
        """Given an array contanining two bits each, sets it up in classical mode"""
        if len(input_bits) > self.number_of_qubits:
            print_error("Inputs excede number of qubits")
            return
        rl = self.create_lookup(2)
        for x in range(len(input_bits)):
            self.u3_gate(x, rl[input_bits[x]])

#=============================
# TRADITIONAL GATES
#=============================

    def and_gate(self, which_qubit_or_bits):
        """Sets up an AND Gate either on a Qubit or with two input bits"""
        if isinstance(which_qubit_or_bits, int):
            input_to_gate_bits = self.decode_qubit(which_qubit_or_bits, 2)
        elif isinstance(which_qubit_or_bits, str):
            input_to_gate_bits = which_qubit_or_bits
        else:
            print_error("Input to XOR Gate type not recognized")
        if input_to_gate_bits == "11":
            out = "1"
        else:
            out = "0"
        return out

    def or_gate(self, which_qubit_or_bits):
        """Sets up an OR Gate either on a Qubit or with two input bits"""
        if isinstance(which_qubit_or_bits, int):
            input_to_gate_bits = self.decode_qubit(which_qubit_or_bits, 2)
        elif isinstance(which_qubit_or_bits, str):
            input_to_gate_bits = which_qubit_or_bits
        else:
            print_error("Input to XOR Gate type not recognized")
        if input_to_gate_bits == "00":
            out = "0"
        else:
            out = "1"
        return out

    def xor_gate(self, which_qubit_or_bits):
        """Sets up an XOR Gate either on a Qubit or with two input bits"""
        if isinstance(which_qubit_or_bits, int):
            input_to_gate_bits = self.decode_qubit(which_qubit_or_bits, 2)
        elif isinstance(which_qubit_or_bits, str):
            input_to_gate_bits = which_qubit_or_bits
        else:
            print_error("Input to XOR Gate type not recognized")
        if input_to_gate_bits == "00" or input_to_gate_bits == "11":
            out = "0"
        else:
            out = "1"
        return out


#=============================
# PRINT FUNCTIONS
#=============================

    def print_status(self, text):
        print('\x1b[1;34;40m', text, '\x1b[0m')

    def print_error(self, text):
        print('\x1b[1;31;40m', text, '\x1b[0m')

    def print_operation(self, text):
        print('\x1b[1;32;40m', text, '\x1b[0m')
            # CODE START
# C = SomeFramework(1, "my_circuit", 10000)

# C.u3_gate(0, 0.4*math.pi, 0, 0)

# C.run_circuit()
# CODE END

# def add_gates_to_qubits(gate_to_add, initial_qubit, end_qubit=0):
#     print("Gate: ", gate_to_add, " added to ", initial_qubit, " and ", end_qubit)


# add_gates_to_qubits('X', 1)p
# add_gates_to_qubits('X', 2, 3)

