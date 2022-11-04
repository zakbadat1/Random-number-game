import random

num = 0
def generate_random_number():
  num = random.randint(1,10)
  print(num)

  
def difference_from_answer(guess, answer):
  if guess == answer:
    return "Correct"
  elif guess > answer:
    return "Too high"
  else:
    return "Too Low"



