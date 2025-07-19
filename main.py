import argparse

from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Chef CLI")
    parser.add_argument(
        "command",
        choices=["hello", "recipe"],
        help="Command to run"
    )
    parser.add_argument(
        "--name",
        help="Recipe name (for 'recipe' command)"
    )
    args = parser.parse_args()

    if args.command == "hello":
        print("Hello from chef!")
    elif args.command == "recipe":
        if args.name:
            print(f"Preparing recipe: {args.name}")
        else:
            print("Please provide a recipe name with --name.")

if __name__ == "__main__":
    main()
