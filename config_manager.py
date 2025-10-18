import json
import os
from typing import Optional, Dict, List

CONFIG_FILE = "config.json"

def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                
                # Migrate old single owner_uid to new owner_uids list
                if "owner_uid" in config and config["owner_uid"] is not None:
                    if "owner_uids" not in config:
                        config["owner_uids"] = [config["owner_uid"]]
                    del config["owner_uid"]
                    save_config(config)
                
                # Ensure owner_uids exists
                if "owner_uids" not in config:
                    config["owner_uids"] = []
                
                return config
        except:
            return {"owner_uids": [], "emotes": {}}
    return {"owner_uids": [], "emotes": {}}

def save_config(config: dict) -> None:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def set_owner_uids(uids: List[str]) -> List[str]:
    config = load_config()
    config["owner_uids"] = uids
    save_config(config)
    return uids

def get_owner_uids() -> List[str]:
    config = load_config()
    return config.get("owner_uids", [])

def add_emote(name: str, emote: str) -> tuple:
    config = load_config()
    if "emotes" not in config:
        config["emotes"] = {}
    config["emotes"][name] = emote
    save_config(config)
    return (name, emote)

def get_emote(name: str) -> Optional[str]:
    config = load_config()
    return config.get("emotes", {}).get(name)

def get_all_emotes() -> Dict[str, str]:
    config = load_config()
    return config.get("emotes", {})
