
import yaml


def save_model(vertices, file_path):
    with open(file_path, 'w') as file:
        file.write(yaml.dump(vertices))
