from . import exceptions

class Database(object):

    def __init__(self, server, name, base_url):
        self._server = server
        self._name = name
        self._base_url = base_url


    def get_doc_url(self, docid) :
        return self._base_url + '/' + docid
    async def create(self, data):
        async with self._server._client.post(self._base_url, json=data) as r:
            return await r.json()

    async def update(self, docid, data, rev=None):
        """ create, or update a doc with a given id 
            achtung: if the doc exists, you must provide a rev """
        doc_url = self.get_doc_url(docid)
        headers = {}
        if rev :
            headers["If-Match"] = rev
        async with self._server._client.put(doc_url, json=data, headers=headers) as r :
            if(r.status == 409) :
                raise exceptions.DocumentConflicts("conflicts")
            
            return await r.json()
        
    async def get(self, docid):
        doc_url = self.get_doc_url(docid)
        async with self._server._client.get(doc_url) as r:
            return await r.json()
            

    
