from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime
import string

app = Flask(__name__)

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\Oracle\instantclient_21_13")
dsn = cx_Oracle.makedsn("bd-dc.cs.tuiasi.ro", 1539, service_name="orcl")
con = cx_Oracle.connect(
    user="bd066",
    password="bd066",
    dsn=dsn
)



# employees begin code
@app.route('/')
@app.route('/angajati')
def angaj():
    employees = []

    cur = con.cursor()
    cur.execute('select * from angajati')
    for result in cur:
        print(result)
        employee = {}
        employee['employee_id'] = result[0]
        employee['first_name'] = result[1]
        employee['last_name'] = result[2]
        employee['pozitie'] = result[3]
        employee['hire_date'] = datetime.strptime(str(result[4]), '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%y')
        employee['salary'] = result[5]

        employees.append(employee)
    cur.close()
    return render_template('employees.html', employees=employees)


@app.route('/addEmployee', methods=['GET', 'POST'])
def add_angaj():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(ID_angajat) from Angajati')
        for result in cur:
            emp = result[0]
        cur.close()
        emp = emp + 1 if emp is not None else 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")

        values.append("'" + request.form['first_name'] + "'")
        values.append("'" + request.form['last_name'] + "'")
        values.append("'" + request.form['pozitie'] + "'")
        values.append("'" + datetime.strptime(str(request.form['hire_date']), '%d.%m.%Y').strftime('%d-%b-%y') + "'")
        values.append("'" + request.form['salary'] + "'")

        fields = ['ID_angajat', 'nume_angajat', 'prenume_angajat', 'pozitie', 'data_angajarii', 'salariu']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('angajati', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/angajati')
    else:
        job = []
        cur = con.cursor()
        cur.execute('select distinct(pozitie) from angajati')
        for result in cur:
            print(result)
            job.append(result[0])
        cur.close()

        return render_template('addEmployee.html', Jobs=job)


@app.route('/delEmployee', methods=['POST'])
def del_emp():
    emp = request.form['employee_id']
    cur = con.cursor()
    cur.execute('delete from angajati where ID_angajat=' + emp)
    cur.execute('commit')
    return redirect('/angajati')


@app.route('/getEmployee', methods=['POST'])
def get_emp():
    emp = request.form['employee_id']
    cur = con.cursor()
    cur.execute('select * from angajati where ID_angajat=' + emp)

    emps = cur.fetchone()
    employee_id = emps[0]
    first_name = emps[1]
    last_name = emps[2]
    pozitie = emps[3]
    hire_date = datetime.strptime(str(emps[4]), '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y')
    salary = emps[5]
    cur.close()

    job = []
    cur = con.cursor()
    cur.execute('select distinct(pozitie) from Angajati')
    for result in cur:
        job.append(result[0])
    cur.close()

    return render_template('editEmployee.html', jobs=job, job_id=pozitie, first_name=first_name, last_name=last_name,
                           hire_date=hire_date, salary=salary)


@app.route('/editEmployee', methods=['POST'])
def edit_emp():
    emp = 0
    cur = con.cursor()

    first_name = "'" + request.form['first_name'] + "'"
    last_name = "'" + request.form['last_name'] + "'"
    cur.execute('select ID_angajat from angajati where prenume_angajat=' + last_name)
    for result in cur:
        emp = result[0]
    cur.close()

    hire_date = "'" + datetime.strptime(str(request.form['hire_date']), '%d.%m.%Y').strftime('%d-%b-%y') + "'"

    job_id = "'" + request.form['job_id'] + "'"
    salary = request.form['salary']
    cur = con.cursor()
    query = "UPDATE angajati SET nume_angajat=%s, prenume_angajat=%s, pozitie=%s, data_angajarii=%s, salariu=%s where ID_angajat=%s" % (
        first_name, last_name, job_id, hire_date, salary, emp)
    cur.execute(query)
    cur.execute('commit')
    return redirect('/angajati')


# employees end code
# -----------------------------------------#
# -----------------------------------------#
# furnizor start code
@app.route('/furnizor', methods=['GET', 'POST'])
def furnizori():
    counselors = []

    cur = con.cursor()
    cur.execute('select * from furnizor')
    for result in cur:
        counselor = {}
        counselor['id_furnizor'] = result[0]
        counselor['nume_furnizor'] = result[1]
        counselor['telefon_furnizor'] = result[2]

        counselors.append(counselor)
    cur.close()
    return render_template('furnizor.html', counselors=counselors)

@app.route('/delFurnizor', methods=['POST'])
def del_furn():
    emp = request.form['id_furnizor']
    cur = con.cursor()
    cur.execute('savepoint furn_save')
    cur.close()
    cur = con.cursor()
    cur.execute('delete from furnizor where ID_furnizor=' + emp)
    return redirect('/furnizor')


@app.route('/undoDelFurnizor', methods=['POST'])
def undo_del_furn():
    cur = con.cursor()
    cur.execute('rollback to furn_save')
    cur.execute('commit')
    return redirect('/furnizor')


# furnizor end code
# -----------------------------------------#


# -------------------------------------------#
# produse start code
@app.route('/produse')
def produse():
    counselors = []

    cur = con.cursor()
    cur.execute('select * from produse')
    for result in cur:
        counselor = {}
        counselor['id_produs'] = result[0]
        counselor['denumire_produs'] = result[1]
        counselor['pret'] = result[2]
        counselor['stoc'] = result[3]
        counselor['id_furnizor_fk'] = result[4]

        counselors.append(counselor)
    cur.close()
    com = []
    cur = con.cursor()
    cur.execute('select id_furnizor from furnizor')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()
    return render_template('produse.html', counselors=counselors, products=com)


@app.route('/ADDprodus', methods=['POST'])
def ad_prod():
    error = None
    if request.method == 'POST':
        loc = 0
        cur = con.cursor()
        cur.execute('select max(id_produs) from produse')
        for result in cur:
            loc = result[0]
        cur.close()
        loc = loc + 1 if loc is not None else 1
        cur = con.cursor()
        values = []
        values.append("'" + str(loc) + "'")
        values.append("'" + request.form['denumire_produs'] + "'")
        values.append("'" + request.form['pret'] + "'")
        values.append("'" + request.form['stoc'] + "'")
        values.append("'" + request.form['id_furnizor_fk'] + "'")
        fields = ['id_produs', 'denumire_produs', 'pret','stoc', 'furnizor_id_furnizor']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'produse',
            ', '.join(fields),
            ', '.join(values)
        )

        cur.execute(query)
        cur.execute('commit')
        return redirect('/produse')
@app.route('/delprodus', methods=['POST'])
def del_prod():
    cnp = request.form['id_produs']
    cur = con.cursor()
    cur.execute('delete from produse where id_produs=' + cnp)
    cur.execute('commit')
    return redirect('/produse')


# produse end code
# -----------------------------------------#


# -----------------------------------------#
# detaliiclient start code
@app.route('/detaliiclient')
def det_client():
    counselors = []

    cur = con.cursor()
    cur.execute('select * from detalii_client')
    for result in cur:
        counselor = {}
        counselor['id_info'] = result[0]
        counselor['id_client'] = result[1]
        counselor['adresa'] = result[2]
        counselor['data_nasterii'] = datetime.strptime(str(result[3]), '%Y-%m-%d %H:%M:%S').strftime('%d-%b-%y')
        counselor['gen'] = result[4]
        counselor['email'] = result[5]

        counselors.append(counselor)
    cur.close()
    return render_template('detaliiclient.html', counselors=counselors)


@app.route('/addDetClient', methods=['GET', 'POST'])
def add_det_client():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(id_informatii) from detalii_client')
        for result in cur:
            emp = result[0]
        cur.close()
        cur = con.cursor()

        cur.execute('select id_client from client where nume_client like(\''+request.form['id_client']+'\')')
        for result in cur:
            auxiliar2 = result[0]
        cur.close()
        emp = emp + 1 if emp is not None else 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")
        values.append("'" + str(auxiliar2) + "'")
        values.append("'" + request.form['adresa'] + "'")
        values.append(
            "'" + datetime.strptime(str(request.form['data_nasterii']), '%d.%m.%Y').strftime('%d-%b-%y') + "'")
        values.append("'" + request.form['gen'] + "'")
        values.append("'" + request.form['email'] + "'")

        fields = ['id_informatii', 'client_id_client', 'adresa', 'data_nasterii', 'gen', 'email']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('detalii_client', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/detaliiclient')
    else:
        job = []
        cur = con.cursor()
        cur.execute('select nume_client from client where id_client not in(select client_id_client from detalii_client)')
        for result in cur:
            print(result)
            job.append(result[0])
        cur.close()

        return render_template('addDetClient.html', Jobs=job)


# detaliiclient end code
# -----------------------------------------#
# -----------------------------------------#
# client start code
@app.route('/client')
def client():
    counselors = []
    cur = con.cursor()
    cur.execute('select * from client')
    for result in cur:
        counselor = {}
        counselor['id_client'] = result[0]
        counselor['nume_client'] = result[1]
        counselors.append(counselor)
    cur.close()
    # -------------
    return render_template('client.html', counselors=counselors)


@app.route('/addClient', methods=['GET', 'POST'])
def ad_client():
    error = None
    if request.method == 'POST':
        loc = 0
        cur = con.cursor()
        cur.execute('select max(id_client) from client')
        for result in cur:
            loc = result[0]
        cur.close()
        loc = loc+ 1 if loc is not None else 1
        conv_loc = str(loc)
        cur = con.cursor()
        values = []
        values.append("'" + conv_loc + "'")
        values.append("'" + request.form['nume_client'] + "'")
        fields = ['id_client', 'nume_client']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'client',
            ', '.join(fields),
            ', '.join(values)
        )
        cur.execute(query)
        cur.execute('commit')
        return redirect('/client')


@app.route('/delClient', methods=['POST'])
def del_client():
    cnp = "'" + request.form['id_client'] + "'"
    auxiliar = 0
    cur = con.cursor()
    cur.execute('delete from detalii_client where client_id_client=' + cnp)
    cur.execute('commit')
    cur.close()
    cur = con.cursor()
    cur.execute('select max(pret_comanda) from client, comanda where client_id_client=' + cnp)
    for result in cur:
        auxiliar = result[0]
    cur.close()
    if auxiliar == None:
        auxiliar = 0
    print(auxiliar)

    cur = con.cursor()
    if auxiliar != 0:
        cur.execute('UPDATE Client SET nume_client = \'UNKNOWN\' where id_client=' + cnp)
    else:
        cur.execute('delete from client where id_client=' + cnp)
    cur.execute('commit')
    return redirect('/client')


# client end code
# -----------------------------------------#
# -----------------------------------------#
# comanda start code
@app.route('/comanda')
def comanda():
    comenzi = []

    cur = con.cursor()
    cur.execute('select * from comanda')
    for result in cur:
        comanda = {}
        comanda['id_comanda'] = result[0]
        comanda['data_comanda'] = result[1]
        comanda['angajati_id_angajat'] = result[2]
        comanda['client_id_client'] = result[3]
        comanda['pret_comanda'] = result[4]

        comenzi.append(comanda)
    cur.close()
    emp = []
    cur = con.cursor()
    cur.execute('select nume_angajat from angajati where pozitie like(\'livrator\')')
    # import pdb;pdb.set_trace()
    for result in cur:
        emp.append(result[0])
    cur.close()

    loc = []
    cur = con.cursor()
    cur.execute('select id_client from client')
    # import pdb;pdb.set_trace()
    for result in cur:
        loc.append(result[0])
    cur.close()
    return render_template('comanda.html', comenzi=comenzi, employees=emp, clients=loc)


@app.route('/addComanda', methods=['GET', 'POST'])
def ad_com():
    error = None
    if request.method == 'POST':
        dep = 0
        cur = con.cursor()
        cur.execute('select max(id_comanda) from comanda')
        for result in cur:
            dep = result[0]
        cur.close()
        dep = dep + 1 if dep is not None else 1
        cur = con.cursor()
        cur.execute('select id_angajat from angajati where nume_angajat like(\''+request.form['angajati_id_angajat']+'\')')
        for result in cur:
            auxiliar2 = result[0]
        cur.close()

        cur = con.cursor()
        values = []
        values.append("'" + str(dep) + "'")
        values.append("'" + request.form['data_comanda'] + "'")
        values.append("'" + str(auxiliar2) + "'")
        values.append("'" + request.form['client_id_client'] + "'")
        fields = ['id_comanda', 'data_comanda', 'angajati_id_angajat', 'client_id_client']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'comanda',
            ', '.join(fields),
            ', '.join(values)
        )

        cur.execute(query)
        cur.execute('commit')
        return redirect('/comanda')


@app.route('/delComanda', methods=['POST'])
def del_com():
    dep = request.form['id_comanda']

    auxiliar = 0
    cur = con.cursor()
    cur.execute('select pret_comanda from comanda where id_comanda=' + dep)
    for result in cur:
        auxiliar = result[0]
    cur.close()
    if auxiliar != 0:
        cur = con.cursor()
        cur.execute('UPDATE relation_prod_com SET cantitate = 0 where comanda_id_comanda=' + dep)
        cur.execute('delete from relation_prod_com where comanda_id_comanda=' + dep)
        cur.execute('commit')
        cur.close()

    cur = con.cursor()
    cur.execute('delete from comanda where id_comanda=' + dep)
    cur.execute('commit')
    return redirect('/comanda')


# comanda end code
# ------------------------------------------#

# -----------------------------------------#
# relation start code
@app.route('/relatie')
def relation():
    rel_prod_com = []

    cur = con.cursor()
    cur.execute('select * from relation_prod_com')
    for result in cur:
        comanda = {}
        comanda['produse_id_produs'] = result[0]
        comanda['comanda_id_comanda'] = result[1]
        comanda['cantitate'] = result[2]
        rel_prod_com.append(comanda)
    cur.close()
    comand = []
    cur = con.cursor()
    cur.execute('select id_comanda from comanda')
    # import pdb;pdb.set_trace()
    for result in cur:
        comand.append(result[0])
    cur.close()

    prod = []
    cur = con.cursor()
    cur.execute('select id_produs from produse')
    # import pdb;pdb.set_trace()
    for result in cur:
        prod.append(result[0])
    cur.close()
    return render_template('relatie.html', comenzi=rel_prod_com, employees=comand, clients=prod)


@app.route('/addRelCom', methods=['POST'])
def ad_rel_com():
    error = None
    if request.method == 'POST':
        rez = []
        job = request.form['comanda_id_comanda']
        cur = con.cursor()
        cur.execute(
            'SELECT DISTINCT(id_produs) FROM produse LEFT JOIN relation_prod_com ON produse.id_produs = relation_prod_com.produse_id_produs AND relation_prod_com.comanda_id_comanda = :job WHERE relation_prod_com.produse_id_produs IS NULL',
            job=job)
        for result in cur:
            rez.append(result[0])
        cur.close()
        return render_template('addRelation.html', comenzi=job, id_prod=rez)


@app.route('/addRel', methods=['GET', 'POST'])
def ad_rel():
    error = None
    if request.method == 'POST':
        cur = con.cursor()
        values = []
        values.append("'" + request.form['id_produs'] + "'")
        values.append("'" + request.form['comenzi'] + "'")
        values.append("'" + request.form['cantitate'] + "'")

        fields = ['produse_id_produs', 'comanda_id_comanda', 'cantitate']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('relation_prod_com', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/relatie')


@app.route('/getRel', methods=['POST'])
def get_rel():
    emp = request.form['id_relatie']
    emp = emp.replace('(', '')
    emp = emp.replace(')', '')

    print(emp)
    aux = emp.split(", ")
    print("alt")
    print(aux)
    cur = con.cursor()
    auxiliar = 0
    cur.execute(
        'select cantitate from relation_prod_com where produse_id_produs=' + aux[1] + ' and comanda_id_comanda=' + aux[
            0])
    for result in cur:
        auxiliar = result[0]
    print(auxiliar)

    return render_template('editRelation.html', id_prod=aux[1], id_com=aux[0], cantitate=auxiliar)


@app.route('/modRel', methods=['POST'])
def mod_rel():
    prod = "'" + request.form['id_produs'] + "'"
    comanda = "'" + request.form['id_com'] + "'"
    quant = "'" + request.form['cantitate'] + "'"
    cur = con.cursor()
    query = "UPDATE relation_prod_com SET cantitate=%s where comanda_id_comanda=%s and produse_id_produs=%s" % (
        quant, comanda, prod)
    cur.execute(query)
    cur.execute('commit')
    return redirect('/relatie')


# relation end code
# ------------------------------------------#
# main
if __name__ == '__main__':
    app.run(debug=True)
    con.close()
