# brainfuck-plus

A version of the BrainFuck language that allows for easier debugging,
completely open-source and written in Python.

In addition to the standard BrainFuck syntax, I have added a ninth character--
the `@`, which prints the index (starting at 0) of the current cell. (Get it?
It prints where you're AT!). But I did not want my interpreter to break all
your previous code that contains `@` in the comments, so I did not include this
feature as default. There are three ways to invoke the special behavior:

```python
python bfp.py <path/to/bf/file> [--at|--easy|-e]
```

...because, yes, this does make coding in BrainFuck MUCH easier by letting you
know where you are.

But this also allows more creative programs using BrainFuck, which is why there
is the flag that says `--at`--because BrainFuck was never meant to be easy in
the first place. So before you start hatin' on this new feature, think about
all that you couldn't do with BrainFuck which you now will be able to do. And
then, go do all that!