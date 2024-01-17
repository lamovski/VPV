import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10.01, 0.01)
plt.figure(figsize=(10, 5))
plt.xticks([])
plt.yticks([])
plt.plot(x, x,       label=r'Второй опыт')
plt.plot(x, x**(1.8),label=r'Первый опыт')
plt.xlabel(r'$U$', fontsize=14)
plt.ylabel(r'$I$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.savefig('./pics/taus.png')
