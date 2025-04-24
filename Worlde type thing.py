import random

word_list = ["suger","black","range","quill","craic","ergot","ouija","soare","tares","ducat","quirk","karst","xebec","gnome","cruet","igloo","shard","okapi","alogi","oorie","poesy","scrod","thole","vinal","zakat","zaire","zaman"]
hidden_word = random.choice(word_list)

for i in range(6):
    guess_word = input()
    output = ""

    if len(guess_word) == 5:

        
        
        print(output)
        if output == "🟩🟩🟩🟩🟩":
            print("You win")
            break

    print(f"You used {i+1} guesses")
