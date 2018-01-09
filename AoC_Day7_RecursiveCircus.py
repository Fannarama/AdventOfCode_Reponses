"""
This program sorts through a list of names/towers that have more towers stacked atop of them.
The order in which they appear is not correct so the list must be sorted to determine which tower is stacked on which.
There is also a weight associated with each tower that is used in Part 2. An example dataset can be seen below.

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

The base here is tknk and all other towers branch from that original one.
"""
#Part 1
import re

x = open("./DataInputs/Day7.txt","r").read()
print("Data imported from: \"./DataInputs/Day7.txt\"")
data = [str(n) for n in x.split("\n")]

nodes = []
stacked = []
for line in data:
    nodes.append(re.match(r'[\w]+', line).group())
    if re.search(r'->', line):
        input = re.search(r'-> (?P<input>[\w, ]+)', line).group('input').replace(' ','').split(',')
        for line in input:
            stacked.append(line)

#print("All Nodes: " + "\t\t" +str(sorted(nodes)))
#print("All Supported Nodes: " + str(sorted(stacked)))
print("Root Node: " + str(set(nodes)-set(stacked)))
root = str(set(nodes)-set(stacked))

"""
    Here I cobbled together an if statement from the 'regex' documentation page and another question response I
    found in the forums. Here the if statement searches the lines of the 'data' set for any that contain a
    "->" phrase and isolates defines it only for that line of the data set. This means any content after the "->"
    and before the "\n" will register as a True response for the if statement, and you proceed to the input portion within the if statement.
    
    Here, an input is defined as a list of searched items using 're.search'. These items are the parsed characters
    defined in the r'-> (?P<input>[\w, ]+)' section that interprets it as one 'line' of characters between the "->"
    and the "\n". Here the (?P.... identifies this as being a named group (which is defined again by the .group('input') argument
    in the same line). That means that the conents of this line will be placed in a group called 'input' which is then assigned
    to a variable of the same name. The group and variable name are the same because we update the value of 'input' for
    each iteration of the for loop which is then appended to a separate list so there is no need to give unique named
    groups if we just want the functionality that the re.search command provides. The .replace(' ','') removes the space
    between the list of brances, and the .split(',') removes the comma by making it the splitting point for a new
    entry in the 'input' list. Without this split you would just get a list of individual characters. The '-> ' is not
    included becasue the [\w], ]+ occurs after '-> ' in the re.search command.
    
    Lastly, the input for that given line from the 'data' set is passed through another for loop where it is
    subdivided and its individual entries are appended to the stacked list.
"""

#Part 2
node_map = {}
node_values = {}
for line in data:
    p_node = re.match(r'[\w]+', line).group()
    node_value = re.search(r'[\d]+', line).group()
    node_values[p_node] = int(node_value)
    if re.search(r'->', line):
        nodes = re.search(r'-> (?P<nodes>[\w, ]+)', line).group('nodes').replace(' ', '').split(',')
        node_map[p_node] = nodes
        
def child_values(node):
    children = node_map[node]
    supports = []
    for child in children:
        if child in node_map.keys():
            child_support = child_values(child)
            value = sum(child_support) + node_values[child]
        else:
            value = node_values[child]
        supports.append(value)
    print(supports)
    if len(set(supports)) != 1:
        print ('Imbalance detected on {}, due to children {}, weighing {}'.format(node, node_map[node], supports))
    return supports

#child_values('vmpywg')
child_values('ncrxh')
print(node_map['ncrxh'])
print(node_values['aptjif'],node_values['glwgh'],node_values['xddbpyw'])
print(node_values['ncrxh'])

