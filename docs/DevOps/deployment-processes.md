# Deployment Processes

[Informative link](https://blog.turbinelabs.io/deploy-not-equal-release-part-one-4724bc1e726b)


## Deploy vs Release

Four phases of code deployment,

```
Build -> Test -> Deploy -> Release
```

Deploy might not be the same as release. 

There are different types of deployment processes, Canary and Blue/Green.

## Canary Deployment (Deploy == Release)

- In a clustered environment, you might first release-in-place to just one of your instances. This practice, most commonly referred to as **canary**, can mitigate some risk, the percentage of your traffic exposed to deploy and release risk is equal to the number of instances with the new version of your service divided by the total number of instances in your service’s cluster.

## Blue/Green (Deploy != Release)

- A **blue/green** deploy involves deploying your service’s new version alongside the released version in production. You may use dedicated hardware or VMs for each *color* and alternate subsequent deploys between them, or you may use containers and an orchestration framework like Kubernetes to manage ephemeral processes. Regardless, the key here is that once your new (green) version is deployed, it is not released — it does not start responding to production requests. Those are still being handled by the existing, known-good (blue) version of the service.
Release in a blue/green setup usually involves making changes at the load balancer that add hosts running the new version and remove hosts running the known-good version. While this approach is much better than release-in-place, it has some limitations, particularly as it relates to release risk.

- If your deployment is hung up in a crash loop backoff or if the database secret is wrong and the newly-deployed service can’t connect, you’re not under any pressure to do anything. Your team can diagnose the problem.

- When deployment is separate from release, you can run automated health checks and integration tests against the newly-deployed version before exposing any production traffic to it. 

- If we agree that every release is a test in production (and whether we agree or not, they are), then what we really want is to segment our production requests using pattern-matching rules and dynamically route an arbitrary percentage of that traffic to any version of our service. This is a powerful concept that forms the foundation of sophisticated release workflows like *dogfooding*, *incremental release*, *rollbacks*, and *dark traffic*.

    - **Dogfooding** is a popular technique of releasing a new version of a service to employees only. With a powerful release service in place, you can write rules like “send 50% of internal employee traffic to instances where version=x.x” In my career, dogfooding in production has caught more embarrassing bugs than I care to admit.

    - **Incremental Release** is the process of starting with some small percentage of production requests routed to a new version of a service while monitoring the performance of those requests — errors, latency, success rate, and so on, against the previous production release. When you’re confident the new version doesn’t exhibit any unexpected behavior relative to the known-good version, you can increase the percentage and repeat the process until you’ve reached 100%.

    - **Rollback** with a release-as-a-continuum system is simply a function of routing production requests back to instances that are still running the last known-good version. It’s fast, low-risk, and like release itself, can be done in a fine-grained, targeted fashion.

    - **Dark Traffic** is a powerful technique where your release system duplicates production requests and sends one copy to the known-good, “light” version of your service and another to a new, “dark” version. The “light” version is responsible for actually responding to the user’s request. The “dark” version handles the request, but its response is ignored. This is particularly effective when you need to test new software under production load.

> A sophisticated release system does more than mitigate deploy risk—it directly improves your product velocity and user experience.