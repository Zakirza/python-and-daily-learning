import pickle

class modeltrainer:
    def __init__(self, model, accuracy):
        self.model=model
        self.accuracy=accuracy

    def display(self):
        print(f"the model is {self.model} and the accuracy is {self.accuracy}")

# model=modeltrainer("Random Forest",97.44) 
# with open("pickle.pkl","wb") as file:
#     pickle.dump(model,file)

with open("pickle.pkl","rb") as file:
    loaded_model=pickle.load(file)

loaded_model.display()


