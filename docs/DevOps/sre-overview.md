# SRE Overview

As quoted in the article and SRE book, 

## Why
- At their core, the development teams want to launch new features and see them adopted by users. 
- At their core, the ops teams want to make sure the service doesn’t break while they are holding the pager. 
- Because most outages are caused by some kind of change—a new configuration, a new feature launch, or a new type of user traffic—the two teams’ goals are fundamentally in tension.

## How-to
- SREs must see the system as a whole and treat its interconnections with as much attention and respect as the components themselves.
- SREs are software engineers running the products and creating systems to accomplish the work that would otherwise be performed, often manually, by sysadmins.

## Seven Principles
- Operations is a software problem 
    * Use software engineering approaches to solve that problem (doing operations well) 
- Manage by Service Level Objectives (SLOs)
    * The product team and the SRE team should select an appropriate availability target for the service and its user base, and the service is managed to that SLO. 
    * 100% availability is not the goal. 
    * Collabaration from business is required.
- Work to minimize toil
    * Toil is tedious, manual, work. If a machine can perform a desired operation, then a machine often should.
- Automate this year’s job away
    * Determining what to automate, under what conditions, and how to automate it.
- Move fast by reducing the cost of failure
    * SREs are specifically charged with improving undesirably late problem discovery.
- Share ownership with developers
    * Product development and SRE teams should have a holistic view of the stack—the frontend, backend, libraries, storage, kernels, and physical machine. 
    * No team should own single components.
- Use the same tooling, regardless of function or job title
    * There is no good way to manage a service that has one tool for the SREs and another for the product developers. 

## DevOps vs SRE
- DevOps is in some sense a wider philosophy and culture. Because it effects wider change than does SRE, DevOps is more context-sensitive.
- SRE has relatively narrowly defined responsibilities and its remit is generally service-oriented (and end-user-oriented) rather than whole-business-oriented. 


## Source 
- [Reference Link](https://www.oreilly.com/ideas/site-reliability-engineering-sre-a-simple-overview)