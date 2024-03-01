from load_cache import load_cache, get_answer, save_cache
from refresh_cache import refresh_cache

def main():
    filename = 'prompts_and_answers.json'

    # Load cache from file
    cache = load_cache(filename)
    print("Loaded Cache:", cache)

    # Example usage of get_answer
    while True:
        user_prompt = input("Enter a prompt (type 'exit' to end): ")
        if user_prompt.lower() == 'exit':
            break

        answer = get_answer(user_prompt, cache, filename)
        print(f"Answer: {answer}")

    # Refresh cache by writing to the file
    refresh_cache(cache, filename)
    print("Cache Refreshed and Saved.")

if __name__ == "__main__":
    main()
