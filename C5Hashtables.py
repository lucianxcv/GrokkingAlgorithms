voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")


"""🔍 Explanation:

It checks if someone already voted using their name as a key

If they’re not in the dictionary, they’re allowed to vote

Then it adds them so next time they’re blocked

This is fast and clean, thanks to hash tables."""