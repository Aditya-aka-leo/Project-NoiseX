inputs = np.array([[random()/2 for _ in range(2)]for _ in range(1000)])
    targets = np.array([[i[0]+ i[1] for i in inputs]])
    mlp = MLP(2,[5],1)
    mlp.train(inputs,targets,50,0.1)