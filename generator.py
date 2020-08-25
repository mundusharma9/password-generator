import string
import random
import time
import itertools
import threading
import sys


print("----------------------------------password generator by samael-----------------------------------------------")

pass1 = string.ascii_uppercase
pass2 = string.ascii_lowercase
pass3 = string.digits
pass4 = string.punctuation


password  = None
while password is None:
    num_of_password_character = (input("How many digits password do you want?:"))
    try:
        password  = int(num_of_password_character)
    except ValueError:
        print(num_of_password_character, " is not a number please enter numbers only")

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True
generator= []
generator.extend(list(pass1))
generator.extend(list(pass2))
generator.extend(list(pass3))
generator.extend(list(pass4))
random.shuffle(generator)
print("\nYour generated password")
print("".join(generator[0:password]))
k=input("      Press enter to exit")