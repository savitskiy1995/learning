from model.group import Group

def delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()