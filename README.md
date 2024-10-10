# Container Plotter

This program reads a JSON file containing information about containers and their associated objects (`Item`) and
automatically generates a 3D plot of each container with its items inside. The program supports multiple containers and
saves the plots as image files in a specified directory.

## Project Structure

The project is based on two main classes: `Container` and `Item`.

### `Item` Class

The `Item` class represents an object placed inside a container. Its properties include:

- **`item_id`**: A unique identifier for the item.
- **`position`**: The [x, y, z] coordinates that define the position of the item within the container.
- **`size`**: The dimensions [width, height, depth] of the item.

### `Container` Class

The `Container` class manages a collection of `Item` objects. Its main properties are:

- **`container_id`**: A unique identifier for the container.
- **`dimensions`**: The [width, height, depth] dimensions of the container.
- **`Items`**: A dictionary that stores `Item` objects added to the container.

The `Container` class includes methods to:

- **`add_Item`**: Add an item to the container if it is within the boundaries.
- **`_is_within_bounds`**: Check if an item fits within the container's dimensions.
- **`get_Items`**: Retrieve all the items in the container.

## Installation

1. Clone the repository:
   ```bash

   git clone https://github.com/your-username/container-plotter.git
   cd container-plotter 
   ```
2. Install the required dependencies:
```bash
    pip install -r requirements.txt
```

3. Running the Program
   ```bash
   python plot_containers.py <json_file_path> <output_directory>

```


TEST 
 python plot_containers.py "containers.json" "Plot3DBinPacking" 
