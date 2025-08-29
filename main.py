import Circuit

circuit = Circuit.Circuit(12)

resistors = circuit.add_resistor(input("assig a resistor tag: "), int(input("add a resistor value: ")))
current = circuit.calculate_tcurrent()
resistance = circuit.calculate_tresistance()
print(circuit.get_resistors())
print(current)






