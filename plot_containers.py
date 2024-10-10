import argparse
import os

from Function import read_containers_from_json
from plot import Plotter


def main():
    parser = argparse.ArgumentParser(description="Plot containers from a JSON file.")
    parser.add_argument("json_file", help="Path to the JSON file containing container data")
    parser.add_argument("output_directory", help="Directory where the plots will be saved")
    args = parser.parse_args()

    output_directory = args.output_directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    containers = read_containers_from_json(args.json_file)

    counter = 1
    for container in containers:
        plotter = Plotter(container)
        filename = os.path.join(output_directory, f"{container.container_id}_{counter}.png")
        plotter.plot(filename)
        counter += 1


if __name__ == "__main__":
    main()