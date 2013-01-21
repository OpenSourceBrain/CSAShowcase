from csa import *

# Create index intervals for excitatory, inhibitory
# and all cells
e = ival (0, 599)
i = ival (600, 899)
a = e + i

# Create geometry function g and metric d
g = random2d (900)
d = euclidMetric2d (g)

# Excitatory and inhibitory conductances, computed as
# gaussian value sets (provides the gaussian of the
# distance for every index pair)
g_e = gaussian (0.1, 0.3) * d
g_i = gaussian (0.2, 0.3) * d

# Create connection-sets with gaussian dependent random
# masks, gaussian dependent conductance and distance
# dependent delay: (mask, conductance, delay)
c_e = cset (random * g_e, g_e, d)
c_i = cset (random * g_i, -g_i, d)

# Combine excitatory and inhibitory connectivity into one
# network using intersection (*) and multiset sum (+)
# operators
c = cross (e, a) * c_e + cross (i, a) * c_i

# We may also plot the outgoing connections from one
# excitatory neuron around coordinate (0.33, 0.5) and one
# inhibitory neuron around coordinate (0.67, 0.5)
sources = [g.inverse(0.33,0.5,e), g.inverse(0.67,0.5,i)]
gplotsel2d (g, c, sources, value=0, range=[-1,1])
