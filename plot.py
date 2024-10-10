import argparse
import os
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import random
import warnings
from Function import read_containers_from_json

warnings.filterwarnings("ignore")  # Ignora i warning di matplotlib


class Plotter:
    def __init__(self, container):
        self.container = container
        self.all_colors = [k for k, v in pltc.cnames.items()]

    def _cuboid_data(self, o, size=(1, 1, 1)):
        X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
             [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
             [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
             [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
             [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
             [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
        X = np.array(X).astype("float")
        for i in range(3):
            X[:, :, i] *= size[i]
        X += np.array(o)
        return X

    def _plotCubeAt(self, positions, sizes=None, colors=None, **kwargs):
        if not isinstance(colors, (list, np.ndarray)):
            colors = ["C0"] * len(positions)
        if not isinstance(sizes, (list, np.ndarray)):
            sizes = [(1, 1, 1)] * len(positions)

        g = []
        for p, s, c in zip(positions, sizes, colors):
            g.append(self._cuboid_data(p, size=s))
        return Poly3DCollection(np.concatenate(g), facecolors=np.repeat(colors, 6), **kwargs)

    def plot(self, path=None):
        """Genera una vista 3D del contenitore e degli oggetti."""
        positions = []
        sizes = []
        labels = []

        for item in self.container.get_Items():
            positions.append(item.position)
            size = item.size
            sizes.append((size[0], size[1], size[2]))
            labels.append(f"{item.item_id}")

        colors = random.sample(self.all_colors * 10, len(positions))

        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(projection='3d')
        ax.add_collection3d(self._plotCubeAt(positions, sizes, colors=colors, edgecolor="k", alpha=0.5))

        X, Y, Z = self.container.dimensions

        # Aggiunge le linee rosse per tracciare i limiti del contenitore
        for x in [0, X]:
            for y in [0, Y]:
                ax.plot([x, x], [y, y], [0, Z], color='r', linewidth=2)
        for x in [0, X]:
            for z in [0, Z]:
                ax.plot([x, x], [0, Y], [z, z], color='r', linewidth=2)
        for y in [0, Y]:
            for z in [0, Z]:
                ax.plot([0, X], [y, y], [z, z], color='r', linewidth=2)

        ax.set_xlim([0, X])
        ax.set_ylim([0, Y])
        ax.set_zlim([0, Z])

        for label, color in zip(labels, colors):
            ax.plot([], [], [], color=color, label=label)
        ax.legend(loc="upper right")
        ax.set_title(f"Container ID: {self.container.container_id}")

        if path:
            plt.savefig(path)
            print(f"Plot salvato in: {path}")
        else:
            plt.show()



