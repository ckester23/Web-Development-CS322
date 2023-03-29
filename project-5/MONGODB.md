# MongoDB basics

This markdown covers basic MongoDB commands.

## Install
You can install Mongo locally, but it is not recommended.
We want to utilize docker as much as possible, and this could be one way.

Instead of referring to the [MongoDB manual](https://www.mongodb.com/docs/manual/tutorial/getting-started/) 
for [install instructions](https://www.mongodb.com/docs/manual/installation/),
we can simply set a Mongo container running:

```
docker run -d -p 27017:27017 mongo:5.0.5
```

You'll notice we're still doing detached mode (`-d`), and that's because Mongo, just like any other service
needs to run in the background because we don't want it taking over our terminal.

We're also binding port `27017`, which is MongoDB's default port, to the same port on our local machine.
This is just for the sake of simplicity.

**NOTE:** if you're using docker on a server shared with others, you might want to bind to a different port 
to prevent collisions.

Once your container is up and running, you're good to go! You now have MongoDB running on your system
at port `27017`! And you didn't have to spend time figuring out how to install it. And later you wouldn't waste a breath
figuring out how to get rid of it.

## GUI
[MongoDB Compass](https://www.mongodb.com/products/compass) is a GUI front end designed to help developers explore their
databases and collections. You're going to want to install this one locally if you want, but it's a personal choice
and not a requirement.

Once you set it up, all you have to do is enter the "connection string", which is typically in the following form:
```
mongodb://user:password@localhost:9999/
```
The username and password refer to the database user, which you wouldn't have to worry about if you're using Docker.
So if you are using docker, and you have Mongo listening to port `27017`, this would be your connection string:
```
mongodb://localhost:27017/
```

**NOTE:** replace `localhost` with domain name or IP address if you're running the container on a server.

## Mongo shell
[Mongo shell](https://www.mongodb.com/docs/v4.4/mongo/) is an interactive interface to MongoDB, 
and typically is installed alongside the service. 
If you installed MongoDB locally (without docker), you should be able to run:

```
mongo
```

to enter mongo shell.
If you are using docker, start an interactive shell in your container:

```
docker exec -it $CONTAINER_ID /bin/bash
```

and then run

```
mongo
```

Or directly start a mongo shell:

```
docker exec -it $CONTAINER_ID /usr/bin/mongo
```

### Basic commands

List of databases:

```
show dbs
```

Select database `brevets`:

```
use brevets
```

### Database commands
Once you've selected a database, you can use the following commands (if you don't select a database, it might default to a
database named `test`):

```
db.getName()
```

To DROP (delete) the database:

```
db.dropDatabase()
```

**NOTE:** databases that don't exist are created as soon as a collection exists within them.
So you could select a database that does not exist, and don't have to worry about deleting it if you change your mind.

To see collections (tables) in the database:

```
db.getCollectionNames()
```

### Collection commands
Assume we're still using database `brevets`, and now want to interact with a collection named `races` inside it.

To insert a document (row / record) into `races`:

```
db.races.insert({...})
```

For example:

```
db.races.insert({title: "Euro 23", location: "Europe", start_location: "Paris", end_location: "Marseille", year: 2023})
```

To read (SELECT) data from the collection:

```
db.races.find()
```

Limit the number of documents read:

```
db.races.find().limit(5)
```

Limit to one document:

```
db.races.findOne()
```

To drop (remove) collection:

```
db.races.drop()
```

### Querying
Both `find` and `fineOne` allow you to pass a query JSON. This allows you to search for documents with specific fields.

For example, suppose we want to find all documents in `races` where `start_location` is `"Paris"`:

```
db.races.find({start_location:"Paris"})
```

Or all documents with `year` greater than 2020:

```
db.races.find({year:{$gt:2020}})
```

Useful operators:
* `$lt`: <
* `$gt`: >
* `$lte`: <=
* `$gte`: >=
* `$ne`: !=

Arrays:
* `$in`: is in array
* `$nin`: is not in array

Regex:
* `$regex`

You can also count documents matching your query:
```
db.races.count({year:{$gt:2020}})
```

**NOTE:** empty query is just `{}`.

#### Querying using `where`:

```
db.races.find({$where: 'this.year > 2020'})
```

### Updating documents
Using queries, you can select and delete specific documents:

```
db.races.remove({title: "Euro 23"})
```

or just update them:

```
db.races.update({title: "Euro 23"}, {start_location: "Monte Carlo"})
```

the above command changes `start_location` in all documents with `title` set to `Euro 23` to `Monte Carlo`.
