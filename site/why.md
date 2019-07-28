# Memorizing Python.  Why?  How?

### Deciding to learn Python

In mid-2018, I decided to learn Python.

At work, our team was replacing our legacy data system, which used Ruby, with
one that used Python, so there was the standard job motivation.  However, my
interest in the language was really piqued after looking into Python more and
noticing its ubiquity, broad library support, and its tragectory and
improvement methodology.

First, I noticed Python's ubiquity.  I saw Python in many places I hadn't
noticed it before, from being the scripting language for cool graphics
applications like [Blender](https://www.blender.org/) and
[Inkscape](https://inkscape.org/develop/extensions/), to being embedded in my
editor, Vim.  I saw it was the most popular language in the world (I had
assumed that was JavaScript).  I realized that with a better understanding of
Python, I could use many tools I already use, or want to use, in more powerful
ways.

I saw that the library support was also surprisingly large.  A large amount of
libraries are already built directly into the standard library.  I realized
that Python would be an excellent tool to reach for when scripting, because I
would be able to pull in many additional libraries very easily.  I came to
understand that Python, despite being so similar, would actually be a
preferable daily driver language to the one I was already using, Ruby, in part
because I was doing more data work, and in part due to its tragectory.

In the past I had shied away from Python because its tragectory felt
unclear to me.  I didn't like the complexities of the 2/3 split.  I worked on
some of our infrastructural tooling at work, but it was written in Python 2,
and I wasn't particularly interested in learning older technology.  If I was
going to learn Python, I wanted to learn Python 3, so I had bided my time.  By
2018, however, the Python 3 switch was [really gaining
steam](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/),
indicating that I could probably go all-in on only learning Python 3, and that
knowledge would be broadly applicable immediately, and definitely more
applicable over time.  Although the switch is still not complete at the moment,
for example the latest version of MacOS still ships with Python 2 by default,
the tide has certainly turned, and [Python 2 will not be maintained past
2020](https://www.python.org/dev/peps/pep-0373/).  So I consider it credible
that the switch will soon be behind us.

Finally, the [PEP process](https://www.python.org/dev/peps/pep-0001/) strikes me
as one of the best processes for improving a language that I've come across, which
bodes well for the long-term prospects for the language.

So, I took stock of the Python ecosystem and concluded that it was worth a real
investment.  I decided to learn Python deeply, and for it to become my primary
language for most of my programming tasks going forward.

### Actually Learning Python

Learning a new language, while not easy, is a process I'm familiar with.
I've have programmed in many languages, including a small amount of Python, in
the past.

However, when I reflected on my skills a bit more, even for languages that I'm
very familiar with, I realized I have always muddled through, learning enough
to work reasonably effectively, but frequently falling back to Stack Overflow
and other reference materials that were close at hand for more uncommon uses.

This is not to say that I didn't put effort into learning those languages.
When I was learning Ruby ten years ago, I read three books on the language
cover to cover and listened to a [large number of
podcasts](https://devchat.tv/ruby-rogues/) to fill in the gaps.  I felt
accomplished having worked my way through so much material, and that knowledge
certainly aided in my day-to-day programming, however I still found myself
continually fumbling around in the REPL or on Stack Overflow.  I had spent
*many hours* reading those books, but their information was frequently not
at-hand when I needed it. ( Subsequently, I've come to understand why, in part
due to wonderful resources like Andy Matuschak's article [Why Books Don't
Work](https://andymatuschak.org/books/) )

This time I was interested in looking for a better approach, in part for the
novelty of it (how can I get excited about learning my Nth language?), and in
part as an experiment; could I do better?

I had stumbled across [Anki](https://apps.ankiweb.net/) earlier in the year and
then also read [Michael Nielsen's fascinating
article](http://augmentingcognition.com/ltm.html) about how he uses spaced
repetition in his research.  It seemed like an interesting approach to
learning that fit the bill of being quite different from my previous approaches.

I decided to see if there were any Python Anki decks already available.  It
turns out, there are, including one [very good
deck](https://ankiweb.net/shared/info/51975584).  I started with that deck.  I
quickly realized that although the deck was not a gentle introduction to
programming, and would likely be overwhelming for a novice, it seemed to
work quite well for me.  I was picking up the concepts and syntax quickly, and
more importantly, I was easily retaining them due to the repetition.

I was seeing tangible gains and reliably remembering everything, however, in
the first several weeks it felt like there was a mountain of cards (there are
211 in that deck).  Anki's schedule had me revisit each card multiple times,
very frequently at first, and the pace continued for a while.  At times I felt
overwhelmed by my queue, and even considered calling the whole thing off more
than once.  But then something surprising happened.  The reviews lessened.  My
queue dwindled.  I...  somehow... was on top of things, and now only had a
couple cards to review per day.  When I reviewed those cards, I knew them
*cold*. What happened?!?

Reliably, my intuition about exponential backoff had failed me, much as any
person's intuition about exponential *anything* fails them.  I hadn't realized
things would become an absolute cakewalk once I passed a threshold.  I also
hadn't realized how abruptly that threshold would arrive.

On Twitter, Andy Matuschak [sums up his similar
findings](https://mobile.twitter.com/andy_matuschak/status/1075487476674834432)
and points to a surprising conclusion:

> This leads to a *very* unintuitive feeling: it's… effectively free to
> memorize as many new cards as I can write? What?
>
> Which in turn means that for me, the real marginal cost is in the moment of
> *writing* a new card.

I found myself facing that same high marginal cost in card creation.  Yes,
reviewing the already-prepared cards from that great deck was now quick and
painless, but as soon as the burden of reviewing the mountain of cards lifted,
I wanted more knowledge; much more.  To that end, I had been creating new cards
while reviewing the Python documentation, but unlike reviewing, which I could
do casually on my phone and became exponentially easier, creating cards was
challenging, time-consuming, and remained equally so over time.  For that
reason, I wasn't creating nearly as many cards as I could consume.

My inability to create enough cards to keep my busy led to look for a scalable
solution.  That solution is the [Memorize
Python](https://github.com/gmccreight/Memorize_Python) project.

### The Memorize Python Project

So here's the call to action: I'm looking for like-minded people (there is at
least [one other one out there](https://sivers.org/srs)) who want to
collaborate on creating a powerful spaced repetition resource that will help
anyone who wants to learn Python at a deep level.

The groundwork has been laid by Anki, and its plugin system that allowed for
fantastic plugin for collaborative deck authoring:
[CrowdAnki](https://ankiweb.net/shared/info/1788670778).

The Memorize Python project uses CrowdAnki in concert with a simple note scheme
that maintains the lineage of the notes' information, and makes collaboration
straightforward by limiting the amount of redundant information authors need to
supply.  In short, the project aims to make collaborating on a shared deck of
Python cards as straightforward and pain-free as possible.

I believe we can collectively build a very powerful artifact that will help us
gain a deep and lasting understanding of Python, a language that I have
determined is worthy of such effort.
