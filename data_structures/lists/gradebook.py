last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = []

# Was instructred to combine the previous list objects into a 2d list manually.
# Why would we do that!?!?
for i, val in enumerate(subjects):
    gradebook.append([val, grades[i]])

# New grades come in
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Update visual arts
gradebook[-1][-1] = gradebook[-1][-1] + 5

# Change poetry to pass / fail
gradebook[2].remove(gradebook[2][-1])
gradebook[2].append("Pass")

# Combine all gradeboks
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)