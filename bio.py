# Self-introduction with additional details

name = "Caio"

profession = "Data Analyst"

nationality = "Brazil"

age = 29

current_location = "Boston, USA"

interests = {

  "professional_interests": ["Data Science", "Artificial Intelligence", "Collaborative Career Growth"],

  "personal_interests": ['football', 'soccer', 'cooking', 'know how stuff works']

}



print(f"Hello! My name is {name}, and I am a {profession} from {nationality}.")

print(f"I am {age} years old and currently living in {current_location}.")

print("""These days I'm challenging myself to be more active in the social networks, but not just watching what is going on.\n

Also, it has been a few months since I moved to America and I really would like to meet people around me matching some interests.\n""")

print("I'm passionate about exploring areas like", end=" ")



professional_interests = interests["professional_interests"]

for i in range(len(professional_interests) - 1):

  print(professional_interests[i], end=", ")

print("and", professional_interests[-1] + ".\n")



print("As hobbies, I have:", end=" ")



personal_interests = interests["personal_interests"]

for i in range(len(personal_interests) - 1):

  print(personal_interests[i], end=", ")

print("and", personal_interests[-1] + ".\n")



print("Want to know more about my profile? Contact me here or at caio.moro@outlook.com 😉")