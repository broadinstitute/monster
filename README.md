# The Monster Team
[![Monster Slack](https://img.shields.io/badge/Slack%20Channel-%23monster-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CCAU5L6LV/)
[![Monster CI Slack](https://img.shields.io/badge/Slack%20Channel-%23monster--ci-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CFXEDUUP5/)

New to the team? [Start here](./getting-started/README.md).

## People

| Name | Role | GitHub |
| --- | --- | --- |
| Ben Carlin | Software Engineer | @benjamincarlin |
| Dan Moran | Tech Lead | @danxmoran |
| Emily Munro-Ludders | Scrum Master | @emunrolu |
| Jeff Korte | Product Owner | @JeffKorte |
| Kathy Reinold | Data Modeler | @kreinold |
| Raaid Arshad | Software Engineer | @raaidbroad |

## GitHub Teams
* [DSP Monsters](https://github.com/orgs/broadinstitute/teams/dsp-monsters) - Team for repositories under the `broadinstitute` org
* [Emerald Writers](https://github.com/orgs/DataBiosphere/teams/broademeraldwrite) - Team for repositories under the `DataBiosphere` org

## Projects

### Data Modeling
Linked Data definitions for the DSP Core Data Model, with:
* Extensions for unmodeled datasets
* Corresponding schema definitions for the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo)

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1n8TP4Q_4n2pCysjQz2Hkn2kpHGEILLCj)
* [Confluence - DSP Core Data Model](https://broadinstitute.atlassian.net/wiki/spaces/DSPCDM/overview)
* [Confluence - FAIR Community of Practice](https://broadinstitute.atlassian.net/wiki/spaces/FairCoP/overview)

#### GitHub repos
* [DSP Data Models](https://github.com/broadinstitute/dsp-data-models) - Data Model definitions with corresponding schemas
* [OLS Docker](https://github.com/broadinstitute/ols-docker) - Dockerization of EBI's Ontology Lookup Service, configured to use ontologies we care about

### Data Ingest
Services for moving data into the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo), including:
* Bulk file transfer
* ETL workflows for tabular data
* Bulk ingest orchestration

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LjtBbMZs5-FqTGcRjw80ZBlHhfd_LT2z)

#### GitHub repos
* [Transporter](https://github.com/databiosphere/transporter) - Bulk file-transfer system
* [Monster ETL](https://github.com/broadinstitute/monster-etl) - Apache Beam workflows for ingest
* [Extractors](https://github.com/broadinstitute/monster-extractors) - Tools / services for mechanically transforming external metadata into Beam-friendly JSON
* [Ingester](https://github.com/broadinstitute/monster-ingester) - Service for orchestrating batch ingests into the Jade repo

### Operations (dev and prod)
Infrastructure, configuration, and shared code used to manage developing and deploying our services.

### GitHub repos
* [Ingest Deploy](https://github.com/broadinstitute/dsp-ingest-deploy) - Terraform and Kubernetes configuration for deploying ingest components into GCP
* [Storage Libs](https://github.com/broadinstitute/monster-storage-libs) - Utility libraries for I/O against external storage systems
* [sbt plugins](https://github.com/broadinstitute/monster-sbt-plugins) - Common build plugins used across Monster projects
