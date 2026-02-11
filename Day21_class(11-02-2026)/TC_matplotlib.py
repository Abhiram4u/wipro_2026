import matplotlib.pyplot as plt

# plt.plot([1,2,3],[4,5,6])
# plt.show()
#
# s = [1,2,3,4]
# y = [10,20,25,30]
#
# plt.scatter(s,y)
# plt.show()
#
# plt.plot(s,y,marker='0',linestyle='------')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Line Chart")
# plt.grid(True)
# plt.show()
#
# names = ["A","B","C"]
# scores = [80,90,100]
# plt.bar(names,scores)
# plt.title("Student Scores")
# plt.show()
#
# plt.barh(names,scores)
# plt.show()



# marks = [50,60,80,70,77,86]
# plt.hist(marks,bins=5)
# plt.title("Marks")
# plt.show()

labels = ["Chrome","Firefox","Opera"]
sizes = [60,25,15]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Browser usage")
plt.show()