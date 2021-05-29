import glob
import os

nonzero_scores = []
high_scores= []
total_scores = 0
path = 'impact_scores'
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        print("Reading ", filename, "...")
        text = f.readlines()
        for line in text:
            segments = line.strip().split()
            if len(segments) > 1 and segments[0] == "IMPACT:":
                score = float(segments[1])
                total_scores += 1
                if score > 0:
                    nonzero_scores.append(score)
                if score > 0.5:
                    high_scores.append(score)
        print("Impacted phrases: ", round(len(nonzero_scores) * 100 / total_scores, 2))
        print("Highly impacted phrases: ", round(len(high_scores) * 100 / total_scores, 2))

