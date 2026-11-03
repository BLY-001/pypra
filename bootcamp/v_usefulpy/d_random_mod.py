#THE RANDOM MODULE
# random - Generate pseudo-random numbers

# randomness has many uses in science, statistics, cryptography, gaming, gambing and other fields
# i.e random assigmnet in randomized controlled trials helps scientist to test hypothesis and random numbers or pseudo random numbers help video games such as video Poker
# in this lecture we will see how to use the python random module that generates pseudo random numbers and sequences most random data generated with python or other programming language
# is not fully random in the scientific sense of the world rather it is pseudo-random generated with a pseudo random number generator (PRNG) which is essentially any algorithm which is used to generate seemingly random but still reproducible data

# nb:the pseudo-random generators in this module should not be used for security purposes or cryptogrphic uses, there are other modules that can be used in cryptographic application such as the secret Module

import random
random.random() #this generates a random float between 0.0 - 1.0
random.uniform(4, 100) # this generates random float numbers in the range in paranthesis
random.randint(1, 100) # to generate a random int btw the range in paranthesis
random.randrange(10, 400, 5) # this return random numbers between 10 and 400 in steps of 5


#we can also use random in loops, i.e to generate 100 random numbers

for i in range(100):
    random.randint(5, 1000)

#another usecase is to choose a random number from a non empty sequence
l1 = list('adfgfjhlkkj;kl[')
random.choice(l1)

# we can also have another element that draws 5 element from l1
#random.sample(population, number of samples) 
random.sample(l1, 4)

# another useful function is shuffle() it shuffles a sequence in place

l2 = ['abcdefg']
random.shuffle(l2)

# there is a class called system random which offers an alternative generator it uses the os.urandom() function that generates random numbers from sources provided by the operaating system 
# anyways it could not be available on all systems

r = random.SystemRandom()
r.random()
r.randint(5,10)

#we can assume that the values directly above are somehow more random