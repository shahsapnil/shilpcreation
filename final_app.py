from flask import Flask,render_template,request
from num2words import num2words

# for selenium automation part to get addresspipre
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
# from selenium.webdriver.chrome.options import Options  # for suppressing the browser

# option = webdriver.ChromeOptions()
# option.headless =True
# driver = webdriver.Chrome(r"D:\automation\browser\chromedriver.exe",options=option)


app= Flask(__name__)

@app.route("/")
def index():
    return render_template('details.html')

@app.route('/register', methods=['GET','POST'])
def register():
    inumber=''
    date=''
    pname=''
    gnumber=''
    address=''

    if request.method=='POST':
        inumber=request.form.get('inumber')
        date=request.form.get('date')
        pname=request.form.get('pname').upper()
        gnumber=request.form.get('gnumber')
        address=request.form.get('address').upper()
        data=request.form


        def is_float(value):
            try:
                float(value)
                return True
            except:
                return False


        mainlist=[]
        for i,j in data.items():
            list1=[]
            list1.append(i)
            if j.isdigit() or is_float(j):
                k=float(j)
                list1.append(k)
            else:
                list1.append(j)
            mainlist.append(list1)
        # print(mainlist)
        finallist=[]
        passlist=[]
        for i in range(5,len(mainlist)):
            if mainlist[i][1]!='':
                finallist.append(mainlist[i][1])
        i = 3
        j=0
        while (i <= len(finallist)):
            passlist.append(finallist[j:i])
            i+=3
            j+=3
        print(passlist)
        qty=0
        total=0
        for i in passlist:
            qty+=i[1]
            total+=i[1]*i[2]
            
        igst=(total*5)/100
        finaltotal=total+igst

        textfinal=num2words(finaltotal).capitalize()
        textigst=num2words(igst).capitalize()

        # driver.get("https://www.mastersindia.co/gst-number-search-and-gstin-verification/")

        # search = driver.find_element_by_xpath('//*[@id="gstin-search-form"]/div/div/input')

        # search.send_keys(gnumber,Keys.ENTER)
        # data = driver.find_element_by_xpath('/html/body/main/section[3]/div/div/div/table/tbody/tr/td[3]')
        # address=data.text.upper()



        # print(inumber)
        # print(date)
        # print(pname)
        # print(gnumber)
        # print(address)
        

        return render_template('invoice.html',name=pname,inumber=inumber,date=date,pname=pname,gnumber=gnumber,address=address,passlist=passlist,qty=qty,finaltotal=finaltotal,igst=igst,textfinal=textfinal,total=total,textigst=textigst)

        # pdf=pdfkit.from_string(invoice,False)
        # response=make_response(pdf)
        # response.headers['Content-Type']='application/pdf'
        # response.headers['Content-Disposition']='inline; filename=output.pdf'
    

    # return render_template('invoice.html')

if __name__=="__main__":
    app.run(debug=True)
