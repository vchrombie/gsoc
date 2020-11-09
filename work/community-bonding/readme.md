## Community Bonding Period Work

### unión comunitaria 1

> I was supposed to setup the project-tracker, fix a schedule for blogging & writing reports and setup the communication 
medium with the community and mentors.

- We will be discussing about the progress of this project every week at the `#grimoirelab` channel on freenode IRC 
(scheduled for every Thursday 17h to 18h (CEST) or 20h30 to 21h30 (IST)). The transcripts of the meetings (chats) will be 
uploaded to the project-tracker.
- I decided to write a work report and a blog post every week (mostly on Monday) explaning the work I did over the week. The 
blog posts will be on my [blog](https://vchrombie.github.io/blog).
- I created a project tracker, [vchrombie/gsoc](https://github.com/vchrombie/gsoc), where I will be storing the work reports, 
meeting logs, blog posts and almost everything related to the GSoC project. :tada:
  - You can find the meeting logs in the [meetings](https://github.com/vchrombie/gsoc/blob/master/meetings) directory.
  - You can find the work reports in the [work](https://github.com/vchrombie/gsoc/blob/master/work) directory.
  - You can find the blog posts on the README.md, [weekly updates](https://github.com/vchrombie/gsoc#weekly-updates).
- I created an issue in the governance repository to keep the community updated with my work, 
[chaoss/governance#205](https://github.com/chaoss/governance/issues/205). I will be posting the blog posts, meeting logs and 
work reports over there. :rocket:
- I will be sending the work summary with the blog links the CHAOSS and GrimoireLab mailing list.

### unión comunitaria 2

> I was supposed to learn how enrichers work and create a PR adding or improving any enricher.

- I started looking into enrichers in grimoirelab-elk, one of the main components of GrimoireLab. It offers a convenient way to store perceval raw data :outbox_tray: and processes & enriches the data :card_index_dividers: which can be consumed by Kibiter. :bar_chart:
  -  ELK stores the Perceval data in ES indexes as raw documents (raw data), [grimoire_elk/raw](https://github.com/chaoss/grimoirelab-elk/tree/master/grimoire_elk/raw).
  -  The enrichers of ELK enriches the raw data, removes the unnecessary data and adds some other information like identities & organization (from SortingHat) and stores them as JSON documents, [grimoire_elk/enriched](https://github.com/chaoss/grimoirelab-elk/tree/master/grimoire_elk/enriched).
- I went through a few examples of simple enrichers like [slack.py](https://github.com/chaoss/grimoirelab-elk/blob/master/grimoire_elk/enriched/slack.py), [gitlab.py](https://github.com/chaoss/grimoirelab-elk/blob/master/grimoire_elk/enriched/gitlab.py), shared by Valerio. I thought of working on adding elk support for rocket chat but Animesh already started working on it, [chaoss/grimoirelab-elk#876](https://github.com/chaoss/grimoirelab-elk/issues/876). I will probably work on some other enricher.
- Apart from that, I opened a PR for adding perceval support to Zulip chat, [chaoss/grimoirelab-perceval#667](https://github.com/chaoss/grimoirelab-perceval/pull/667). It needs some iterations to be in good shape. I will work on this enricher once the PR is in good shape.
- Also, I have opened a couple of issues in perceval repository.
  - Found that googlehits backend was not working since the id used to parse the data is changed. Following up on the discussion and looking forward to fixing it, [chaoss/grimoirelab-perceval#668](https://github.com/chaoss/grimoirelab-perceval/issues/668).
  - I proposed a new feature for adding perceval support to Trello. We need to discuss the feasibility of storing all the backends in the same repository or different repositories. So, this feature [chaoss/grimoirelab-perceval#664](https://github.com/chaoss/grimoirelab-perceval/issues/664) might need to wait.
  - I proposed having an issue template, but it was already suggested and we need to discuss it, [chaoss/grimoirelab-perceval#665](https://github.com/chaoss/grimoirelab-perceval/issues/665).

### unión comunitaria 3

> I planned to work on adding perceval support for zulip chat and start working on a new enricher.

- I started working on adding zulip backend for perceval last week. Valerio reviewed the PR and suggested a lot of changes. With his help, I was able to extract a few data items. Later, I implemented the logic for incremental fetching and got it working, [chaoss/grimoirelab-perceval#667](https://github.com/chaoss/grimoirelab-perceval/pull/667). :running_man: 
- You can retrieve the messages sent to any particular stream of a zulip chat by
  ```
  perceval zulip 'https://example.zulipchat.com/' 'stream_name' -e 'BOT_EMAIL_ADDRESS' -t 'BOT_API_KEY'
  ```
- I tested it across a few streams and reported the results, [chaoss/grimoirelab-perceval#667-comment](https://github.com/chaoss/grimoirelab-perceval/pull/667#issuecomment-633218035). I started working on the unit tests, planning to finish this by this week. :flying_saucer:
- Apart from this, Valerio suggested working on the *gitlabcomments* enricher. The initial discussion about this feature happened here, [chaoss/grimoirelab#208](https://github.com/chaoss/grimoirelab/issues/208). The proposal was to create a new enricher, similar to *github2*, which would focus on enriching the gitlab comments data.
- Also, I went through the Prosoul codebase to have some idea about the data format which can be easily consumable by prosoul. Hoping to get this done soon, preferably before the coding period. :cold_face:

### unión comunitaria 4

> I planned to work on the gitlabcomments enricher and complete the pending tasks for the coding period.

- In continuation of the previous week, I started working on the *gitlabcomments* enricher. As this is most similar to the *github2* enricher, I tested it across a few repositories and analyzed the enriched items and the dashboards. :chart_with_downwards_trend:
- I did a comparison of the github and gitlab perceval output to know more about the two APIs like similar items, different items, items that vary according to the features of the software which are fetched in each of the backends.
- I started implementing the functions for enriching the issue items and opened a draft PR too, [chaoss/grimoirelab-elk#881](https://github.com/chaoss/grimoirelab-elk/pull/881). I will work on completing this, in the coming weeks.
- I had the task of creating a UML diagram for the existing implementation of Prosoul. I have a decent understanding of the codebase. So, I went ahead and created one. :point_down:

![uml-prosoul](prosoul-uml.png)
- I still have to make a few activity diagrams for simple workflows of Prosoul like creating a quality model, making an assessment. I have it on my check-list. :ballot_box_with_check:
- I have explored how to create an study index. I also made a few plans for the first coding period. :ok_man:
