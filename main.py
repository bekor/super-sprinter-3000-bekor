from flask import Flask, render_template, request
import data_manager
import common

app = Flask(__name__)

#NEM KEZELTED LE HA ID nincs a databazbe
@app.route('/story', methods=['GET', 'POST'])
@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def story(story_id=None):
    default_list = ["", "", "", "", 1000, 2.5, ""]
    data = data_manager.get_datatable_from_file("data/story.csv")
    if request.method == 'POST':
        button_data = common.handle_button_request(request.form)
        if button_data and button_data[0] == "editrow":
            update_list = data[int(button_data[1])]
            return render_template("form.html.j2", form_data=update_list)
        else:
            return render_template("form.html.j2", form_data=default_list)
    else:
        default_list[0] = str(story_id)
        if story_id:
            story_id_list = data[story_id]
            return render_template("form.html.j2", form_data=story_id_list)
        return render_template("form.html.j2", form_data=default_list)


@app.route('/', methods=['GET', 'POST'])
@app.route('/list', methods=['GET', 'POST'])
def data_table():
    data = data_manager.get_datatable_from_file("data/story.csv")
    if request.method == 'POST':
        dict_data_form = request.form
        form_data = []
        if len(dict_data_form) < 3:
            form_data = common.handle_button_request(dict_data_form)
            if form_data and form_data[0] == "deleterow":
                new_data = common.delete_data_row(data, form_data[1])
                return render_template("list.html.j2", data=new_data)
        elif len(dict_data_form) >= 3:
            form_data = common.handle_requestform(dict_data_form)
            if form_data[6] == "Create":
                data = common.add_row_to_stories(form_data[:6], data)
            elif form_data[6]:
                form_data.insert(0, str(form_data[6][6:]))
                data = common.update_row(form_data[:7], data)
            return render_template("list.html.j2", data=data)
        else:
            return render_template("form.html.j2", data=data)
    return render_template("list.html.j2", data=data)


if __name__ == '__main__':
    app.run(debug=True)
