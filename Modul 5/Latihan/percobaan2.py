import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([12, 13, 10, 7, 8, 4])

plt.figure(figsize=(10,4))
plt.title('Gamestonks Stock Rate')
plt.xlabel('Years')
plt.ylabel('Stock Price (USD)')
plt.plot(xpoints, ypoints, color='green', marker='o')
plt.xlim([0,8])
plt.ylim([0,14])
plt.xticks(xpoints, labels=["2003", "2005", "2007", "2009", "2011", "2013"])
plt.yticks(ypoints, labels=["210", "230", "200", "170", "180", "80"])
plt.show()