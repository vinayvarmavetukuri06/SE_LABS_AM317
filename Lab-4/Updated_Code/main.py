from game import WordleGame


if __name__ == "__main__":
    print("Choose word length: 4, 5, or 6.")

    while True:
        choice = input("> ").strip().lower()

        if choice == "q":
            print("Game quit.")
            break

        if choice in {"4", "5", "6"}:
            WordleGame(length=int(choice)).run()
            break

        print("Enter 4, 5, or 6.")
