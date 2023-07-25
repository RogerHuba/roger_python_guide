class GameLogic:
    @staticmethod
    def calculate_score(dice):
        """
        Computes the score of a list of dice in Farkle.
        The input should be a list of integers representing the dice rolls (between 1 and 6).

        Returns the total score as an integer.
        """

        # count the occurrences of each die value
        counts = [0] * 7  # 7 to simplify indexing, since dice are numbered 1 to 6
        for d in dice:
            counts[d] += 1

        score = 0

        # check for triples and higher
        for i in range(1, 7):
            if counts[i] >= 3:
                counts[i] -= 3  # remove the triple from the counts
                score += i * 100  # score the triple
                # if i == 1:
                #     score += 700  # bonus for triple ones
                # elif i == 5:
                #     score += 350  # bonus for triple fives

        # check for remaining ones and fives
        score += counts[1] * 100
        score += counts[5] * 50

        # check for a straight
        if counts[1] == 1 and counts[2] == 1 and counts[3] == 1 and counts[4] == 1 and counts[5] == 1 and counts[6] == 1:
            score += 1500

        return score