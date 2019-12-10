# Notes on Google SRE

## Chapter 1: Introduction

- **Traditional Approach**
    * Assemble existing components and deploy to produce a service
    * Respond to events and updates as they occur
    * Pros
        - Standard procedure
        - Availability of existing Software 
    * Cons
        - Manual intervention for event handling 
        - Ops is at odds with dev
- **Google's Approach - SRE**
    * Software engineers work on ops
    * Automate tasks
    * Cost effective
    * dev and ops aren't at odds
---
- **Tenets** - SRE team is responsible for:
    - latency
    - performance
    - efficiency
    - change management
    - monitoring
    - emergency response
    - capacity planning

- **Durable focus on Engineering**
    - 50% ops cap -> extra ops work is redirected to product teams on overflow.
    - Provides feedback mechanism to product teams as well as keeps load down.
    - Target max 2 events per 8-12 hour on-call shift.
    - Postmortems for all serious incidents, even if they didn’t trigger a page.
    - Blameless postmortems.

- Move fast **without breaking SLO**
    - Error budget can be spent on anything: launching features, etc.
    - Error budget allows for discussion about how phased rollouts and 1% experiments can maintain tolerable levels of errors
    - SRE and product devs are incentive aligned to spend the error budget to get maximum feature velocity
    - Build confidence through simulated disasters and other testing

- **Monitoring**
    - Automate response when alerts are triggered
    - Never require a human to interpret any part of the alerting domain
    - Three valid kinds of monitoring output
        - Alerts: human needs to take action immediately
        - Tickets: human needs to take action eventually
        - Logging: no action needed

- **Emergency response**
    - Reliability is a function of MTTF (mean-time-to-failure) and MTTR (mean-time-to-recovery)
    - Systems that don’t require humans to respond will have higher availability due to lower MTTR
    - Having a “playbook” produces 3x lower MTTR

- **Change management**
    - 70% of outages due to changes in a live system. 
    - Mitigation:
        - Implement progressive rollouts
        - Monitoring
        - Rollback
    - Avoid human interaction on repetitive tasks

- **Provisioning**
    - Adding capacity is riskier than load shifting as it involves making significant changes to existing systems
    - Expensive enough that it should be done quickly and only when necessary

- **Efficiency and performance**
    - Load slows down systems
    - SREs provision to meet capacity target with a specific response time goal
    - Efficiency == costs

## Chapter 2: Production environment at Google

## Chapter 3: Embracing risk

- **Managing risk**
    - Reliability isn’t linear in cost. It can easily cost 100x more to get one additional increment of reliability
        - Cost associated with redundant equipment
        - Cost of building features for reliability as opposed to “normal” features
    - *Goal*: make systems reliable enough, but not too reliable!

- **Measuring service risk**
    - Standard practice: identify metric to represent property of system to optimize
    - Possible metric = uptime / (uptime + downtime)
    - Aggregate availability = successful requests / total requests
        - Not all requests are equal, but aggregate availability is an ok first order approximation
    - Usually set quarterly targets

- **Risk tolerance of services**
    - Usually not objectively obvious
    - SREs work with product owners to translate business objectives into explicit objectives

- **Identifying risk tolerance of infrastructure services**
    - Target availability. Running ex: Bigtable
        - Some consumer services serve data directly from Bigtable -- need low latency and high reliability
        - Some teams use bigtable as a backing store for offline analysis -- care more about throughput than reliability
    - Cost
        - Too expensive to meet all needs generically. Ex: Bigtable instance
            - Low-latency Bigtable user wants low queue depth
            - Throughput oriented Bigtable user wants moderate to high queue depth
            - Success and failure are diametrically opposed in these two cases!
    - Solution
        - Partition infrastructure and offer different levels of service
        - In addition, allows service to externalize the cost of providing different levels of service (e.g., expect latency oriented service to be more expensive than throughput oriented service)

## Chapter 4: Service Level Objectives

- Ex: Chubby planned outages
    - Google found that Chubby was consistently over its SLO, and that global Chubby outages would cause unusually bad outages at Google
    - Chubby was so reliable that teams were incorrectly assuming that it would never be down and failing to design systems that account for failures in Chubby
    - Solution: take Chubby down globally when it’s too far above its SLO for a quarter to “show” teams that Chubby can go down

- What do you and your users care about?
    - Too many indicators: hard to pay attention
    - Too few indicators: might ignore important behavior
    - Different classes of services should have different indicators
        - User-facing: availability, latency, throughput
        - Storage: latency, availability, durability
        - Big data: throughput, end-to-end latency
    - All systems care about correctness

- **Collecting indicators**
    - Can often do naturally from server, but client-side metrics sometimes needed.

- **Aggregation**
    - Use distributions and not averages
    - User studies show that people usually prefer slower average with better tail latency
    - Standardize on common defs, e.g., average over 1 minute, average over tasks in cluster, etc.
        - Can have exceptions, but having reasonable defaults makes things easier

- **Choosing targets**
    - Don’t pick target based on current performance
        - Current performance may require heroic effort
    - Keep it simple
    - Avoid absolutes
        - Unreasonable to talk about “infinite” scale or “always” available
    - Minimize number of SLOs
    - Perfection can wait
        - Can always redefine SLOs over time
    - SLOs set expectations
        - Keep a safety margin (internal SLOs can be defined more loosely than external SLOs)
    - Don’t overachieve
        - See Chubby example, above
        - Another example is making sure that the system isn’t too fast under light loads

## Chapter 5: Eliminating Toil

- All of these tasks can be useful in eliminating toil
    - Tasks that are not just “work I don’t want to do”
    - Tasks that are Repetitive
    - Tasks that can be automated
- No enduring value
- O(n) with service growth
- If Toil > 50%, it is a sign that the manager should spread toil load more evenly

## Chapter 6: Monitoring distributed systems

- Monitoring can be useful to 
    - Analyze long-term trends
    - Compare over time or do experiments
    - Alerting
    - Building dashboards
    - Debugging

- Setting reasonable expectations
    - Monitoring is non-trivial
    - Number of engineers has decreased over time due to improvements in tooling/libs/centralized monitoring infra
    - General trend towards simpler/faster monitoring systems with better tools
    - Limited success with complex dependency hierarchies (e.g., “if DB slow, alert for DB, otherwise alert for website”).
        - Used mostly for very stable parts of system
    - Rules that generate alerts for humans should be simple to understand and represent a clear failure

- Four golden signals
    - Latency
    - Traffic
    - Errors
    - Saturation

## Chapter 7: Evolution of automation at Google

    Automation is a force multiplier, not a solution for all issues.

- Value of automation
    - Consistency
    - Extensibility
    - MTTR
    - Faster non-repair actions
    - Time savings

