# Memorizing a Programming Language.  Why?  How?

In 2018, I decided to really learn Python.  I had moved into a more
data-centric role, and our team was starting to use more Python.  Additionally,
Python 3 switch was [really gaining
steam](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/).
Also, Python is used for scripting some very interesting apps, like
[blender](https://www.blender.org/),
[inkscape](https://inkscape.org/develop/extensions/), and my editor, vim, even
comes with a python module embedded in it.  Basically, it seemed like a
no-brainer that I should finally learn it.

Learning another language, while not easy, is a process I'm familiar with.
I've have programmed in many languages, including a small amount of Python, in
the past.

However, when I reflected on my skills a bit more, even for languages that I'm
very familiar with, I realized I have always muddled through, learning enough
to work effectively, but frequently falling back to Stack Overflow and other
reference materials that were close at hand for more uncommon uses.

This is not to say that I didn't practice those languages.  When I was learning
Ruby ten years ago, I read three books on the language cover to cover and
listened to a [large number of podcasts](https://devchat.tv/ruby-rogues/) to
fill in the gaps.  I felt accomplished having worked my way through so much
material, and that knowledge certainly aided in my day-to-day programming,
however I still found myself continually fumbling around in the REPL or on
Stack Overflow.  I had spent *hours* reading those books, but their information
was frequently not at-hand when I needed it. ( Subsequently, I've come to understand
why, in part due to wonderful resources like Andy Matuschak's article [Why
Books Don't Work](https://andymatuschak.org/books/) )

This time I was interested in looking for a better approach, in part for the
novelty of it (how can I get excited about learning my Nth language?), and in
part as an experiment; could I do better?

I had stumbled across [Anki](https://apps.ankiweb.net/) earlier in the year and
then also read [Michael Nielsen's fascinating
article](http://augmentingcognition.com/ltm.html) about how he uses spaced
repetition in his research.  It seemed like an interesting learning approach to
learning that fit the bill of being quite different from my previous approaches.

I decided to see if there were any Python Anki decks already available.  It
turns out, there are, including one [very good
deck](https://ankiweb.net/shared/info/51975584).  I started with that deck.  I
quickly realized that although the deck was not a gentle introduction to
programming, and would likely be overwhelming for a novice, it seemed to be
work quite well for me.  I was picking up the concepts and syntax quickly, and
more importantly, I was easily retaining them due to the repetition.

However, in the early days, it felt like there was a mountain of cards (there
are 211 in that deck).  Anki's schedule had me revisit them multiple times
each, very frequently at first, and the pace continued for a while.  At times I
felt overwhelmed by my queue, and even considered calling it a failed
experiment more than once.  But then something surprising happened.  The
reviews lessened.  My queue dwindled.  I... somehow... only had a couple cards
to review per day, and when I reviewed them I knew them *cold*.  What
happened?!?  My intuition about exponential backoff had, reliably, failed me.
I hadn't realized things would become an absolute cakewalk once I passed a
threshold.  I also hadn't realized how abruptly that threshold would arrive.

[This tweet from Andy
Matuschak](https://mobile.twitter.com/andy_matuschak/status/1075487476674834432)
sums up his similar findings, and points to a surprising conclusion:

> This leads to a *very* unintuitive feeling: it's… effectively free to
> memorize as many new cards as I can write? What?
>
> Which in turn means that for me, the real marginal cost is in the moment of
> *writing* a new card.

I found myself facing that same high marginal cost.  Yes, reviewing the
already-prepared cards was now quick and painless, but I wanted more knowledge;
much more.  To that end, I had been creating new cards while reviewing the
Python documentation, but unlike reviewing, which I could do casually on my
phone, creating cards was challenging and time-consuming.  I wasn't
creating nearly as many cards as I could consume.

My inability to create enough cards to keep my busy led to the [Memorize
Python](https://github.com/gmccreight/Memorize_Python) project.

### Memorize Python

My inability to write as many cards as I would like has led me to create this
project.  I'm looking for like-minded people (there is at least [one other one
out there](https://sivers.org/srs)) who want to collaborate on creating a
powerful resource that we can all benefit from.

The groundwork has been laid by Anki, and its plugin system that allowed for
fantastic plugin geared specifically towards authoring decks collaboratively to
be developed: [CrowdAnki](https://ankiweb.net/shared/info/1788670778).

Memorize Python uses CrowdAnki in concert with a simple note scheme that
maintains the lineage of the note information, and makes collaboration
straightforward by limiting the amount of redundant information authors need to
supply.  In short, the project aims to make collaborating on a shared deck of
Python cards as straightforward and pain-free as possible.

I believe we can collectively build a very powerful artifact that will help us
gain a deep and lasting understanding of Python, a language that is exceedingly
popular, capable, and likely to stand the test of time.
