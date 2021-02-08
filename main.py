print("what's your mood")

mood = input("what's your mood")

if mood == "happy":
    print("It is great to see you {0}.".format(mood))
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Please, don't be {0}. I suggest you to listen to your favourite music.".format(mood))
elif mood == "relaxed":
    print("That's great to hear! Feeling {0} is what we need in this hectic times!".format(mood))
else:
    print("I don't recognize this mood.")

