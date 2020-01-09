# Monster DevOps - Motivation
Monster controls its own DevOps code and processes. There are upsides and downsides to this.

On the bad side, it:
* Generates more dev work
* Increases the "surface area" of tech that Monster engineers must be familar with.

On the other hand, it:
* Allows us to quickly adjust our deployments to meet the requirements of new projects
* Reduces the chances of us being blocked on a dependency from DSP DevOps
* Enables us to experiment with spinning infrastructure up/down as part of batch workflows
* Forces us to understand and build expertise across our full stack

We believe the benefits outweigh the costs.

## The role of DSP DevOps
Though we own our DevOps code and processes, the DSP DevOps team still plays an important
role in our team. They provide guidance when exploring new technologies, and sanity-check
our attempts at making things work. Significant changes to Monster infrastructure should
be discussed / reviewed by at least one DevOps engineer.
