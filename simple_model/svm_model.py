#Import svm model
import pandas, numpy
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def calculate(train_data, test_data):
    data = train_data.drop(columns=["Unnamed: 0"])
    X = data.drop(columns=["simplified.significance"])
    Y = data["simplified.significance"]

    # scaler = MinMaxScaler(feature_range=(0, 1))
    # rescaledX = scaler.fit_transform(X)

    scaler = StandardScaler().fit(X)
    rescaledX = scaler.transform(X)

    # Create a svm Classifier
    clf = svm.SVC(kernel='linear')  # Linear Kernel

    # Train the model using the training sets
    clf.fit(rescaledX, Y)
    test_data = test_data.drop(columns=["Unnamed: 0"])
    X_test = test_data.drop(columns=["simplified.significance"])
    Y_test = test_data["simplified.significance"]
    # Predict the response for test dataset
    y_pred = clf.predict(X_test)
    accuracy = metrics.accuracy_score(Y_test, y_pred)
    #print("Accuracy:", accuracy)
    mean_accuracy.append(accuracy)



file = "simplified_only_benign_and_pathogenic.csv"
original_data = pandas.read_csv(file)

kf = KFold(n_splits = 10, shuffle = True, random_state = 2)

mean_accuracy = []
splits = kf.split(original_data)
for split in splits:
    train = original_data.iloc[split[0]]
    test = original_data.iloc[split[1]]
    calculate(train, test)

mean = numpy.mean(mean_accuracy)
st_dev = numpy.std(mean_accuracy)

print("Mean accuracy ", mean)
print("Standard deviation ", st_dev)