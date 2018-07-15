from asynctest import TestCase
from coussin.server import Server
from coussin import exceptions

class TestCoussin(TestCase):

    async def setUp(self):
        self.server = Server()
        self.db = await self.server.get_db("test_coussin", create=True)

    async def tearDown(self):
        await self.server.delete_db("test_coussin")
        
    async def test_get_infos(self):
        infos = await self.server.infos()
        print("running",infos)
        self.assertEquals("Welcome", infos["couchdb"])

    async def test_docs(self):
        """ nominal case """
        dat = await self.db.create({"msg": "test"})
        document = await self.db.get(dat["id"])
        self.assertEquals("test", document["msg"])
        r = await self.db.update(dat["id"],
                                 {"msg": "test2"},
                                 rev=dat["rev"])                

        document = await self.db.get(dat["id"])
        self.assertEquals("test2", document["msg"])

        self.assertAsyncRaises(exceptions.DocumentConflicts,
                               self.db.update(dat["id"], {"msg": "test3"}))
