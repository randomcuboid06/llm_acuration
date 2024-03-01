import json

def refresh_cache(cache, filename):
    """
    Refresh the entire cache and save it to the specified JSON file.

    Parameters:
    - cache (dict): The cache dictionary to refresh.
    - filename (str): The path to the JSON cache file to save to.
    """
    with open(filename, 'w') as file:
        json.dump(cache, file, indent=2)
