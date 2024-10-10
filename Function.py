import csv
import json

from Container import Container


def write_container_to_csv(container, filename):
    """Scrive i dettagli di un container e i suoi Item in un file CSV."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Scrivi l'intestazione
        writer.writerow(['Container ID', 'Dimensions (X,Y,Z)', 'Item ID', 'Position (X,Y,Z)', 'Size (X,Y,Z)'])

        # Scrivi i dati per ogni Item
        for Item in container.get_Items():
            writer.writerow([
                container.container_id,                          # Container ID
                f"{container.dimensions}",                      # Dimensioni del container
                Item.item_id,                               # Item ID
                f"{Item.position}",                           # Posizione del Item
                f"{Item.size}"                                # Dimensioni del Item
            ])

    print(f"CSV salvato come {filename}")

def write_container_to_json(container, filename):
    """Scrive i dettagli di un container e i suoi Item in un file JSON."""
    container_data = {
        'container_id': container.container_id,
        'dimensions': container.dimensions,
        'Items': []
    }

    # Aggiungi i Item al dizionario del container
    for Item in container.get_Items():
        Item_data = {
            'item_id': Item.item_id,
            'position': Item.position,
            'size': Item.size
        }
        container_data['Items'].append(Item_data)

    # Scrivi il JSON nel file
    with open(filename, 'w') as json_file:
        json.dump(container_data, json_file, indent=4)

    print(f"JSON salvato come {filename}")

def read_containers_from_json(filename):
    """Legge i dettagli di più container e i loro Item da un file JSON."""
    containers = []  # Lista per memorizzare i container letti
    try:
        with open(filename, 'r') as json_file:
            containers_data = json.load(json_file)

        # Controlla se i dati sono una lista di container
        if not isinstance(containers_data, list):
            raise ValueError("JSON data is not a list of containers.")

        # Crea un'istanza di ogni container
        for container_data in containers_data:
            container = Container(container_id=container_data['container_id'], dimensions=tuple(container_data['dimensions']))

            # Aggiungi i Item al container
            for item_data in container_data.get('items'):
                item_id = item_data['item_id']  # Assicurati di utilizzare 'item_id' in minuscolo
                position = item_data['position']
                size = tuple(item_data['size'])
                container.add_Item(item_id=item_id, position=position, size=size)

            containers.append(container)  # Aggiungi il container alla lista

        return containers  # Restituisci la lista di container

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