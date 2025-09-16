from fluxion.utils.config import OptimisationConfig , generate_default_server_configs , to_json_dict
import json

default_config = generate_default_server_configs()
default_config = to_json_dict(default_config)
print(default_config)

def generate_server_configs():
    with open("optmization_config.json", "r") as f:
        config = OptimisationConfig.from_dict(json.load(f))
        
    print(config)
    
if __name__ == "__main__":
    generate_server_configs()