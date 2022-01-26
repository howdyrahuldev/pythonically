from flask import Flask, request, render_template, redirect, send_file
import sqlite3, os

app = Flask(__name__)
active_id = "###THIS@@IS$$INACTIVE%%%"
app_root = os.path.dirname(os.path.abspath(__file__))+"\\attachments\\"


def profile_exists(id):
    con = sqlite3.connect('my-profile-database.db')
    cursorObj = con.cursor()
    cursorObj.execute(r'SELECT * FROM profiles WHERE eid=?', (id,))
    data = cursorObj.fetchall()
    con.commit()
    con.close()
    print(data)
    return len(data)


def connect_auth(id,passw,flag):
    con = sqlite3.connect('my-auth-database.db')
    cursorObj = con.cursor()
    if flag == 'verify':
        cursorObj.execute(r'SELECT password FROM userauth where eid=?',(id,))
        try:
            passw1 = cursorObj.fetchall()[0][0]
            status = (passw == passw1)
        except:
            status = "not registered"
        con.commit()
        con.close()
        print(status)
        return status

    elif flag == 'register':
        try:
            cursorObj.execute(r"INSERT INTO userauth VALUES(?,?)",(id,passw))
            con.commit()
            con.close()
            return 'Bingo!!!! You have registered successfully.'
        except:
            return "You had already registered previously."


def verify_profile_data(id):
    con = sqlite3.connect('my-profile-database.db')
    cursor = con.cursor()
    cursor.execute(r'SELECT * FROM profiles WHERE eid=?', (id,))
    profile_details = cursor.fetchall()
    con.commit()
    con.close()
    print(profile_details)
    return profile_details


def get_profile_data(id):
    if len(verify_profile_data(active_id)) > 0:
        return verify_profile_data(active_id)[0]
    else:
        return "0"


def profile_database_update(name,email,website,cover_letter,love_work,file_name):
    con = sqlite3.connect('my-profile-database.db')
    cursorObj = con.cursor()
    try:
        cursorObj.execute(r"INSERT INTO profiles VALUES(?,?,?,?,?,?)",(email, name, website, cover_letter, love_work, file_name))
        print('done')
    except:
        cursorObj.execute(r"UPDATE profiles SET name = ?, site = ?, cover = ?, lovework = ?, file = ? WHERE eid = ?", (name, website, cover_letter, love_work, file_name, email))
        print('updated')
    con.commit()
    con.close()

@app.route("/")
def first_page():
    return redirect('/register')


@app.route('/register')
def get_register_page():
    return render_template('/register.html')


@app.route("/profile-change")
def get_profile_change():
    if active_id == "###THIS@@IS$$INACTIVE%%%":
        return render_template('/no-login.html')
    else:
        if profile_exists(active_id) == 0:
            return render_template('/update.html', email=active_id)
        else:
            return render_template("/change.html", email=active_id)


@app.route("/profile-change", methods=['POST'])
def post_profile_change():
    profile_data = get_profile_data(active_id)

    file_name = profile_data[5]

    name = request.form['name']
    email = active_id
    website = request.form['website']
    cover_letter = request.form['cover-letter']
    love_work = request.form['love-working']
    try:
        os.remove(app_root + file_name)
    except:
        pass
    attachment = request.files['attachment']
    file_name = f'{file_name.split(".")[0]}.{attachment.filename.split(".")[1]}'
    attachment.save(app_root + file_name)
    profile_database_update(name, email, website, cover_letter, love_work, file_name)
    return  render_template("/profile-updated.html")


@app.route('/register', methods=['POST'])
def register():
    id = request.form['email']
    password = request.form['pass']
    return render_template('/message-register.html' , message=connect_auth(id,password,'register'))


@app.route('/login')
def login():
    return render_template('/login.html')


@app.route('/login', methods=['POST'])
def login_check ():
    id = request.form['email']
    password = request.form['pass']
    if connect_auth(id,password,'verify') == "not registered":
        return render_template('/failure.html')

    elif connect_auth(id,password,'verify'):
        global active_id
        active_id = id
        if len(verify_profile_data(active_id)) > 0:
            profile_data = ("View Your Details", "/my-profile")
        else:
            profile_data = ("Update Your Details", "/update-profile")

        return render_template('/success.html', text=profile_data[0], href=profile_data[1])

    else:
        return render_template('/failure.html')


@app.route('/my-profile')
def my_profile():
    if active_id == "###THIS@@IS$$INACTIVE%%%":
        return render_template('/no-login.html')
    else:
        profile_data = get_profile_data(active_id)
        if profile_data == "0":
            return redirect("/update-profile")
        else:
            name = profile_data[1]
            website = profile_data[2]
            cover_letter = profile_data[3]
            if profile_data[4] == "Yes":
                love_work = "Loves to work."
            else:
                love_work = " Doesn't love to work."
            file_name = profile_data[5]
            file_url = "/attachments/"+file_name
            return render_template('/profile.html', email=active_id, name=name, love_work=love_work, website=website,
                                   cover=cover_letter, attachment=file_name, href="/file-download/"+file_name)


@app.route("/file-download/<file_name>")
def file_download(file_name):
    return send_file(app_root+file_name)


@app.route('/logout')
def logout():
    global active_id
    active_id = "###THIS@@IS$$INACTIVE%%%"
    return redirect('/login')


@app.route('/update-profile')
def profile_update_view():
    if active_id == "###THIS@@IS$$INACTIVE%%%":
        return render_template('/no-login.html')
    else:
        if profile_exists(active_id) == 0:
            return render_template('/update.html', email=active_id)
        else:
            return render_template('/already-updated.html')


def get_all_data(id):
    con = sqlite3.connect('my-profile-database.db')
    cursor = con.cursor()
    cursor.execute(r'SELECT * FROM profiles')
    profile_details = cursor.fetchall()
    con.commit()
    con.close()
    print(profile_details)
    if len(profile_details) > 0:
        return profile_details[-1][-1]
    else:
        return "0.abc"


@app.route('/update-profile', methods=["POST"])
def dump_profile_to_database():
    name = request.form['name']
    email = active_id
    website = request.form['website']
    cover_letter = request.form['cover-letter']
    love_working = request.form['love-working']
    attachment = request.files['attachment']
    verifier = get_all_data(active_id)
    print("verifier is ",verifier)
    if len(verifier) == 0:
        file_name = f"0.{attachment.filename.split('.')[1]}"
    else:
        temp = int(verifier.split('.')[0])+1
        print(temp)
        file_name = f"{temp}.{attachment.filename.split('.')[1]}"
    attachment.save(app_root+file_name)
    profile_database_update(name, email, website, cover_letter, love_working, file_name)
    return render_template('/profile-updated.html')


app.run(host="0.0.0.0", port=5000)