class EnhancedCPU:
    def __init__(self):
        # Instrucciones, incluyendo una operación condicional y manejo de memoria
        self.memory = ["LOAD 10", "ADD 20", "STORE 0", "SUB 30", "JUMP_IF_ZERO 6", "JUMP 0", "HALT"]
        self.data_memory = [0] * 10  # Memoria de datos para operaciones de carga y almacenamiento
        self.pc = 0  # Contador de programa
        self.register = 0  # Registro general
        self.zf = False  # Flag de cero
        self.running = True  # Controla la ejecución del ciclo

    def fetch(self):
        # Obtener y avanzar la instrucción actual
        instruction = self.memory[self.pc]
        self.pc += 1
        print(f"Fetching instruction at PC={self.pc - 1}: {instruction}")
        return instruction

    def execute(self, instruction):
        # Ejecutar la instrucción
        parts = instruction.split()
        op = parts[0]

        print(f"Executing: {instruction}")  # Mostrar la instrucción que se está ejecutando

        if op == "LOAD":
            self.register = int(parts[1])
            print(f"LOAD: Register set to {self.register}")
        elif op == "ADD":
            self.register += int(parts[1])
            print(f"ADD: Register increased to {self.register}")
        elif op == "SUB":
            self.register -= int(parts[1])
            self.zf = self.register == 0
            print(f"SUB: Register decreased to {self.register}, Zero Flag is {'set' if self.zf else 'not set'}")
        elif op == "STORE":
            address = int(parts[1])
            self.data_memory[address] = self.register
            print(f"STORE: Storing {self.register} in data memory at address {address}")
        elif op == "JUMP":
            self.pc = int(parts[1])
            print(f"JUMP: Jumping to instruction at address {self.pc}")
        elif op == "JUMP_IF_ZERO":
            print(f"JUMP_IF_ZERO: Zero Flag is {'set' if self.zf else 'not set'}")
            if self.zf:
                self.pc = int(parts[1])
                print(f"JUMP_IF_ZERO: Jumping to instruction at address {self.pc}")
        elif op == "HALT":
            print("HALT: Stopping execution")
            self.running = False

    def run(self):
        # Ejecutar el ciclo de instrucciones hasta que se detenga
        while self.running:
            instruction = self.fetch()
            self.execute(instruction)

# Crear una instancia de la CPU mejorada y ejecutarla
cpu = EnhancedCPU()
cpu.run()
