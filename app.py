from flask import Flask
from flask import render_template, request, jsonify
import re
from calculator.controller import CalculatorController
from members.controller import MemberController

app = Flask(__name__)

@app.route("/")
def hello_world():
    ctrl = MemberController()
    ctrl.create_table()
    return render_template('intro.html')

@app.route("/cabbage", methods=['GET','POST'])
def predict_cabbage():
    # 컨트롤러가 가져온 값
    result = 6000
    render_params = {}
    render_params['result'] = result
    return render_template('cabbage.html', **render_params)

@app.route("/login", methods=['POST'])
def login():
    print('로그인 들어옴')
    userid = request.form['userid']
    password = request.form['password']
    print('userid %s'%(userid))
    print('password %s' % (password))
    ctrl = MemberController()
    view = ctrl.login(userid, password)
    return render_template(view)

@app.route("/move/<path>")
def move(path):
    return render_template('{}.html'.format(path))

@app.route("/ui_calc")
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else:
        print('넘어온 식 {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자 {}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            result = n1 / n2

    return jsonify(result = result)



@app.route('/ai_calc', methods=["POST"])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    c = CalculatorController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = int(result)
    return render_template('ai_calc.html', **render_params)



if __name__ == '__main__':
    app.run()
