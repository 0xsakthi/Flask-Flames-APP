from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST','GET'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = 'sakthi'
        operation = request.form['operation']

    if operation =='Flames':
       num1 = num1.lower()
       num2 = num2.lower()
       num1 = num1.replace(" ","")
       num2 = num2.replace(" ","")
       for i in num1:
       	for j in num2:
       		if i == j:
       			num1 = num1.replace(i,"",1)
       			num2 = num2.replace(j,"",1)
       			break
       count = len(num1) + len(num2)
       if count>0:
       	list1 = ["'FRIENDS'👬","'LOVERS'❤️","'AFFECTION'💌","'MARRIAGE'💍","'ENEMIES'👿","'SIBILINGS'🙊"]
       	while len(list1)>1:
       		c = count%len(list1)
       		s_index = c-1
       		if s_index>=0:
       			left = list1[:s_index]
       			right = list1[s_index+1:]
       			list1 = right+left
       		else:
       			 list1 = list1[:len(list1)-1]
       sum = list1[0]
       return render_template('app.html', sum=sum)


if __name__ == ' __main__':
    app.debug = True
    app.run()
