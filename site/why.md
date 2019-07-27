# Memorizing a Programming Language.  Why?  How?

In 2018, I decided to really learn Python.  I had moved into a more
data-centric role, and our team was starting to use more Python.  Additionally, Python 3 switch was [really gaining steam](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/).
Basically, it seemed like a no-brainer.

Learning another language, while not easy, is a well-trod path for me.  I've
been around the block, and have programmed in many languages, including Python,
in the past.

However, when I reflected on my skills a bit more, I realized I have always
muddled through, learning enough to get the job done, but frequently falling
back to Stack Overflow and other reference materials that were close at hand.

Don't get the wrong impression, I studied!  When I was learning Ruby ten years
ago, I read three books on the language cover to cover and listened to a [large
number of podcasts](https://devchat.tv/ruby-rogues/) to fill in the gaps.  I
felt accomplished having worked my way through so much material, and
that knowledge certainly aided in my day-to-day programming, however I still
found myself continually fumbling around in the REPL or on Stack Overflow.  I
had spent *hours* reading those books, but their information was just not
at-hand when I needed it. ( Subsequently, I've come to understand why, in part
due to wonderful resources like Andy Matuschak's article [Why Books Don't
Work](https://andymatuschak.org/books/) )

This time I was interested in taking a different approch, in part for the
novelty of it (how can I get excited about learning my Nth language), and in
part as an experiment; could I do better?

I had stumbled across [Anki](https://apps.ankiweb.net/) earlier in the year and
then also read [Michael Nielsen's fascinating
article](http://augmentingcognition.com/ltm.html) about how he uses spaced
repetition in his research.  It sure seemed like an interesting approach to
learning.

I decided to see if there were any Python decks.  It turns out, there are,
including one [very good deck](https://ankiweb.net/shared/info/51975584).  I
started with that deck.  I quickly realized that although the deck
would be overwhelming for a novice (within the first handfull of cards, many
are related to various complicated scoping examples with minimal context),
it seemed to be working very well for me.  I was picking up the concepts
quickly, and more importantly, I was readily retaining them due to the
repetition.

However, in the early days, it felt like there was a mountain of cards (there
are 211 in that deck).  Anki's schedule forced me to revisit them relentlessly.
At times I felt overwhelmed by my queue, and even considered calling it a
failed experiment more than once.  But then something surprising happened.  The
reviews lessened.  My queue dwindled.  I... somehow... only had a couple cards
to review per day, and when I reviewed them I knew them *cold*.  What
happened?!?  My intuition about exponential backoff had completely failed me.
I hadn't realized it would become an absolute cakewalk to keep all these Python
facts in my head, and I hadn't realized how abruptly that switch would arrive.

[This tweet from Andy
Matuschak](https://mobile.twitter.com/andy_matuschak/status/1075487476674834432)
sums it up his similar findings, and points to a surprising conclusion:

> This leads to a *very* unintuitive feeling: it's… effectively free to
> memorize as many new cards as I can write? What?
>
> Which in turn means that for me, the real marginal cost is in the moment of
> *writing* a new card.

I found myself facing that same high marginal cost.  Yes, reviewing the
already-prepared cards was now quick and painless, but I wanted more knowledge;
much more.  To that end, I had been creating new cards while reviewing the
Python documentation, but unlike reviewing, which can be done casually on your
phone, creating cards is a challenging and time-consuming process, so I wasn't
creating nearly as many as I could consume.  Additionally, for the first few
months I was creating sub-par cards.  I could tell because one of them would
come up for review and the question would be slightly ambigous, robbing me of
the satisfaction of nailing the answer, and decreasing my motivation.

I ultimately learned how to write satisfying cards, but I have not been able to
write the volume of cards that I wish I could... which leads to this project.

### This project

My inability to write as many cards as I would like has led me to create this
project.  I'm looking for like-minded people (there is at least [one other one
out there](https://sivers.org/srs)) who want to collaborate on creating a
resource we can all benefit from.

The groundwork has been laid by Anki, and its plugin system that
allowed for fantastic plugin geared specifically towards authoring decks collaboratively:
[CrowdAnki](https://ankiweb.net/shared/info/1788670778).

Additionally, I think we can arrive at a simple note taking scheme that
maintains the lineage of the information, and makes collaboration
straightforward.  The [Memorize Python](https://github.com/gmccreight/Memorize_Python)
project aims to make collaborating on a shared deck as pain-free as possible.

I believe we can collectively build a very powerful artifact that will help us
gain a deep and lasting understanding of Python.
