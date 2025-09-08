To calculate the best possible word for wordle there are two seperate metrics:  
For the first word chosen, and some subsequent words, we want to select the word that is not most likely
but rather gives us the greatest possible information on what the hidden word actually is  
After a series of 2-3 guesses the word should be extremely apparent, at which point the word chosen should instead be the most likely word to be chosen

An additional complication is that the lexicon of words that can be guessed is significantly larger than the lexicon of words that are possible answers
so a threshold should be applied on possible guesses vs possible answers to allow the bot to use obscure words to gain information
whilst only trying for real valid answers
This shall be solved for later

TODO:
-
1. Remove the probabilistic bias from the bot based on word frequency [✔]
2. Create a metric for information gathered from each word as a guess [✔]
   1. Calculate the probability of a given result when the word is guessed [✔]
   2. Calculate the information gathered from each given result [✔]
   3. Calculate an expected information value from the guess given both option [✔]
3. Present the highest information option to the user []
4. Take in the result []
5. Recalculate based on the new information []
6. When only one answer is possible present the option as the final answer []
7. Make the bot's CLI resilient to user input []

Future Expansion:
-
- Trim the guess list to only assume possible answers that are of a certain frequency in English
- GUI