## Coding Period 2 Work

### Week-7 Summary

- This week, I mostly focused on adding support for other data sources like pipermail and meetup.
- We discussed the metrics that we can add for _pipermailqm_. [vchrombie/gsoc#11](https://github.com/vchrombie/gsoc/issues/11)
  - number of emails
  - number of replies
  - number of threads
  - number of users
- I worked on these metrics and implemented all of them. :100:
- We also discussed the metrics and implementation possibilities for _meetupqm_. [vchrombie/gsoc#14](https://github.com/vchrombie/gsoc/issues/14)
  - number of RSVPs
  - number of comments
  - number of yes RSVPs
- There is one particular case in the meetup metrics. The number of yes RSVPs is not a _per day_ metric, unlike the other. It would be a _per event_ metric. We decided to use the event date as the required datetime field. :business_suit_levitating:
- There were two pending metrics from the _gitlabqm_ (number of issues/merge requests attended) that we proposed earlier. I completed their implementation this week. [vchrombie/gsoc#8](https://github.com/vchrombie/gsoc/issues/8)
- Now that we will have meetup on the list, we are planning to do a pilot study on all the projects of [GitLab.org](https://gitlab.com/gitlab-org/) in the upcoming week.
- I'll also work on finishing the _meetupqm_ enricher and work on tests for enrichers too in the next week.
