import json

class PromptCacher:
    """
    A class for caching prompts and answers.

    This class allows users to cache prompts and answers in a JSON file.
    """

    def __init__(self, cache_file='prompts_and_answers.json'):
        """
        Initialize the PromptCacher object.

        Parameters:
        - cache_file (str): The path to the JSON cache file.
        """
        self.cache_file = cache_file
        self.cache = self.load_cache()

    def load_cache(self):
        """
        Load the cache from the JSON file.

        Returns:
        - dict: The loaded cache as a dictionary.
        """
        try:
            with open(self.cache_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_cache(self):
        """
        Save the current cache to the JSON file.
        """
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file, indent=2)

    def get_answer(self, prompt):
        """
        Get the answer for a given prompt from the cache.

        If the prompt is not found in the cache, prompt the user to enter an answer
        and save it to the cache.

        Parameters:
        - prompt (str): The prompt for which to get the answer.

        Returns:
        - str: The answer to the prompt.
        """
        if prompt in self.cache:
            return self.cache[prompt]
        else:
            answer = input(f"Prompt: {prompt}\nEnter answer: ")
            self.cache[prompt] = answer
            self.save_cache()
            return answer

def main():
    """
    Main function to interact with the PromptCacher.
    """
    prompt_cacher = PromptCacher()

    while True:
        user_prompt = input("Enter a prompt (type 'exit' to end): ")
        if user_prompt.lower() == 'exit':
            break

        answer = prompt_cacher.get_answer(user_prompt)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
