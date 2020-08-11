## Coding Period 3 Work

### Week-10 Summary

- I was focusing on writing down :memo: results obtained from the gitlab pilot study :helicopter: performed last week. [vchrombie/gsoc#13 (comment)](https://github.com/vchrombie/gsoc/issues/13#issuecomment-669236168)
- Apart from that, I also worked on implementing _githubqm_ enricher. All the enrichers, planned so far, are implemented. :100:
- The metrics would be almost the same ones for the _gitlabqm_ enricher. There is one minor change in the Pull Requests Comments. The comments data can be obtained as review comments in github raw data (this comes from the API). The PR comments and review comments are different. I followed this, keeping _github2_ (github comments) enricher of GrimoireLab-ELK in mind. [vchrombie/gsoc#19](https://github.com/vchrombie/gsoc/issues/19)
- The implemented metrics are 
  - number of issues created
  - number of issues closed
  - number of pull requests created
  - number of pull requests closed
  - number of pull requests merged
  - number of issue comments
  - number of review comments
  - number of issues attended
  - number of pull requests reviewed
- For the next week, I'm planning to start with the documentation work of the project. As we now have the _githubqm_ enricher, I'm planning to perform a pilot study on CHAOSS projects.
