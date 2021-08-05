import numpy as np
import matplotlib.pyplot as plt

mu = 0.0
sigma = 0.1
selection = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(selection, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='y')
plt.title("Gaussian Distribution")
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.show()

