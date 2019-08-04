# Memorizing Python.  Why?  How?

### Deciding to learn Python

In mid-2018 I decided to learn Python.

At work, our team was replacing our legacy data system, which used Ruby, with
one that used Python, based on Airflow.  That provided me with the standard job
motivation to learn Python.  However, my interest in Python was really piqued
after digging deeper into its ecosystem and registering its exceptional
ubiquity, library support, improvement methodology, and trajectory.

First, I noticed Python's ubiquity.  I saw Python in many places I hadn't
noticed it before.  It is used as the scripting language for cool graphics
applications like [Blender](https://www.blender.org/) and
[Inkscape](https://inkscape.org/develop/extensions/).  It is embedded in my
editor, Vim.  I also learned it is the most popular language in the world (I had
assumed that was JavaScript).  I realized that with a better understanding of
Python, I could use many tools I already use, or want to use, in more powerful
ways.

I saw that the library support was also exceptionally good, even out of the
box.  Python has "batteries included".  Many libraries are already built
directly into the standard library, so you can accomplish many things without
needing to reach out of the language for 3rd party tools.  I realized that
Python would be an excellent tool to reach for when doing my day-to-day
scripting, because I would be able to pull in many libraries so easily.  I came
to understand that Python, despite being so similar to Ruby, would actually be
a preferable daily driver language, in part because I was doing more data work,
and in part because of its library support.  But what really hooked me was its
trajectory and improvement process, both of which made it clear to me that a
long-term investment would be rewarded.

In the past I had shied away from Python because its trajectory felt unclear to
me.  I didn't like the complexities of the 2/3 split.  I worked on some of our
infrastructural tooling at work, but it was written in Python 2, and I wasn't
particularly interested in learning older technology.  If I was going to learn
Python, I wanted to learn Python 3, so I bided my time.  By 2018, however, the
Python 3 switch was [really gaining
steam](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/),
indicating that I could probably go all-in on only learning Python 3, and that
knowledge would be broadly applicable immediately, and definitely more
applicable over time.  Although the switch is still not "complete" at the
moment, (the latest version of MacOS still ships with Python 2 by default), the
tide has certainly turned, and [Python 2 will not be maintained past
2020](https://www.python.org/dev/peps/pep-0373/).  It seems credible that the
switch will soon be a think of the past for all practical purposes.

Finally, the [PEP process](https://www.python.org/dev/peps/pep-0001/) strikes
me as one of the best processes for improving a language that I've come across.
Its emphasis on scholarship (pointing to, evaluating, and using the best ideas
from similar efforts), and on clearly motivating the new feature, bodes well
for the long-term prospects for the language.  It also indicates to me that I
will be able to stay up-to-date with the latest changes with ease by
following the new PEPs.

Taken together, all these factors led me to conclude that Python was worth a
substantial time investment.  I decided to learn Python deeply, and for it to
become my primary language for most of my programming tasks going forward.

### Actually Learning Python

Learning a new language, while not easy, is a process I'm familiar with.
I have programmed in many languages, including a small amount of Python, in
the past.

However, when I reflected on my programming skills a bit more, even for
languages that I'm very familiar with, I realized I have always muddled
through, learning enough to work reasonably effectively, but falling back to
Stack Overflow and other reference materials when my fully-internalized
knowledge failed me, which was frequently.

This is not to say that I didn't put effort into learning those languages.
When I was learning Ruby ten years ago, I read three books on the language
cover to cover and listened to a [large number of
podcasts](https://devchat.tv/ruby-rogues/) to fill in the gaps.  I felt
accomplished having worked my way through so much material, and that knowledge
certainly aided in my day-to-day programming, however I still found myself
continually fumbling around in the REPL or browsing Stack Overflow.  I had
spent *many hours* reading those books, but their information was frequently
not at-hand when I needed it. ( Subsequently, I've come to understand why, in
part due to wonderful resources like Andy Matuschak's article [Why Books Don't
Work](https://andymatuschak.org/books/) )

This time I was interested in looking for a better approach to learning, in
part for the novelty of simply doing things differently (how can I get excited
about learning my Nth language?), and in part as an experiment; could I do
better?

I had stumbled across [Anki](https://apps.ankiweb.net/) earlier in the year and
then also read [Michael Nielsen's fascinating
article](http://augmentingcognition.com/ltm.html) about how he uses spaced
repetition in his research.  It seemed like an interesting approach to
learning, and it fit the bill of being quite different from my previous
approaches.

I looked to see if there were any Python Anki decks already available, and
there was a [very good deck](https://ankiweb.net/shared/info/51975584).  I
started with that deck.  I quickly realized that although the deck was not a
gentle introduction to programming, and would likely be overwhelming for a
novice.  However, it worked quite well for me, despite little exposition.  I
was picking up the concepts and syntax quickly, and more importantly, I was
easily retaining them because the cards were presented to me over and over as I
learned them.

I was seeing tangible gains and reliably remembering everything, but the
process was not without its problems.  In the first several weeks it felt like
there was a mountain of cards.  Although there are only 211 cards in that deck,
Anki's schedule had me revisit each card multiple times, initially very
frequently.  It felt like that pace continued for a while.  At times I felt
overwhelmed by my queue, and even considered calling the whole thing off more
than once.  But then something surprising happened.  The reviews lessened.  My
queue dwindled.  I...  somehow... was on top of things, and then... very on top
of things.  Suddenly I only had a couple cards to review per day, and it took
less than a minute.  When I reviewed those cards, I knew them *cold*. What
happened?!?

Reliably, my intuition about exponential backoff had failed me, much as any
person's intuition about exponential *anything* fails them.  I hadn't realized
things would become an absolute cakewalk once I passed an important threshold.
I also hadn't realized how abruptly that threshold would arrive.

On Twitter, Andy Matuschak [sums up his similar
findings](https://mobile.twitter.com/andy_matuschak/status/1075487476674834432)
and points to a surprising conclusion:

> This leads to a *very* unintuitive feeling: it's… effectively free to
> memorize as many new cards as I can write? What?
>
> Which in turn means that for me, the real marginal cost is in the moment of
> *writing* a new card.

I found the same thing.  Reviewing the already-prepared cards from that great
deck was now quick and painless, but as soon as the burden of reviewing the
mountain of cards lifted, I wanted more knowledge; much more.  To that end, I
had been creating new cards while reviewing the Python documentation, but
unlike reviewing, which I could do casually on my phone, and which became
exponentially easier over time, creating cards was challenging, time-consuming,
and remained that way.  For that reason, I wasn't creating nearly as many cards
as I could consume.

My inability to create enough cards to learn from effectively led me to look
for a more scalable solution.  That solution ultimately became the [Memorize
Python](https://github.com/gmccreight/Memorize_Python) project.

### The Memorize Python Project

The simplest description of the Memorize Python project is how I would describe
it to someone who wanted to learn Python using it.  The project is a git
repository containing a JSON file that anyone can load into Anki as a deck
using a special plugin in Anki called
[CrowdAnki](https://ankiweb.net/shared/info/1788670778).  Once loaded, the deck
contains questions and answers about Python, and functions like any other Anki
deck would.

So, if the project functions like a deck, why bother with git and CrowdAnki?
Doesn't that just complicate things?  Why not just make a deck?

The key considerations are collaborative authoring, and continual updates.  I
cannot write enough cards to make a compelling resource on my own.  I can seed
the project with hundreds of cards, but with a project as ambitious as memorizing
the whole of Python, it will take many, many more cards than that.  Also, not
all of the cards will be available right at the outset.  People will contribute
cards throughout the life of the project, and users will need to be able to
easily update their decks in Anki (while retaining their current progress).
Git and CrowdAnki address both of those issues directly.  With git we can do
tremendously scalable collaborative authoring, and with CrowdAnki we can keep
our decks up-to-date.

The Memorize Python project uses CrowdAnki in concert with a simple note scheme
that maintains the lineage of the notes' information, and makes collaboration
more straightforward by limiting the amount of redundant information authors
need to supply.  In short, the project aims to make collaborating on a shared
deck of Python cards as straightforward and pain-free as possible.


### Call to Action

So here's the call to action: I'm looking for like-minded people (there is at
least [one person who is thinking along these lines out
there](https://sivers.org/srs)).  Do you want collaborate on creating a
powerful spaced repetition resource that will help anyone who wants to learn
Python at a deep level?  If so, reach out!  Better yet, find a Python resource
(documentation, blog posts, source code) with friendly licensing terms
and create a JSON file with notes about it, and contribute it to the
community... pull requests welcome!

I believe that together we can collectively build a very powerful dataset that
will help us gain a deep and lasting understanding of Python, a language that
is worthy of careful study.  I get excited about how much we will know!  I look
forward to hearing from you.
