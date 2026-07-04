#PART C: Working with Data using Dicts(i.e. dictionaries)
#dataset is represented as a list of dicts.

def apply_transform(dataset, M):

    transformed_dataset = []

    for point in dataset:

        x = point["x"] #getting original values of x,y from every dictionary.
        y = point["y"]

        new_x = M[0][0] * x + M[0][1] * y  #getting the new values by multiplying the original values with matrix M
        new_y = M[1][0] * x + M[1][1] * y

        new_point = {     # new Dict containing the transformed values
            "x": new_x,
            "y": new_y
        }

        transformed_dataset.append(new_point)

    return transformed_dataset
dataset = [
    {"x": 2, "y": 3},
    {"x": -1, "y": 4},
    {"x": 0, "y": -2},
    {"x": 5, "y": 1}
]
M=[[1,1],[0,1]]
print(dataset[0]["x"]) #how to access such data in the dataset using both indexing and key.
print(f"The dataset after applying transformation is {apply_transform(dataset,M)}") 


"""C.2. Write a function pariwise_distances(dataset) that returns a dict mapping (i, j) pairs to the Euclidean distance 
between point i and j. Compute each pair only once (i.e. only where i < j)"""


''''dataset = [
    {"x": 2, "y": 3}, //...> I considered this as point 0 
    {"x": -1, "y": 4},//...>........................point 1
    {"x": 0, "y": -2},//........>point 2
    {"x": 5, "y": 1} //..........>point3   the condition of choosing pair of points as (i<j) is to help us avoid duplicate i.e distance from point 0 to pint 1 is same as the distance from point 1 to point 0
]'''
def pairwise_distances(dataset):
    distances={}
    for i in range(len(dataset)):
        for j in range(i+1,len(dataset)):
            x1=dataset[i]["x"] #picking the first point coordinates
            y1=dataset[i]["y"]

            x2=dataset[j]["x"] #picking the next point
            y2=dataset[j]["y"]

            #Now we can compute the distance between these two points
            distance=((x2-x1)**2+(y2-y1)**2)**0.5 
            distances[(i,j)]=distance
    return distances
   
print(pairwise_distances(dataset))


'''C.3 Apply the transformation matrix T from Part B to the dataset, then compare 
pairwise distances before and after the transformation. Print a short summary: 
are distances preserved? What does this suggest about information loss?'''

#Methodology: given transformation matrix T=[[2,0],[1,1]] ,I am going to apply this transformation to the dataset
#with help of apply_transform() method , after I get a transformed dataset, I will then compute the Euclidean distance btn pair 
#of points using pairwise_distances() method and then compare with the one found before transformation.
T=[[2,0],[1,1]]
newDataset=apply_transform(dataset,T) #new Dataset obtained after tranforming original dataset by matrix T
print("The distances btn pairs of points for dataset after transformation")
print("---------------------------------------------------------------------")
print(pairwise_distances(newDataset))
newDataset=apply_transform(dataset,T) #new Dataset obtained after tranforming original dataset by matrix T
print("The distances btn pairs of points for dataset before transformation")
print("---------------------------------------------------------------------")
print(pairwise_distances(dataset))

#Interpretation
outcome='''The pairwise distances are not preserved after the transformation. Every pair of points has a different distance 
compared to the original dataset. This indicates that the transformation changes the geometry of the data by stretching or compressing the space. 
Therefore, the original spatial relationships 
between points are not fully preserved, suggesting some loss of geometric information.'''

print(outcome)

