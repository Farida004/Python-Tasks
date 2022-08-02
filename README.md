# python-tasks

# Task 1 - Algorithm Test

Implement a string compression using python. For example, aaaabbbccddddddee would become a4b3c2d6e2. If the length of the string is not reduced, return the original string.

## Requirements
Implement a compress function which accepts an input string and returns a compressed string. Code must be implemented using python 3.6 and must follow strictly pep8 rules.
Provide comments regarding the implementation.

## Test Cases 
assert compress(‘bbcceeee’) == ‘b2c2e4’
assert compress(‘aaabbbcccaaa’) == ‘a3b3c3a3’
assert compress(‘a’) = a

# Task 2 - Network Failure Point
We have a mesh network connected by routers labeled from 1 to 6 in a directed manner. Write an algorithm that can detect the routers with the highest number of connections so we might know which routers will cause a network failure if removed. Multiple connections between the same routers should be treated as separate connections. A tie for the most number of connections is possible. 

## Requirements
Implement a identify_router function that accepts an input graph of nodes representing the total network and identifies the node with the most number of connections. 
Return the label of the node. 

Implement a directed graph data structure using Python 3.6.

Each node is unique thus there will be no cases of having multiple nodes with the same label.
Each node will have an infinite number of both inbound and outbound links.

## Test Cases 

1 -> 2 -> 3 -> 5 -> 2 -> 1 = 2 *since router 2 has 2 inbound links and 2 outbound links

1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6 = 5 * since router 5 has 2 inbound links and 2 outbound link

2 -> 4 -> 6 -> 2 -> 5 -> 6 = 2, 6 * since router 2 has 1 inbound link and 2 outbound links and 6 has 2 inbound links and 1 outbound link

# Task 3 - Django Test


