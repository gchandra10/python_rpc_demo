from xmlrpc.server import SimpleXMLRPCServer


class CalculatorService:
    def add(self, x, y):
        print(f"Server: Computing {x} + {y}")
        return x + y
    
    def subtract(self, x, y):
        print(f"Server: Computing {x} - {y}")
        return x - y
    
    def multiply(self, x, y):
        print(f"Server: Computing {x} * {y}")
        return x * y
    
    def divide(self, x, y):
        print(f"Server: Computing {x} / {y}")
        if y == 0:
            return "Error: Division by zero!"
        return x / y

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Calculator RPC Server running on port 8000...")
print("Waiting for client requests...")

# Register our calculator service
calc = CalculatorService()
server.register_instance(calc)

# Start the server
server.serve_forever()