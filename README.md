# Toilet

See [the wiki page](https://wiki.apap04.com/wiki/Toilet) for more general public info.

## Developer stuff

Hello! Welcome to the repo of the Toilet bot. This README will house all the developer stuff that developers need to know. Let's start!

### Hosting

Toilet is hosted on Google Cloud Platform using App Engine. You can use whatever host you want but you'll have to configure everything youreslf since some files here are meant for GCP.

### Running the bot

To run the bot, you must specify a token. If you know how to do this stuff, you can just hardcode a token. But if you're running a public repository, you might have to specify a token locally so you don't have any hassle with leaking tokens.

#### Starting the bot

1. Copy the example json file and edit the values accordingly.
2. Install your packages: `python3 -m pip install -r requirements.txt`
3. OPTIONAL: Enable genius integration:
   1. Make a new API client on [Genius API clients](https://genius.com/api-clients)
   2. On Linux, do `$ export GENIUS_TOKEN=<your token>`
   3. On Windows, do `$ set GENIUS_TOKEN=<your token>`

4. Run the bot!

```bash
$ python3 main.py
```

### Contributing

How to contribute to the project...

Step 1... fork then clone the repo!

```bash
$ git clone git@github.com:username/toilet.git # using ssh just because :p
```

step 2, get your environment setup. use venv if you want to.

```bash
$ export TOKEN=<token>
$ pip3 install -r requirements.txt
```

step 3, checkout a new branch

```bash
$ git checkout -b my-epic-change # branch name should be either issue TL-/# or anything that relates to an issue
```

step 4, make a change.

```patch
- async def unreasonable_change(ctx):
+ async def reasonable_change(ctx):
+    await ctx.send("hi")
```

step 5, test changes then push to repo.

```bash
$ python3 main.py --log info
[...] # output!
^C

$ git add <file>
$ git commit -m "i changed this for issue #69"
$ git push
```

step 6, make pr. go to main repo > pr > new pr (compare with fork, base to dev) > add details and submit! (also ping apap)
