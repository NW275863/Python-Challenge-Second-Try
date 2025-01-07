import csv

with open('election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    votes = list(readCSV)
    total_votes = len(votes) - 1
candidates = {}

for row in votes[1:]:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

for candidate, vote_count in candidates.items():
    percentage = (vote_count / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({vote_count})')
  winner = max(candidates, key=candidates.get)

print(f'Winner: {winner}')
print(f'Total Votes: {total_votes}')
