import data_manager


# appending the story datas with a new form
#
# @form_data: list string
# @data: list of list
def add_row_to_stories(form_data, data):
    data_length = len(data)
    form_data.insert(0, str(data_length))
    data_manager.append_datatable_to_file("data/story.csv", form_data)
    data = data_manager.get_datatable_from_file("data/story.csv")
    return  data

# updating a story form by ID
#
# @form_data: list string
# @data: list of list
def update_row(form_data, data):
    for idx, row in enumerate(data):
        if row[0] == form_data[0]:
            data[idx] = form_data
    data_manager.write_datatable_to_file("data/story.csv", data)
    data = data_manager.get_datatable_from_file("data/story.csv")
    return  data


# @form_data: list string
def handle_button_request(form_data):
    button_request = []
    for key, value in form_data.items():
        button_request.append(key)
        button_request.append(value)
    return button_request


# delete story form by ID from the story datas
#
# @form_data: list string
# @id_story: string
def delete_data_row(data, id_story):
    new_data = [row for row in data if row[0] != id_story]
    for idx, row in enumerate(new_data):
        if row[0].isnumeric():
            new_data[idx][0] = str(idx)
    data_manager.write_datatable_to_file("data/story.csv", new_data)
    return new_data
