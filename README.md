# Toilet

See [the wiki page](https://wiki.apap04.com/wiki/Toilet) for more general public info.

## Developer stuff

Hello! Welcome to the repo of the Toilet bot. This README will house all the developer stuff that developers need to know. Let's start!

### Hosting

Toilet is hosted on Google Cloud Platform using App Engine. You can use whatever host you want but you'll have to configure everything youreslf since some files here are meant for GCP.

### Running the bot

To run the bot, you must specify a token. If you know how to do this stuff, you can just hardcode a token. But if you're running a public repository, you might have to specify a token locally so you don't have any hassle with leaking tokens.

#### Linux instuctions

1. Define TOKEN

```bash
$ export TOKEN=<token>
```

2. Run the bot

```bash
$ python3 main.py --log info
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
