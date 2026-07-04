"""B. 1. Writting a function mat_vec_multiply(M, v) that multiplies a 2 x 2 matrix M by a 2D vector v and 
returns the resulting vector. Use loops only."""

def mat_vec_multiply(M,v):
    resultVect=[]
    for i in range(2):
        for j in range(1):
            x=(M[i][j]*v[0]+M[i][j+1]*v[1]) #here I took each element of matrix M and multiplied it by v
            resultVect.append(x)
    return resultVect

#writing down a given matrix 
M=[[2,1],[0,3]]
v=[2,1]
print(f"The product of matrix {M} and vector {v} results into {mat_vec_multiply(M,v)}")

"""B.2. Write a function mat_mat_multiply(A, B) that multiplies two 2 x 2 matrices
and returns a 2 x 2 result as a list of lists."""
"""def mat_mat_multiply(A,B):
    result_mat=[]
    for i in range(2):
        for j in range(2):
            if i==0 and j==0:
                x=(A[i][j]*B[i][j]+A[i][j+1]*B[i+1][j]) #this statement is for computing the matrix multiplication
                result_mat.append(x)
            if i==0 and j==1:
                x=(A[i][j-1]*B[i][j]+A[i][j]*B[i+1][j])
                result_mat.append(x)
            if i==1 and j==0:
                x=(A[i][j]*B[i-1][j]+A[i][j+1]*B[i][j])
                result_mat.append(x)   
            if i==1 and j==1:
                x=(A[i][j-1]*B[i-1][j]+A[i][j]*B[i][j])
                result_mat.append(x) 
    return result_mat """

def mat_mat_multiply(A, B):
    result = []

    for i in range(2):          # Looping through rows of A
        row = []                # Creating a new row for the result

        for j in range(2):      # Looping through columns of B
            value = 0           # Initializing the sum

            for k in range(2):  # Multiplying corresponding elements
                value = value + A[i][k] * B[k][j]

            row.append(value)   # Adding the computed value to the current row

        result.append(row)      # Adding the completed row to the result

    return result


A=[[1,2],[1,1]]
B=[[2,2],[2,3]]
print(f"the product of matrix A={A} and B={B} is {mat_mat_multiply(A,B)}") 

#B.3. Write a function determinant(M) that computes the determinant of a 2 x 2 matrix.

def determinant_matrix(M):
    det=(M[0][0]*M[1][1]-M[0][1]*M[1][0])
    return det

M=[[2,3],[1,4]]
print(f"The determinant of matrix {M} is {determinant_matrix(M)}")


#B.4 Applying the transformation from mastery challenge 01 to the given basis vectors
# we do have basis Vectors: e1 and e2 defined as follow:

T=[[2,0],[1,1]] #given transformation matrix
e1=[1,0]
e2=[0,1]
print(f"The matrix {T} transforms vector {e1} into {mat_vec_multiply(T,e1)}")
print(f"The matrix {T} transforms vector {e2} into {mat_vec_multiply(T,e2)}")
#Observation: I have realized the above transformation made by matrix T is truly the same as the one I got in matery challenge 01, e1 is transformed,
#  while e2 remained unchanged after transformation which implies that e2 is a special vector (i.e. an eigen vector)

