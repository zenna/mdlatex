# mdlatex

`mdlatex` makes it more convenient to use markdown to create latex for journal or conference submissions.

1. Install pandoc
2. Add `compile.py` to your path and make it executable with chmod (you may have to change the first line if your python is not in `/usr/bin`)
3. Follow the example in the repository and run `compile.py`

Or in more detail:

1. For any project create a `config` file where the first line is the name of the project e.g. `ijcai2015` and the remaining lines are the `md` files stored in `md`.
2. Get the latex files for the conference and convert it into a template, by putting $body$ where you want your text to be - see `ijcai2015.template`
3. run `compile.py`, press enter many times
4. Two pdfs will be created, one in `pandoctex` and one in `ijcai2015`