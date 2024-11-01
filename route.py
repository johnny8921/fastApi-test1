
@app.get('auth/login')
async def login():
    pass

@app.get ('auth/logout')
async def logout():
    pass


@app.get('auth/users/{}object_id}/change-password')
async def change_password(object_id:int):
    pass

@app.get('auth/users/{object_id}')
async def user(object_id: int):
    pass

@app.get('auth/users')
async def user_list():
    pass

@app.get('access-areas/{object_id}')
async def access_area(object_id): #uuid
    pass

@app.get('access-areas')
async def access_area_list():
    pass

@app.get('access-structure')
async def access_structure():
    pass

@app.get('employees/{uuid}')
async def employees(uuid: int): #uuid
    pass
@app.get('employees')
async def employees_list():
    pass

@app.get('controllers/{uuid}')
async def controllers(uuid: str): #uuid
    pass
@app.get('controllers')
async def controllers_list():
    pass

@app.get('events')
async def events():
    pass

@app.get('schedules/{schedule_number}')
async def schedules(schedule_number: int):
    pass
@app.get('schedules')
async def schedules_list():
    pass

@app.get('access-keys/{access_key_uuid}')
async def access_keys(access_key_uuid: str):
    pass
@app.get('access-keys')
async def access_keys_list():
    pass

@app.get('presets/{preset_uuid}')
async def presets(preset_uuid: str):
    pass
@app.get('presets')
async def presets_list():
    pass

@app.get('remote-armed')
async def remote_armed():
    pass

@app.get('remote-firealarm')
async def remote_firealarm():
    pass

@app.get('remote-commands')
async def remote_commands():
    pass

@app.get('export/reports')
async def reports():
    pass

@app.get('export/reports/t13')
async def reports_t13():
    pass

@app.get('export/database')
async def export_database():
    pass

@app.get('export/access-keys')
async def export_access_keys():
    pass

#
# 'info/version'
# '1c/employees-add-few'
# '1c/set-1c-info'
# '1c/report-cards-xml'
