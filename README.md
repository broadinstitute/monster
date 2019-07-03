# The Monster Team
[![Monster Slack](https://img.shields.io/badge/Slack%20Channel-%23monster-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CCAU5L6LV/)
[![Monster CI Slack](https://img.shields.io/badge/Slack%20Channel-%23monster--ci-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CFXEDUUP5/)

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
* [Broad Pipeline Developers](https://github.com/orgs/BICCN/teams/broad-pipeline-developers) - Team for repositories under the `BICCN` org

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
Infrastructure for moving data into the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo), including:
* Bulk file transfer
* ETL workflows for tabular data
* Deployment infrastructure

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LjtBbMZs5-FqTGcRjw80ZBlHhfd_LT2z)

#### GitHub repos
* [Transporter](https://github.com/databiosphere/transporter) - Bulk file-transfer system
* [Ingest Deploy](https://github.com/broadinstitute/dsp-ingest-deploy) - Terraform and Kubernetes configuration for deploying ingest components into GCP
* [Monster ETL](https://github.com/broadinstitute/monster-etl) - Apache Beam workflows for ingest
* [GDR Ingest](https://github.com/broadinstitute/gdr-ingest) - Initial experiments at ingesting ENCODE data (archived)
* [Kafka Deploy](https://github.com/broadinstitute/emerald-kubernetes-kafka) - Initial experiments at managing Kafka and Zookeeper in Kubernetes (archived)

### BRAIN Initiative
Scientific pipelines and infrastructure for processing BRAIN data in [Terra](https://app.terra.bio).

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LnYdg2RwGJ84aVbFdLFjK9qrT-nKqcJu)

#### GitHub repos
* [CEMBA](https://github.com/biccn/cemba) - Analysis pipeline for single nucleus methylation data
* [Terra Import Builder](https://github.com/BICCN/terra-import-builder) - Cloud function converting NeMO payloads into Terra import URLs
