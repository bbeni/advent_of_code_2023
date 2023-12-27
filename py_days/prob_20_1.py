from ast import Mod


LOW = 0
HIGH = 1

OFF = False
ON = True



modules = {}


class Machine:
    def __init__(self) -> None:
        self.modules = {}

    def add_module(self, module):
        self.modules[module.id] = module

    def connect_all(self):

        # add fizzling dummy modules for dead ends
        for module in list(self.modules.values()):
            for conn_to in module._connections_ids:
                if conn_to not in self.modules:
                    self.modules[conn_to] = Module([], conn_to)

        # connect all
        for id, module in self.modules.items():
            for conn_to in module._connections_ids:
                module.add_outgoing(self.modules[conn_to])
                self.modules[conn_to].add_incomming(module)

        for module in self.modules.values():
            if isinstance(module, Conjunction):
                module.setup_memory()


    def loop(self):
        current_modules = [self.modules['broadcaster']]
        current_inputs = [(LOW, self.modules['broadcaster'])]

        low_counter = 1
        high_counter = 0

        while len(current_modules) != 0:
            # step

            next_modules = []
            next_inputs = []
            for module, inp_and_sender in zip(current_modules, current_inputs):
                inp, sender = inp_and_sender
                out = module.propagate(inp, sender.id)
                #print(module)
                #print(out)
                if out is None:
                    continue
                for next in module.outgoing_connections:
                    next_modules.append(next)
                    next_inputs.append((out, module))

                if out == LOW:
                    low_counter += len(module.outgoing_connections)
                else:
                    high_counter += len(module.outgoing_connections)

            current_modules = next_modules
            current_inputs = next_inputs

        return high_counter, low_counter


class Module:
    def __init__(self, connections_ids, id):
        self._connections_ids = connections_ids
        self.incomming_connections = []
        self.outgoing_connections = []
        self.id = id

    def add_incomming(self, other):
        self.incomming_connections.append(other)

    def add_outgoing(self, other):
        self.outgoing_connections.append(other)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id} -> {self._connections_ids}>'
    
    def propagate(self, pulse_in, sent_by):
        print(f'{self.id} just fizzled into the sand..')
        return pulse_in
    

class FlipFlop(Module):
    def __init__(self, connections, id):
        super().__init__(connections, id)
        self.state = OFF
    
    def propagate(self, pulse_in, _):
        if pulse_in == HIGH:
            return
        self.state = not self.state
        if self.state == ON:
            return HIGH
        return LOW

class Conjunction(Module):
    def __init__(self, connections, id):
        super().__init__(connections, id)

    def setup_memory(self):
        self.memory = {}
        for incomming in self.incomming_connections:
            self.memory[incomming.id] = LOW

    def propagate(self, pulse_in, sent_by):
        self.memory[sent_by] = pulse_in

        if LOW in self.memory.values():
            return HIGH
        return LOW

class Broadcaster(Module):
    def propagate(self, pulse_in, sent_by):
        return pulse_in



machine = Machine()
for line in open(0):
    tokens = line.strip().replace(' ->', ',').split(', ')

    mod = None
    if tokens[0][0] == 'b':
        mod = Broadcaster(tokens[1:], tokens[0])
    if tokens[0][0] == '%':
        mod = FlipFlop(tokens[1:], tokens[0][1:])
    if tokens[0][0] == '&':
        mod = Conjunction(tokens[1:], tokens[0][1:])
    machine.add_module(mod)

machine.connect_all()

high = 0
low = 0

for i in range(1000):
    h, l =machine.loop()
    high += h
    low += l

print(high,low, high*low)