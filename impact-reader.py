import glob
import os
import math

path = 'impact_scores'

for filename in glob.glob(os.path.join(path, '*.txt')):
    nonzero_scores = []
    high_scores = []
    impact_scores_sub_errors = []
    total_scores = 0

    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        print("Reading ", filename, "...")
        text = f.readlines()

        # In the code, a portion represents the impact evaluation of a single line in a transcript. A line represents
        # a line in an impact evaluation i.e. a file ending in "_impact.txt", not a line in the transcript itself
        portions = 1
        sub_error_in_portion = False
        for line in text:
            segments = line.strip().split()
            if len(segments) > 1 and segments[0] == "****":
                sub_error_in_portion = True
                print("Substitution error in line " + str(portions) + " of transcript")
            if len(segments) > 1 and segments[0] == "IMPACT:":
                score = float(segments[1])
                total_scores += 1
                if score > 0:
                    nonzero_scores.append(score)
                if score > 0.5:
                    high_scores.append(score)
                if sub_error_in_portion:
                    impact_scores_sub_errors.append(score)
            if len(segments) == 1 and segments[0] == "====================":
                sub_error_in_portion = False
                print("End line " + str(portions))
                portions += 1
                print("Start line " + str(portions))
        print("Total phrases: ", total_scores)
        print("Impacted phrases: ", len(nonzero_scores))
        print("Highly impacted phrases: ", len(high_scores))
        print("% Impacted phrases: ", round(len(nonzero_scores) * 100 / total_scores, 2))
        print("% Highly impacted phrases: ", round(len(high_scores) * 100 / total_scores, 2))
        print("Mean impact score for phrases with substitution errors: ",
              sum(impact_scores_sub_errors) / len(impact_scores_sub_errors))
