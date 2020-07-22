<div align="center">
    <a href="https://summerofcode.withgoogle.com/projects/#5489558193438720"><img src="notes/gsoc-chaoss-banner.png" width="720" alt="google-summer-of-code"></a>
    <h2>
    Creating Quality models using GrimoireLab and <a href="https://github.com/chaoss">CHAOSS</a> metrics
    </h2>
</div>

<p align="center">
	<a href="#project-abstract">Project Abstract</a> | 
	<a href="#pull-requests--issues">Pull Requests & Issues</a> | 
	<a href="#weekly-updates">Weekly Updates</a> | 
	<a href="#links">Links</a>
</p>

<p align="center">
	Check out my <a href="https://vchrombie.github.io/blog">blog</a> or follow me on <a href="https://twitter.com/vchrombie">Twitter</a> for more updates.
</p>
<br>

## Project Abstract

GrimoireLab is a powerful open-source platform that provides support for monitoring and in-depth analysis of software projects. It produces a rich set of dashboards, which can be easily inspected by decision-makers to help them understand the evolution and health of their projects. Despite the large set of dashboards available in GrimoireLab, comparing projects between each other is not straightforward since it requires navigating and drilling down the data in different dashboards.

Prosoul is a web application that empowers decision-makers with the means to create and manage their own quality models, which are useful means to evaluate and compare software projects. This project idea is about supporting the definition of Quality Models using GrimoireLab data and Prosoul.

The main aim of the project is to design an approach to shape the GrimoireLab data in a format that can easily be consumed by Prosoul and implement it on the data obtained from a few data sources like git, github and mailing list repositories to obtain simple quality models.

**Mentors**: [@Polaris000](https://github.com/Polaris000), [@inishchith](https://github.com/inishchith), [@dlumbrer](https://github.com/dlumbrer) and [@valeriocos](https://github.com/valeriocos).

## Working Branches

- _gitlabqm_ enricher :fast_forward: https://github.com/vchrombie/grimoirelab-elk/tree/gitlabqm
- _gitlabqm_+_gitqm_ enricher :fast_forward: https://github.com/vchrombie/grimoirelab-elk/tree/gitlabqm+gitqm

## Pull Requests & Issues

#### [Bitergia/prosoul](https://github.com/Bitergia/prosoul)

Pull Requests

- [#207](https://github.com/Bitergia/prosoul/pull/207): [panels] update attribute-template.json **`/ap`**
- [#206](https://github.com/Bitergia/prosoul/pull/206): [views] update the viz result kibana_url **`/ap`**
- [#203](https://github.com/Bitergia/prosoul/pull/203): [assessment] Fix the TemplateSyntaxError **`/ap`**
- [#201](https://github.com/Bitergia/prosoul/pull/201): [UI] Improve the Login UI **`/ap`**
- [#200](https://github.com/Bitergia/prosoul/pull/200): [docs] Update README.md with installation video **`/ap`**
- [#199](https://github.com/Bitergia/prosoul/pull/199): add license headers and copyright information **`/ap`**
- [#196](https://github.com/Bitergia/prosoul/pull/196): [docs] fixed minor typos in README.md **`/ap`**

Issues

- [#205](https://github.com/Bitergia/prosoul/issues/205): Kibana dashboard URL doesn't have the port number **`/ap`**
- [#204](https://github.com/Bitergia/prosoul/issues/204): index_pattern is not up to date in the templates **`/ap`**

#### [chaoss/grimoirelab-elk](https://github.com/chaoss/grimoirelab-elk)

Pull Requests

- [#902](https://github.com/chaoss/grimoirelab-elk/pull/902): [qm-elk] Add support for QM data enrichment **`/cp1`**
- [#892](https://github.com/chaoss/grimoirelab-elk/pull/892): [enriched-gitlabqm] New enricher for QM GitLab data **`/cp1`**
- [#881](https://github.com/chaoss/grimoirelab-elk/pull/881): [enriched-gitlabcomments] New enricher to handle gitlab comments  **`/cb`**
- [#815](https://github.com/chaoss/grimoirelab-elk/pull/815): [schema] Update mattermost.csv **`/ap`**
- [#814](https://github.com/chaoss/grimoirelab-elk/pull/814): [schema] Update dockerhub.csv **`/ap`**
- [#812](https://github.com/chaoss/grimoirelab-elk/pull/812): [schema] Update askbot.csv **`/ap`**
- [#788](https://github.com/chaoss/grimoirelab-elk/pull/788): Update README.md **`/ap`**
- [#787](https://github.com/chaoss/grimoirelab-elk/pull/787): [doc] fix mistake in README.md **`/ap`**

Issues

- [#876](https://github.com/chaoss/grimoirelab-elk/issues/876): [Rocket.Chat] Add rocketchat backend support to ELK **`/cb`**

#### [chaoss/grimoirelab-perceval](https://github.com/chaoss/grimoirelab-perceval)

Pull Requests

- [#667](https://github.com/chaoss/grimoirelab-perceval/pull/667): [backend] Add Zulip Backend **`/cb`**
- [#624](https://github.com/chaoss/grimoirelab-perceval/pull/624), [#623](https://github.com/chaoss/grimoirelab-perceval/pull/623): [perceval] Update license and copyright information **`/ap`**
- [#615](https://github.com/chaoss/grimoirelab-perceval/pull/615): [github] Update the docstrings **`/ap`**

Issues

- [#668](https://github.com/chaoss/grimoirelab-perceval/issues/668): [googlehits] Returns None object **`/cb`**
- [#665](https://github.com/chaoss/grimoirelab-perceval/issues/665): Issue template **`/cb`**
- [#664](https://github.com/chaoss/grimoirelab-perceval/issues/664): [Feature Request] Add support for Trello **`/cb`**
- [#630](https://github.com/chaoss/grimoirelab-perceval/issues/630): [Feature Request] Add support for Zulip **`/ap`**

#### [chaoss/grimoirelab-sirmordred](https://github.com/chaoss/grimoirelab-sirmordred)

Pull Requests

- [#476](https://github.com/chaoss/grimoirelab-sirmordred/pull/476): [docs] Update Getting-Started.md result image **`/cp1`**
- [#450](https://github.com/chaoss/grimoirelab-sirmordred/pull/450): [docs] revamp of getting-started.md **`/ap`**
- [#431](https://github.com/chaoss/grimoirelab-sirmordred/pull/431): Fix askbot configuration typos **`/ap`**

Issues

- [#433](https://github.com/chaoss/grimoirelab-sirmordred/issues/433):  Issue regarding the back-links #433 **`/ap`**

> **Tags**:
> - **a**pplication **p**eriod : **`/ap`**
> - **c**ommunity **b**onding period : **`/cb`** 
> - **c**oding **p**eriod **x** - **`/cpx`** <br>

## Weekly Updates

### Community Bonding (May 4, 2020 - June 1, 2020)

- GSoC Acceptance, [aceptación gsoc](https://vchrombie.github.io/blog/gsoc-acceptance).
- Week 1: [Report](work/community-bonding#week-1-summary) | Blog Post :point_right: [unión comunitaria 1](https://vchrombie.github.io/blog/community-bonding-1).
- Week 2: [Report](work/community-bonding#week-2-summary) | Blog Post :point_right: [unión comunitaria 2](https://vchrombie.github.io/blog/community-bonding-2).
- Week 3: [Report](work/community-bonding#week-3-summary) | Blog Post :point_right: [unión comunitaria 3](https://vchrombie.github.io/blog/community-bonding-3).
- Week 4: [Report](work/community-bonding#week-4-summary) | Blog Post :point_right: [unión comunitaria 4](https://vchrombie.github.io/blog/community-bonding-4).
- Community Bonding Period, [período de vinculación comunitaria](https://vchrombie.github.io/blog/community-bonding-period).

### Coding Period 1 (June 1, 2020 - June 29, 2020)

- Week 1: [Report](work/week-1/#week-1-summary) | Blog Post :point_right: [semana uno](https://vchrombie.github.io/blog/coding-period-1-week-1).
- Week 2: [Report](work/week-2/#week-2-summary) | Blog Post :point_right: [semana dos](https://vchrombie.github.io/blog/coding-period-1-week-2).
- Week 3: [Report](work/week-3/#week-3-summary) | Blog Post :point_right: [semana tres](https://vchrombie.github.io/blog/coding-period-1-week-3).
- Week 4: [Report](work/week-4/#week-4-summary) | Blog Post :point_right: [semana cuatro](https://vchrombie.github.io/blog/coding-period-1-week-4).
- Coding Period 1, [período de codificación uno](https://vchrombie.github.io/blog/coding-period-1).
- :bicyclist: First Evaluation Period (June 29 - July 3): PASSED :ballot_box_with_check:.
- Week 5: [Report](work/week-5/#week-5-summary) | Blog Post :point_right: [semana cinco](https://vchrombie.github.io/blog/coding-period-1-week-5).

### Coding Period 2 (July 4, 2020 - July 24, 2020)
- Week 6: [Report](work/week-6/#week-6-summary) | Blog Post :point_right: [semana seis](https://vchrombie.github.io/blog/coding-period-2-week-6).
- Week 7: [Report](work/week-7/#week-7-summary) | Blog Post :point_right: [semana siete](https://vchrombie.github.io/blog/coding-period-2-week-7).

## Links

- [GSoC 2020 Proposal CHAOSS - Venu](notes/gsoc-proposal-venu.pdf)
- [Project Link](https://summerofcode.withgoogle.com/projects/#5489558193438720) on GSoC Website.
- [Microtasks](https://github.com/vchrombie/chaoss-microtasks) repository.
- [Contributions](notes/application-period-contributions.md) during application period.

## Footnotes

- We will be discussing about the progress of this project every week at the `#grimoirelab` channel on freenode IRC (scheduled for every Thursday 17h to 18h (CEST) or 20h30 to 21h30 (IST)). The transcripts of the meetings (chats) are available in [meetings](meetings/) directory.
- I will be writing a blog post every week (mostly on Monday) explaning the work I did over the week. You can find the links to the work summary and blog posts in the [work](work/) directory.
