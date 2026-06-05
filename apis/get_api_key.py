from dotenv import load_dotenv
import os


def get_api_key(key_name):
    load_dotenv()

    api_key = os.getenv(key_name, "")

    if not api_key:
        raise RuntimeError(f"{key_name} not set. Check .env")
    
    return api_key


def main():
    pass


if __name__ == "__main__":
    main()

