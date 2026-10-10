def Marvellous_MSE(Y_true,Y_Pred):
    n = len (Y_Pred)
    total_error = 0

    for i in range(n):
        error = Y_true[i] - Y_Pred[i]
        total_error = total_error + (error **2)

    MSE = total_error / n
    return MSE    

Y_true = [10,20,30]
Y_Pred = [12,18,33]

loss = Marvellous_MSE(Y_true,Y_Pred)

print("loss is :",loss)

