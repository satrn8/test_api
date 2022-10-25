from voluptuous import Schema


create = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})

update_put = Schema({
    "name": str,
    "job": str,
    "updatedAt": str
})

update_patch = Schema({
    "name": str,
    "job": str,
    "updatedAt": str
})