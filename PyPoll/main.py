import csv

total_votes = 0
candidates = []
percent_of_vote = 0
vote_by_candidate = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
tooley_vote = 0
pop_vote_winner = ""

with open("election_data.csv", "r") as elect_data:
    csvreader = csv.reader(elect_data)
    header = csvreader.__next__()
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote += 1
        elif row[2] == "Li":
            li_vote += 1 
        else:
            tooley_vote += 1
khan_percent = float(khan_vote / total_votes)
correy_percent = float(correy_vote / total_votes)
li_percent = float(li_vote / total_votes)
tooley_percent = float(tooley_vote / total_votes)

if (khan_percent > correy_percent) & (khan_percent > li_percent) & (khan_percent > tooley_percent):
    pop_vote_winner = "Khan"
elif correy_percent > khan_percent & correy_percent > tooley_percent & correy_percent > li_percent:
    pop_vote_winner = "Correy"
elif li_percent > khan_percent & li_percent > correy_percent & li_percent > tooley_percent:
    pop_vote_winner = "Li"
else:
    pop_vote_winner = "Tooley"



print ("Total number of Votes: {}".format(total_votes))
print ("Khan won {:.3%} ({})".format(khan_percent, khan_vote)) 
print ("Correy won {:.3%} ({})".format(correy_percent, correy_vote))
print ("Li won {:.3%} ({})".format(li_percent, li_vote))
print ("O\'Tooley won {:.3%} ({})".format(tooley_percent, tooley_vote))
print ("By popular vote, ", pop_vote_winner, " is the winner of the election")

elect_results = open("election_results.txt","w+")

print ("Total number of Votes: {}".format(total_votes),file = elect_results)
print ("Khan won {:.3%} ({})".format(khan_percent, khan_vote), file = elect_results) 
print ("Correy won {:.3%} ({})".format(correy_percent, correy_vote), file = elect_results)
print ("Li won {:.3%} ({})".format(li_percent, li_vote), file = elect_results)
print ("O\'Tooley won {:.3%} ({})".format(tooley_percent, tooley_vote), file = elect_results)
print ("By popular vote, ", pop_vote_winner, " is the winner of the election", file = elect_results)

elect_results.close()