a_votes = int(input("Enter the number of votes for candidate A: "))
b_votes = int(input("Enter the number of votes for candidate B: "))
c_votes = int(input("Enter the number of votes for candidate C: "))

total_votes = a_votes + b_votes + c_votes

percent_a = int(a_votes/total_votes * 100)
percent_b = int(b_votes/total_votes * 100)
percent_c = int(c_votes/total_votes * 100)

print(f"Candidate A received {percent_a}% of the votes.")
print(f"Candidate B received {percent_b}% of the votes.")
print(f"Candidate C received {percent_c}% of the votes.")
