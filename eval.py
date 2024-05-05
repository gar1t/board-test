import sys
import timeit

import gage

FACTOR = 500_000

perf = 10_000 * timeit.timeit()
value_to_org = FACTOR / perf

gage.write_summary(
    metrics={
        "perf": perf,
        "value_to_org": value_to_org,
    },
    attributes={
        "platform": sys.platform,
        "value_to_org_version": "v1",
    },
)
