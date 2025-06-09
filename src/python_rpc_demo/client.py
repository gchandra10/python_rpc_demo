import xmlrpc.client

# Connect to the remote server
print("Connecting to Calculator RPC Server...")
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("\n=== RPC Calculator Demo ===")

try:
    # Make RPC calls - these look like local function calls!
    print("Calling remote add function...")
    result1 = server.add(15, 25)
    print(f"15 + 25 = {result1}")
    
    print("\nCalling remote multiply function...")
    result2 = server.multiply(7, 8)
    print(f"7 * 8 = {result2}")
    
    print("\nCalling remote divide function...")
    result3 = server.divide(100, 4)
    print(f"100 / 4 = {result3}")
    
    print("\nTrying division by zero...")
    result4 = server.divide(10, 0)
    print(f"10 / 0 = {result4}")
    
except Exception as e:
    print(f"RPC Error: {e}")

print("\nDone! All calculations were performed on the remote server.")

# - Client calls server.add(15, 25) 
# - This looks like a normal function call
# - But actually sends a network request to the server
# - Server receives request, runs the calculation
# - Server sends result back over network
# - Client receives 40 and displays it
# - User never sees the network complexity!