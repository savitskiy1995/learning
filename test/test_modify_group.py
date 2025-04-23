from model.group import Group

def test_modify_group_name(app):
    if app.group.count_name_symbols == 0:
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_name(app):
    if app.group.count_name_symbols != 0:
    app.group.modify_first_group(Group(name=None))






#def test_modify_group_header(app):
#   app.group.modify_first_group(Group(name="New header"))

#def test_modify_group_footer(app):
#    app.group.modify_first_group(Group(name="New footer"))


