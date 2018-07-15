import aiohttp
from . import db, exceptions


class Server(object):
    """ A CouchDB server (contains a session, with connection pool) """
    def __init__(self, url="http://localhost:5984", auth=None):
        self._client = aiohttp.ClientSession(auth=auth)
        self._url = url
        

    async def infos(self):
        async with self._client.get(self._url) as resp :
            return await resp.json()

    async def has_db(self, name):
        async with self._client.head(self._url + '/' +  name) as resp :
            return resp.status == 200
        
    async def get_db(self, name, create=False):
        """ returns a db, create it if does not exists """
        exists = await self.has_db(name)
        base_url = self._url + '/' + name
        if not exists :
            if create:
                async with self._client.put(base_url) as r :
                    assert(r.status == 201)
            else :
                raise exceptions.NoSuchDatabase("%s does not exists", name)
            
        return db.Database(self, name, base_url)

    async def delete_db(self, name):
        await self._client.delete(self._url + '/' + name)
        
            
                                        
