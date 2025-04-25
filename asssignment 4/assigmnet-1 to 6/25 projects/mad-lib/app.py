print("Welcome to the Mad Libs Game: A Crazy Day at School!\n")

teacher_name = input("Enter your teacher's name: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb ending in -ed: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
silly_word = input("Enter a silly word (like 'boink' or 'splat'): ")

story = f"""
Today was a really {adjective1} day at school. My teacher, {teacher_name}, gave us a surprise quiz!
Right when I opened my {noun1}, I accidentally {verb1} all over the classroom.
Everyone started laughing and the principal came from the {place} to see what happened.

He looked so {adjective2} when he heard me shout "{silly_word}!".
I think I’m going to be the talk of the school for a while!
"""

print("\nHere's your Mad Libs story:")
print(story)