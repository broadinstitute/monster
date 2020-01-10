## Monster DevOps - System Requirements
Many of the requirements placed on Monster's ingest pipelines (either by stakeholders
or by internal operations) fall squarely within the realm of infrastructure management.

## Production isolation
Things break during normal development, and it's valuable to have a "bleeding edge"
deployment up-and-running to flush out problems. This doesn't mean production should
be at risk of breaking every time we merge a pull request.

Similarly, when multiple pipelines are running in a stable production space, we should
be able to release new versions of some of them without disrupting the others.

## Cost management
Monster's stakeholders agree to fund the compute resources used when running ingest
pipelines. To give everyone involved an accurate picture of exactly how much an ingest
project is costing its stakeholder, it's important that we separate the processing
used for each project into separate billing units. In GCP, the only way to do this is
to run each project's compute under a separate Google project.

On the other hand, running an entire copy of our orchestration and monitoring stack in
every Google project would both overcharge our stakeholders and limit our own ability
to monitor system status. We are willing to eat an "operational cost" funded by the Broad
to centralize systems that make our lives easier on Monster.

## System monitoring
Monster is on the hook to ensure that its ingest pipelines continue to run on schedule.
To do this effectively while continuously developing new pipelines, we need to be sure
that we can reuse dashboards and alerts across different projects. If checking system
status requires looking at `N` different outputs, it should be because each of those
outputs delivers a different type of useful information across our projects, not because
we have `N` different projects running identical copies of the same stack.
