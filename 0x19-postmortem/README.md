**Postmortem: The Great Cache Catastrophe**

**Issue Summary:**
- _Duration_: August 20, 2024, 14:30 - 15:45 GMT
- Impact: Our API service experienced a significant outage, causing a 50% degradation in response times. Users faced intermittent failures and slow responses, with approximately 40% of our active user base affected.
- _Root Cause_: A configuration error in the cache server led to an overload, causing a cascading failure that affected the APIs performance.

**Timeline:**
- _14:30 GMT_: Issue detected by automated monitoring systems; alerts triggered indicating high latency and increased error rates in the API service.
- _14:35 GMT_: Initial investigation began. Engineers noted the spike in latency but found no issues with the application servers or databases.
- _14:45 GMT_: First assumption was a potential database bottleneck; efforts shifted to database performance tuning.
- _14:55 GMT_: Customer complaints escalated the issue; feedback confirmed that the problem was widespread and not isolated.
- _15:05 GMT_: Investigation turned towards the cache server after examining the infrastructure; it was found that cache utilization was at 100% and not serving requests properly.
- _15:15 GMT_: The issue was identified as a misconfigured cache eviction policy. Cache was set to retain more data than it could handle, causing overload.
- _15:30 GMT_: Cache configuration was corrected, and the system was gradually restored to normal operation.
- _15:45 GMT_: Full service recovery confirmed. Monitoring continued to ensure stability.

**Root Cause and Resolution:**
- _Cause_: The cache server configuration was incorrectly set to retain excessive data due to a recent update in the eviction policy settings. This resulted in cache overflow, causing significant delays and failures in the API responses as the system struggled to serve requests from an overloaded cache.
- _Resolution_: The cache eviction policy was corrected to the proper configuration. The cache server was cleared and restarted to ensure it was operating under optimal conditions. This allowed the system to return to normal performance levels.

**Corrective and Preventative Measures:**
1. Immediate Actions:
- _Patch Cache Configuration_: Reconfigure the cache eviction policy to align with optimal performance settings.
- _Reboot Cache Servers_: Clear and restart cache servers to remove any stale data and apply new configurations.
2. Preventative Actions:
- _Enhanced Monitoring_: Implement more granular monitoring on cache utilization and eviction rates. Set up alerts for cache hit/miss ratios and performance anomalies.
- _Configuration Review_: Establish a review process for configuration changes involving critical infrastructure components. Ensure changes are tested in a staging environment before deployment.
- _Training and Documentation_: Improve documentation around cache configurations and ensure engineering teams are trained on the impact of configuration changes.
- _Incident Simulation_: Conduct regular simulations and drills to ensure quick identification and resolution of similar issues in the future.
