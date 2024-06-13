import sys
import timeit

from gage_summary import write_summary

FACTOR = 500_000

perf = 10_000 * timeit.timeit()
value_to_org = FACTOR / perf

write_summary(
    metrics={
        "perf": perf,
        "value_to_org": value_to_org,
    },
    attributes={
        "platform": sys.platform,
        "value_to_org_version": "v1",
    },
)
