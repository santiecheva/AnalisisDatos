import xmlrpc.client

url = 'http://52.55.183.90:8069'
db = 'rave'
username = 'josealejandroeche@gmail.com'
password = 'Rave.Agencia2008'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


ids = models.execute_kw(db, uid, password,
    'crm.lead', 'search',
    [[['partner_id', '=', 10991]]])

print(len(ids))

for id in ids:
    models.execute_kw(db, uid, password, 'crm.lead', 'write', [[id], {
        'partner_id': 5337
    }])
    models.execute_kw(db, uid, password, 'crm.lead', 'name_get', [[id]])