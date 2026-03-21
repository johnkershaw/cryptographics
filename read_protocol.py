import protocol_visualiser as pv

filepath = 'protocols/nspk.txt'
f = open(filepath, 'r')
lines = f.readlines()
f.close()

# print(lines)

pv.setup()

protocol = []
for line in lines:
    if '->' in line:
        line = line[line.find('.') + 1:].strip()
        protocol.append(line)
print(protocol)
pv.process(protocol)

pv.teardown()