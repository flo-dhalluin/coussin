# Coussin : async couchdb python client

Since [aiocouchdb](https://github.com/aio-libs/aiocouchdb) seems stalled ( does not support a decent version of aiohttp, and couchdb 2), I started a rewrite, based on aiohttp 3. 

So far that's just a minimal PoC lib. Do not use. 

## example 

```python

from coussin.server import Server

server = Server()
db = await server.get_db("test", create=True)
await db.update_document("someid", {"message": "test"})
data = await db.get_document("someid")
```

## todo 

- auth 
- indexes 
- all the couchdb goodies ( sharding, replication ... )

