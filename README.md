# Async Python Web Frameworks comparison

https://klen.github.io/py-frameworks-bench/
----------
#### Updated: 2024-05-12

[![benchmarks](https://github.com/klen/py-frameworks-bench/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/klen/py-frameworks-bench/actions/workflows/benchmarks.yml)
[![tests](https://github.com/klen/py-frameworks-bench/actions/workflows/tests.yml/badge.svg)](https://github.com/klen/py-frameworks-bench/actions/workflows/tests.yml)

----------

This is a simple benchmark for python async frameworks. Almost all of the
frameworks are ASGI-compatible (aiohttp and tornado are exceptions on the
moment).

The objective of the benchmark is not testing deployment (like uvicorn vs
hypercorn and etc) or database (ORM, drivers) but instead test the frameworks
itself. The benchmark checks request parsing (body, headers, formdata,
queries), routing, responses.

## Table of contents

* [The Methodic](#the-methodic)
* [The Results](#the-results-2024-05-12)
    * [Accept a request and return HTML response with a custom dynamic header](#html)
    * [Parse path params, query string, JSON body and return a json response](#api)
    * [Parse uploaded file, store it on disk and return a text response](#upload)
    * [Composite stats ](#composite)



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep%22%2C%22blacksheep2%22%2C%22starlette%22%2C%22fastapi%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B557670%2C544875%2C388110%2C281325%2C51795%5D%7D%5D%7D%7D' />

## The Methodic

The benchmark runs as a [Github Action](https://github.com/features/actions).
According to the [github
documentation](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
the hardware specification for the runs is:

* 2-core vCPU (Intel® Xeon® Platinum 8272CL (Cascade Lake), Intel® Xeon® 8171M 2.1GHz (Skylake))
* 7 GB of RAM memory
* 14 GB of SSD disk space
* OS Ubuntu 20.04

[ASGI](https://asgi.readthedocs.io/en/latest/) apps are running from docker using the gunicorn/uvicorn command:

    gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 app:app

Applications' source code can be found
[here](https://github.com/klen/py-frameworks-bench/tree/develop/frameworks).

Results received with WRK utility using the params:

    wrk -d15s -t4 -c64 [URL]

The benchmark has a three kind of tests:

1. "Simple" test: accept a request and return HTML response with custom dynamic
   header. The test simulates just a single HTML response.

2. "API" test: Check headers, parse path params, query string, JSON body and return a json
   response. The test simulates an JSON REST API.

3. "Upload" test: accept an uploaded file and store it on disk. The test
   simulates multipart formdata processing and work with files.


## The Results (2024-05-12)

<h3 id="html"> Accept a request and return HTML response with a custom dynamic header</h3>
<details open>
<summary> The test simulates just a single HTML response. </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 20634 | 3.09 | 3.12 | 3.10
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 19596 | 3.12 | 3.32 | 3.35
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 15076 | 4.13 | 4.18 | 4.25
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 10277 | 6.18 | 6.22 | 6.50
| [django](https://pypi.org/project/django/) `4.0.3` | 1304 | 45.96 | 47.00 | 49.66


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 11462 | 5.58 | 5.62 | 5.58
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 11235 | 5.66 | 5.70 | 5.70
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 8850 | 7.20 | 7.24 | 7.23
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 6669 | 9.57 | 9.62 | 9.60
| [django](https://pypi.org/project/django/) `4.0.3` | 1198 | 50.93 | 52.21 | 53.37

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 5309 | 11.97 | 12.05 | 12.06
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 5267 | 12.10 | 12.17 | 12.15
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 1948 | 32.57 | 32.72 | 32.82
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 1809 | 35.20 | 35.33 | 35.37
| [django](https://pypi.org/project/django/) `4.0.3` | 951 | 63.91 | 65.47 | 67.17


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 557670 | 6.91 | 6.96 | 6.95
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 544875 | 6.93 | 7.04 | 7.03
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 388110 | 14.63 | 14.71 | 14.77
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 281325 | 16.98 | 17.06 | 17.16
| [django](https://pypi.org/project/django/) `4.0.3` | 51795 | 53.6 | 54.89 | 56.73

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)