# CHECK
def ring_algorithm(failed_node, num_nodes):
    ring = [i for i in range(1, num_nodes+1)]
    
    # Initiating an election
    initiator = failed_node
    election_message = [initiator]
    current_node = (initiator + 1) % num_nodes
    
    while current_node != initiator:
        election_message.append(current_node)
        current_node = (current_node + 1) % num_nodes
        
    winner = max(election_message)
    
    # Sending Coordinator message
    coordinator_message = [winner]
    current_node = (winner + 1) % num_nodes
    
    while current_node != winner:
        coordinator_message.append(current_node)
        current_node = (current_node + 1) % num_nodes
        
    return coordinator_message

# Input of failed coordinator node and number of nodes
failed_node = int(input("Enter the failed coordinator node: "))
num_nodes = int(input("Enter the number of nodes: "))

result = ring_algorithm(failed_node, num_nodes)
print("Coordinator selected by ring algorithm:", result[0])
