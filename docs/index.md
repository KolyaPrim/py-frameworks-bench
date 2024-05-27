---
layout: home
list_title: Archive
description: Python frameworks benchmarks
---

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>

This is a simple benchmark for python async frameworks. Almost all of the
frameworks are ASGI-compatible (aiohttp and tornado are exceptions on the
moment).

The objective of the benchmark is not testing deployment (like uvicorn vs
hypercorn and etc) or database (ORM, drivers) but instead test the frameworks
itself. The benchmark checks request parsing (body, headers, formdata,
queries), routing, responses.

* Read about the benchmark: [The Methodic](methodic.md)
* Check complete results for the latest benchmark here: [Results (2024-05-27)](_posts/2024-05-27-results.md)

[![benchmarks](https://github.com/klen/py-frameworks-bench/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/klen/py-frameworks-bench/actions/workflows/benchmarks.yml)
[![tests](https://github.com/klen/py-frameworks-bench/actions/workflows/tests.yml/badge.svg)](https://github.com/klen/py-frameworks-bench/actions/workflows/tests.yml)

## Combined results

<canvas id="chart" style="margin-bottom: 2em"></canvas>
<script>
    var ctx = document.getElementById('chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['blacksheep2-msg','blacksheep2','blacksheep','starlette','fastapi','django',],
            datasets: [
                {
                    label: '# of requests',
                    data: ['589155','561735','556590','391260','279990','50295',],
                    backgroundColor: [
                        '#4E79A7', '#A0CBE8', '#F28E2B', '#FFBE7D', '#59A14F', '#8CD17D', '#B6992D', '#F1CE63', '#499894', '#86BCB6', '#E15759', '#FF9D9A', '#79706E', '#BAB0AC', '#D37295', '#FABFD2', '#B07AA1', '#D4A6C8', '#9D7660', '#D7B5A6',
                    ]
                },
            ]
        }
    });
</script>

Sorted by sum of completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep2-msg](https://pypi.org/project/blacksheep2-msg/) `` | 589155 | 6.73 | 6.79 | 6.87
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 561735 | 7.1 | 7.16 | 7.18
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 556590 | 6.97 | 7.03 | 7.01
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 391260 | 14.73 | 14.84 | 14.8
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 279990 | 17.13 | 17.24 | 17.33
| [django](https://pypi.org/project/django/) `4.0.3` | 50295 | 55.0 | 56.88 | 58.34


More details: [Results (2024-05-27)](_posts/2024-05-27-results.md)