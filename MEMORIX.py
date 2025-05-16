import random
import time

# Clear the screen
def clean():
    print("\n" * 50)

# Save high score to high_score.txt
def save_high_score(level):
    f = open("high_score.txt", "w")
    f.write(str(level))
    f.close()

# Load high score from high_score.txt
def load_high_score():
    try:
        f = open("high_score.txt", "r")
        score = int(f.read())
        f.close()
        return score
    except:
        return 0

# Save name and score to leaderboard.txt
def save_leaderboard(name, level):
    f = open("leaderboard.txt", "a")
    f.write(name + ":" + str(level) + "\n")
    f.close()

# Sort helper: get score from (name, score) tuple
def get_score(leader):
    return leader[1]

# Load leaderboard.txt
def load_leaderboard():
    try:
        f = open("leaderboard.txt", "r")
        lines = f.readlines()
        f.close()
        board = []
        for line in lines:
            if ":" in line:
                parts = line.strip().split(":")
                board.append((parts[0], int(parts[1])))
        board.sort(key=get_score, reverse=True)
        return board
    except:
        return []

# Show top 5 player and score
def show_leaderboard():
    board = load_leaderboard()
    print()
    print("🏆 Top 5 High Scores:")
    for i in range(min(5, len(board))):
        print(str(i+1) + ". " + board[i][0] + " - Level " + str(board[i][1]))
    return board

# main()
def main():
    level = 1
    high_score = load_high_score()

    clean()
    print("🎓 Welcome to MEMORIX!")
    print("🇦🇺 Let's take a quick brain break!")
    print("🥴 Numbers will flash briefly — try to remember them in order.")
    print("They say a koala’s memory can reach level 10… Can yours? 🐨")
    time.sleep(3.0)

    while True:
        sequence = []
        for i in range(level):
            sequence.append(random.randint(0, 9))
        print()
        print("Get ready...")
        time.sleep(0.7)
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        clean()
        print("🐨 GO! 🐨\n")
        time.sleep(0.5)

        for num in sequence:
            print("   " + str(num) + "   ")
            print("-----")
            time.sleep(0.6)
            clean()

        user_input = input("Enter the sequence: ")
        user_list = list(user_input.strip())

        correct = True
        for i in range(len(sequence)):
            if i >= len(user_list) or user_list[i] != str(sequence[i]):
                print()
                print("❌ You got number " + str(i+1) + " wrong.")
                print("You entered: " + (user_list[i] if i < len(user_list) else "nothing"))
                print("Correct number was: " + str(sequence[i]))
                correct = False
                break

        if correct:
            print("🥴 Correct! Reaching next level.")
            level += 1
            time.sleep(0.8)
            clean()
        else:
            print()
            print("🤯 Game Over. You reached Level " + str(level) + ".")
            if level > high_score:
                print("🎉 New High Score!")
                save_high_score(level)
                high_score = level
            else:
                print("🏆 High Score: " + str(high_score))

            name = input("Enter your name: ")
            if name.strip() == "":
                name = "Anonymous"
            save_leaderboard(name, level)

            board = show_leaderboard()
            for i in range(len(board)):
                if board[i][0] == name and board[i][1] == level:
                    print("\n📍 You are in position #" + str(i+1))
                    break
            print()
            print("Going Back to menu...")
            print()
            time.sleep(3)
            break

# Menu
def menu():
    while True:
        print("🐨 Welcome to MEMORIX!")
        print("[1] Start Game")
        print("[2] View High Score")
        print("[Q] Quit")
        choice = input("Choose an option: ").strip().upper()

        if choice == "1":
            main()
        elif choice == "2":
            print("\n🏆 Current High Score: " + str(load_high_score()) + "\n")
            show_leaderboard()
            time.sleep(3)
        elif choice == "Q":
            print("TA! See ya mate👋")
            break
        else:
            print("Invalid choice. Try [1|2|Q].")
            print()


if __name__ == "__main__":
    menu()
