# mdlatex

1. Install pandoc
2. Add `compile.py` to your path and make it chmoddable
3. Follow the example in the repositry and run compile

Or in more detail

3. For any project create a `config` file where the first line is the name of the project e.g. `ijcai2015` and the remaining lines are the `md` files stored in `md`.
5. Get the latex files for the conference and convert it into a template, by putting $body$ where you want your text to code - see `ijcai2015.template`
6. run `compile`, press enter many times
7. Two pdfs will be created, one in `pandoctex` and one in `ijcai2015`