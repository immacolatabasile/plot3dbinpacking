import csv
import json

from Container import Container


def write_container_to_csv(container, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)


        writer.writerow(['Container ID', 'Dimensions (X,Y,Z)', 'Item ID', 'Position (X,Y,Z)', 'Size (X,Y,Z)'])

        # Scrivi i dati per ogni Item
        for Item in container.get_Items():
            writer.writerow([
                container.container_id,
                f"{container.dimensions}",
                Item.item_id,
                f"{Item.position}",
                f"{Item.size}"
            ])

    print(f"CSV salvato come {filename}")

def write_container_to_json(container, filename):
    container_data = {
        'container_id': container.container_id,
        'dimensions': container.dimensions,
        'Items': []
    }


    for Item in container.get_Items():
        Item_data = {
            'item_id': Item.item_id,
            'position': Item.position,
            'size': Item.size
        }
        container_data['Items'].append(Item_data)

    with open(filename, 'w') as json_file:
        json.dump(container_data, json_file, indent=4)

    print(f"JSON salvato come {filename}")

def read_containers_from_json(filename):
    containers = []
    try:
        with open(filename, 'r') as json_file:
            containers_data = json.load(json_file)

        if not isinstance(containers_data, list):
            raise ValueError("JSON data is not a list of containers.")

        for container_data in containers_data:
            container = Container(container_id=container_data['container_id'], dimensions=tuple(container_data['dimensions']))

            for item_data in container_data.get('items'):
                item_id = item_data['item_id']
                position = item_data['position']
                size = tuple(item_data['size'])
                container.add_Item(item_id=item_id, position=position, size=size)

            containers.append(container)
        return containers

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON.")
    except KeyError as e:
        print(f"Error: Missing key in JSON data: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")