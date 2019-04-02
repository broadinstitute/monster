# The Monster Team
[![Monster Slack](https://img.shields.io/badge/Slack%20Channel-%23monster-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CCAU5L6LV/)
[![Monster CI Slack](https://img.shields.io/badge/Slack%20Channel-%23monster--ci-blue.svg?style=flat)](https://broadinstitute.slack.com/messages/CFXEDUUP5/)

## People

| Name | Role | GitHub |
| --- | --- | --- | --- | --- |
| Ben Carlin | Software Engineer | @benjamincarlin |
| Dan Moran | Tech Lead | @danxmoran |
| Emily Munro-Ludders | Scrum Master | |
| Jeff Korte | Product Owner | @JeffKorte |
| Kathy Reinold | Data Modeler | @kreinold |

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

### Data Ingest
ETL workflows and infrastructure for moving data into the [Jade Data Repository](https://github.com/databiosphere/jade-data-repo).

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LjtBbMZs5-FqTGcRjw80ZBlHhfd_LT2z)

#### GitHub repos
* [Transporter](https://github.com/databiosphere/transporter) - bulk file-transfer system
* [Transporter Deploy](https://github.com/broadinstitute/transporter-deploy) - Kubernetes configuration for deploying Transporter
* [Monster ETL](https://github.com/broadinstitute/monster-etl) - Apache Beam workflows for ingest
* [GDR Ingest](https://github.com/broadinstitute/gdr-ingest) - Initial experiments at ingesting ENCODE data (archived)

### BRAIN Initiative
Scientific pipelines and infrastructure for processing BRAIN data in [Terra](https://app.terra.bio).

#### Documentation
* [Google Docs](https://drive.google.com/drive/folders/1LnYdg2RwGJ84aVbFdLFjK9qrT-nKqcJu)

#### GitHub repos
* [CEMBA](https://github.com/biccn/cemba) - Analysis pipeline for single nucleus methylation data
* [Terra Import Builder](https://github.com/BICCN/terra-import-builder) - Cloud function converting NeMO payloads into Terra import URLs
