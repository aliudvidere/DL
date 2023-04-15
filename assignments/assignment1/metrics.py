def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i]:
            accuracy += 1
    accuracy /= len(prediction)

    k = 0
    for i in range(len(prediction)):
        if prediction[i] == True and ground_truth[i] == True:
            precision += 1
        if prediction[i] == True and ground_truth[i] == False:
            k += 1
    precision = precision / (precision + k)

    k = 0
    for i in range(len(prediction)):
        if prediction[i] == True and ground_truth[i] == True:
            recall += 1
        if prediction[i] == False and ground_truth[i] == True:
            k += 1
    recall = recall / (recall+ k)

    f1 = 2 * recall * precision / (recall + precision)
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return 0
