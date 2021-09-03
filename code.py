import plotly.figure_factory as ff 
import pandas as pd  
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["Math_score"].to_list()
fig = ff.create_distplot([data], ["Math Score"])
fig.show()

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean

meanlist = []
for i in range(0, 1000):
    setOfMeans = randomSetOfMean(100)
    meanlist.append(setOfMeans)

mean = statistics.mean(data)
stdev = statistics.stdev(meanlist)

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)

fig2 = ff.create_distplot([meanlist], ["MEAN OF MEANLIST"])

fig2.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation Start"))
fig2.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation End"))
fig2.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation Start"))
fig2.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation End"))

fig2.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig2.show()

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df2 = pd.read_csv("data1.csv")
data2 = df2["Math_score"].to_list()
mean_Offirst_intervention = statistics.mean(data2)
fig3 = ff.create_distplot([meanlist], ["Math Score 1"])
fig3.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN OF POPULATION(DATA1)"))
fig3.add_trace(go.Scatter(x = [mean_Offirst_intervention, mean_Offirst_intervention], y = [0, 0.17], mode = "lines", name = "MEAN OF 1st Intervention"))

fig3.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation Start"))
fig3.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation End"))
fig3.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation Start"))
fig3.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation End"))

fig3.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df3 = pd.read_csv("data2.csv")
data3 = df3["Math_score"].to_list()
mean_Offirst_intervention = statistics.mean(data2)
fig4 = ff.create_distplot([meanlist], ["Math Score 2"])
fig4.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN OF 2nd Intervention"))
fig4.add_trace(go.Scatter(x = [mean_Offirst_intervention, mean_Offirst_intervention], y = [0, 0.17], mode = "lines", name = "MEAN OF 2nd Intervention"))

fig4.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation Start"))
fig4.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation End"))
fig4.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation Start"))
fig4.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation End"))

fig4.show()

df4 = pd.read_csv("data3.csv")
data4 = df4["Math_score"].to_list()
mean_Offirst_intervention = statistics.mean(data2)
fig3 = ff.create_distplot([meanlist], ["Math Score 3"])
fig3.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN OF POPULATION(DATA1)"))
fig3.add_trace(go.Scatter(x = [mean_Offirst_intervention, mean_Offirst_intervention], y = [0, 0.17], mode = "lines", name = "MEAN OF 3rd Intervention"))

fig3.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation Start"))
fig3.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "1 Standard Deviation End"))
fig3.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation Start"))
fig3.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "2 Standard Deviation End"))

fig3.show()

#finding the z score using the formula z_score = (mean - mean_of_sample2)/std_deviation print("The z score is = ",z_score)