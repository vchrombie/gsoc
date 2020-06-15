## Coding Period 1 Work

### Week-2 Summary

- Got a basic idea :bulb: of how the format of enriched items should look like. 

(taking _gitlab_ enricher as example) [vchrombie/gsoc#7](https://github.com/vchrombie/gsoc/issues/7)
```
{
  "project": "cms" ,    <---
  "metric_class": "issues" ,    <---
  "metric_type": "LineChart" ,    <---
  "metric_id": "issues.numberOpenIssues" ,    <---
  "metric_desc": "The number of issues opened on a current date.",    <---
  "metric_name": "Number of Open Issues" ,    <---
  "metric_es_value": 8 ,    <---
  "metric_es_compute": "sample" ,
  "datetime": "2020-01-01T00:00:00+00:00" ,    <---
  "uuid": "2fb8da7299fa849c8cda9dc5f9c571493fa67234" ,    <---
  "metric_es_value_weighted": 8 ,    <---
  "meta": {
    "top_projects": [
      "main"
    ]
  }
}
```

The `project` can be derived using the search_fields in the perceval item. The `metric_es_value` (or `metric_es_value_weighted`) is the actual required value which is equal to the number of the metric data items (here in _gitlabqm_, it can be the number of issues/comment/merge requests) on a particular date represented by `datetime`.

The fields like `metric_class`, `metric_type`, `metric_id`, `metric_desc`, `metric_name` are self-explanatory, which are dependent on the type of metric we are defining and the data source.
- I started working on implementing the enricher, basically extracting the required fields from the raw (perceval) data. Working branch :point_right: https://github.com/vchrombie/grimoirelab-elk/tree/gitlabqm.
- Approach for the _gitlabqm_ enricher:
  1. Filter all the issues items and build a dictionary with dates and keys and the number of issues (metric data items) as values.
  2. Add the items to make the dictionary enricher item and upload it to es.
- I plan to finish this basic enricher ASAP :monorail: and get a review on the implementation (within this week) and decide to work on improving the implementation or move on to the next data source (git, pipermail, github2). [vchrombie/gsoc#6](https://github.com/vchrombie/gsoc/issues/6)
- Apart from this, I worked on the _gitlabcomments_ enricher. Valerio reviewed and suggested some more improvements to the PR. The enricher looks perfectly fine now. [vchrombie/gsoc#4](https://github.com/vchrombie/gsoc/issues/4)
- Made a small script that generates a schema file, given the index name as an argument, [generate-es-index-schema](https://gist.github.com/vchrombie/bf6a682edcf47624126317897e58679c).
- Learned how to add tests in elk and added the tests for _gitlabcomments_ enricher. There are a few improvements in the tests to increase the coverage of the enricher. I plan to work on it and complete the enricher work this week. :cartwheeling:
- We also discussed about about the [Getting-Started](https://github.com/chaoss/grimoirelab-sirmordred/blob/master/Getting-Started.md) section of sirmordred repo as GrimoireLab got updated (ES/Kibiter 6.8.6).
