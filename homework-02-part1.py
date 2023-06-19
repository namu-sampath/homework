#Namu Sampath
#June 8, 2023
#homework 02, part 01

#lists! 
#list of numbers 
num = [22,90,0,-10,3,22,48]
#length of numbers 
n = len(num)
print(len(num))
#fourth number in the list
print(num[3])
#sum of 2nd and 4the element of the list
print(num[1]+ num[3])
#second largest value in the list
#sort numbers from smallest to biggest
#remove repeated numbers
num_2 = [-10, 0, 3, 22, 48, 90]
print(num_2[4])
#last element of original unsorted list
print(num[-1])
#sum of all numbers divided by 2 
total = sum(num)
print(total/2)
#is the median or mean of the numbers higher?
# formula for mean
# sum of values divided by number of values
mean = (total/n)
print("The mean is", mean)
# median is the middle number in a group of numbers
# sort the list in ascending order
sorted(num)
print(sorted(num))
import statistics
sorted(num)
median = statistics.median(num)
print("The median is", median)

if int(median) < int(mean): 
    print("The mean is higher than the median.")
else:
    print("The median is higher than the mean.")

#dictionaries! 
movie = {'title': 'Moonlight',
        'year': 2016,
        'director': 'Barry Jenkins'
}
print("My favorite movie is", movie['title'], 
    "which was released in", movie['year'],
    "and was directed by", movie['director'])

movie_in_millions = {'budget': 4, 'revenue': 65.2}
print("The budget for", movie['title'], "was", movie_in_millions['budget'],
      "million dollars and the revenue was", movie_in_millions['revenue'], "million dollars.")
#finding the difference between the revenue and budget for the film
difference = (movie_in_millions['revenue'] - movie_in_millions['budget'])
print("The difference between the revenue and budget was", difference, "million dollars.")
#was the film a good investment? 
if movie_in_millions['budget'] > movie_in_millions['revenue']: 
    print("That was a bad investment.")
if movie_in_millions['revenue'] > (5 * movie_in_millions['budget']):
    print("That was a great investment.")
else:
    print("That was an okay investment.")

#dictionary of NYC's population by borough
population = {'manhattan':1.6, 
                   'brooklyn': 2.6,
                   'bronx': 1.4,
                   'queens': 2.3,
                   'staten island': 0.47                   
                   }
print("The population of Brooklyn is", population['brooklyn'], 'million people.')
#total population of all five boroughs
pop_sum = population['manhattan'] + population['bronx'] + population['brooklyn'] + population['queens'] + population['staten island']
print("The combined population of all five boroughs is", pop_sum, "million people.")

#what percent of people live in manhattan? 
manhattan_percent = (round((population['manhattan']/pop_sum),2)*100)
print(manhattan_percent, "%", "of NYC's population lives in Manhattan.")



