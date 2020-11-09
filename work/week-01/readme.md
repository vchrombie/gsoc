## Coding Period 1 Work

### semana uno

- I decided to start working on the QM enrichers and I took gitlab as the first option because I was familiar with it. 
[vchrombie/gsoc#6](https://github.com/vchrombie/gsoc/issues/6).
- The main step of building an enricher is to get a minimal idea :thought_balloon: of the data format of the enriched item. I checked the existing index format which I used during the [microtask-9](https://github.com/vchrombie/chaoss-microtasks/tree/master/microtask-9). I was able to figure out a decent format of the index which can be consumed by Prosoul. Ideally, the enricher should perform queries to get the data for every day.

For example: If we want to measure the number of issues opened, the enriched data should be a document per day giving the value of the number of issues opened that day. (something like)
  ```
  {
    "Date" : "20181229",
    "numberOfIssuesOpened" : 8
  },
  {
    "Date" : "20181230",
    "numberOfIssuesOpened" : 5
  },
  ```
I need to change the format a bit (as we don't need a few items :no_good_man:). [vchrombie/gsoc#7](https://github.com/vchrombie/gsoc/issues/7)
- I was contemplating about the metrics that can be extracted from the gitlab data. Valerio suggested a few metrics.
    - number of issues per day
    - number of comments per day
    - number of merges per day
- I was thinking over it and felt we can divide these metrics into some more detail. :thinking:
    - number of issues per day
        - number of issued opened per day
        - number of issues closed per day
        - number of issues attended per day
    
I got this idea from this quality model, [developer_model.json](https://github.com/Bitergia/prosoul/blob/master/django-prosoul/prosoul/data/developer_model.json). 
We need to dig more into these metrics and find all that metrics which we can extract from the gitlab data (versions, labels, milestones). I will check the existing qms for more inspiration. [vchrombie/gsoc#8](https://github.com/vchrombie/gsoc/issues/8)
- Other than planned in the timeline, I also worked on the _gitlabcomments_ enricher ([chaoss/grimoirelab-elk#881](https://github.com/chaoss/grimoirelab-elk/pull/881)) 
and achieved a considerable target :metal:. I completed working on the enricher and Valerio pointed out some mistakes which I corrected and got the enricher working. 
We discussed the faulty reaction mapping and fixed its logic with sensible mapping right now. The enricher and configurations are completed, schema and tests are pending. [vchrombie/gsoc#4](https://github.com/vchrombie/gsoc/issues/4)
