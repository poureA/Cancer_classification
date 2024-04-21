from tkinter import Tk , Entry , Button , Label 
from pickle import load
root = Tk()
features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
Row = 1
entry_widgets = list()
key = True
for i in range(len(features)):
    if 0<=i<=14:
        if key :
            lbl = Label(text=f'Enter {features[i]}:',font=(20))
            lbl.grid(row=i+1,column=1)
            entry = Entry(font=(5),bg='sky blue')
            entry.grid(row=i+1,column=2,ipadx=50,ipady=5)
            entry_widgets.append(entry)
            key = False
        else :
            lbl = Label(text=f'Enter {features[i]}:',font=(20))
            lbl.grid(row=i+1,column=1)
            entry = Entry(font=(5))
            entry.grid(row=i+1,column=2,ipadx=50,ipady=5)
            entry_widgets.append(entry)
            key = True
    else :
        if key:
            lbl = Label(text=f'Enter {features[i]}:',font=(20))
            lbl.grid(row=Row,column=3,ipady=5)
            entry = Entry(font=(5),bg='sky blue')
            entry.grid(row=Row,column=4,ipadx=50,ipady=5)
            Row+=1
            entry_widgets.append(entry)
            key = False
        else:
            lbl = Label(text=f'Enter {features[i]}:',font=(20))
            lbl.grid(row=Row,column=3,ipady=5)
            entry = Entry(font=(5))
            entry.grid(row=Row,column=4,ipadx=50,ipady=5)
            Row+=1
            entry_widgets.append(entry)
            key = True
def Do():
    lst = []
    for e in entry_widgets:
        lst.append(float(e.get()))
    with open("D:\\datasets\\cancer_classification\\model_CatBoostClassifier.pkl",'rb') as file:
        model = load(file)
        pred = model.predict([lst])
    if pred[0]==0:
        result = Label(text='Benign',bg='white',font=(10))
        result.grid(row=33,column=3,ipadx=40,ipady=10)
        return result
    else :
        result = Label(text='Malignant',bg='white',font=(10))
        result.grid(row=33,column=3,ipadx=40,ipady=10)
        return result
button = Button(text='Predict',bg='yellow',command=Do)
button.grid(row=32,column=3,ipadx=40,ipady=10)
result = Label(bg='white')
result.grid(row=33,column=3,ipadx=40,ipady=10)
root.title('Cancer_classification_(predictor)')    
root.mainloop()
