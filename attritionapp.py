from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import pygal
import seaborn as sns
import matplotlib.pyplot as plt
import io
from io import BytesIO
import base64
from io import StringIO 
model = pickle.load(open('attr.pkl', 'rb'))

app=Flask(__name__)


@app.route('/input', methods=['POST','GET'])
def input():
    if request.method=="POST":
        msg=""
        at=[0]*21
        detail=request.form
        at[0]=int(detail['uage'])
        at[4]=int(detail['ugender'])
        at[1]=int(detail['udepartment'])
        at[9]=int(detail['mstatus'])
        at[3]=int(detail['ueducation'])
        at[7]=int(detail['urole'])
        at[6]=int(detail['ujlevel'])
        at[2]=int(detail['udistance'])
        at[16]=float(detail['uwork'])
        at[11]=int(detail['unwork'])
        at[18]=float(detail['ucompany'])
        at[19]=float(detail['ucrole'])
        at[20]=float(detail['ulpromotion'])
        at[10]=float(detail['umincome'])
        at[12]=float(detail['uhpercentage'])
        at[5]=int(detail['uinvolvement'])
        at[8]=int(detail['usatisfaction'])
        at[14]=int(detail['ursatisfaction'])
        at[13]=int(detail['uprating'])
        at[15]=int(detail['uslevel'])
        at[17]=int(detail['uwbalance'])

        prediction=model.predict([at])
        if prediction==0:
            msg="The eomployee will stay in the company"
        else:
            msg="The employee will leave the company"

        data=pd.read_csv("Attrition.csv")
        img = StringIO()
        #sns.countplot(x='JobRole',hue='Attrition',data=data)
        plt.plot(data['Attrition'],data['MonthlyIncome'])
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot=base64.b64encode(img.getvalue())
        return render_template('output.html',msg=msg,plot=plot)







@app.route('/')
def submit():
    return render_template('input 6.html')

if __name__ == '__main__':
    app.run(debug=True)