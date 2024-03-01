import json

def load_cache(filename):
    """
    Load the cache from the specified JSON file.

    Parameters:
    - filename (str): The path to the JSON cache file.

    Returns:
    - dict: The loaded cache as a dictionary.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_cache(cache, filename):
    """
    Save the cache to the specified JSON file.

    Parameters:
    - cache (dict): The cache dictionary to save.
    - filename (str): The path to the JSON cache file to save to.
    """
    with open(filename, 'w') as file:
        json.dump(cache, file, indent=2)

def get_answer(prompt, cache, filename):
    """
    Get the answer for a given prompt from the cache.

    If the prompt is not found in the cache (case-insensitive), prompt the user to enter an answer
    and save it to the cache.

    Parameters:
    - prompt (str): The prompt for which to get the answer.
    - cache (dict): The cache dictionary to search and update.
    - filename (str): The path to the JSON cache file.

    Returns:
    - str: The answer to the prompt.
    """
    # Convert prompt to lowercase for case-insensitive search
    prompt_lower = prompt.lower()

    if prompt_lower in (key.lower() for key in cache):
        # Find the original prompt from the cache
        original_prompt = next(key for key in cache if key.lower() == prompt_lower)
        return cache[original_prompt]
    else:
        answer = input(f"Prompt: {prompt}\nEnter answer: ")
        cache[prompt] = answer
        save_cache(cache, filename)
        return answer
