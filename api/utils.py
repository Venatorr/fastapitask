def model2dict(model):
    '''
    Преобразование объекта модели в словарь
    '''
    d = {}
    for column in model.__table__.columns:
        d[column.name] = str(getattr(model, column.name))
    return d
