# speech-to-text-evaluator
evaluating output from Google Speech-To-Text using the ACE2 metric vs the traditional WER metric for caption-understandability 

BACKGROUND
===============

The *ACE-framework* has three main components:

a. **Word Importance Model**: This model is responsible for scoring each word in a sentence with the importance score.

b. **Semantic Distance Model**: This model computes the distance between reference or hypothesis word (or phrases).

c. **Error Combination Model**: The word importance model and the semantic distance model is used compute the impact of each error (using a weighing parameter `alpha`). The individual error impact scores are then combined using the error combination model to get the single final score for the sentence.

	individual_error_impact_score = alpha * word_importance + (1 - alpha) * semantic_distance
	ace_score = error_combination_model(individual_error_impact_scores)

So, the software makes use of these components to produce the ACE quality evaluation score. There are two version of the metrics derived from the ACE-framework: ACE metric and ACE2 metric. The ACE metric is the original metric described in ASSETS'17 paper: Kafle and Huenerfauth, 2017. The ACE2 metric is the newly updated metric based on new studies (See `/reference` folder)
