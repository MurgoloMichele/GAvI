# true_pos = len(relevant & retrieved)
# true_neg = [len(total) - len(relevant | retrieved)]
# false_pos = len(retrieved - relevant)
# false_neg = len(relevant - retrieved)

class PrecisionRecall:

    def __init__(self):
        self.type = "PrecisionRecall"
        
    def precision(self, relevant, retrieved):
        precision = len(set(relevant) & set(retrieved)) / len(retrieved)
        return precision

    def recall(self, relevant, retrieved):
        recall = len(set(relevant) & set(retrieved)) / len(relevant)
        return recall
