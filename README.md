# Async Python Web Frameworks comparison

https://klen.github.io/py-frameworks-bench/
----------
#### Updated: 2024-05-27

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
* [The Results](#the-results-2024-05-27)
    * [Accept a request and return HTML response with a custom dynamic header](#html)
    * [Parse path params, query string, JSON body and return a json response](#api)
    * [Parse uploaded file, store it on disk and return a text response](#upload)
    * [Composite stats ](#composite)



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep2-msg%22%2C%22blacksheep2%22%2C%22blacksheep%22%2C%22starlette%22%2C%22fastapi%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B589155%2C561735%2C556590%2C391260%2C279990%2C50295%5D%7D%5D%7D%7D' />

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


## The Results (2024-05-27)

<h3 id="html"> Accept a request and return HTML response with a custom dynamic header</h3>
<details open>
<summary> The test simulates just a single HTML response. </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 21228 | 3.00 | 3.02 | 3.14
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 20660 | 3.09 | 3.11 | 3.09
| [blacksheep2-msg](https://pypi.org/project/blacksheep2-msg/) `` | 20491 | 3.08 | 3.11 | 3.35
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 15339 | 4.11 | 4.14 | 4.18
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 10224 | 6.20 | 6.24 | 6.59
| [django](https://pypi.org/project/django/) `4.0.3` | 1265 | 47.69 | 49.21 | 51.01


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep2-msg](https://pypi.org/project/blacksheep2-msg/) `` | 13704 | 4.65 | 4.70 | 4.67
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 11212 | 5.69 | 5.73 | 5.71
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 11164 | 5.72 | 5.76 | 5.73
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 8805 | 7.25 | 7.29 | 7.27
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 6657 | 9.57 | 9.67 | 9.61
| [django](https://pypi.org/project/django/) `4.0.3` | 1164 | 52.17 | 53.52 | 54.89

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 5234 | 12.13 | 12.25 | 12.23
| [blacksheep2-msg](https://pypi.org/project/blacksheep2-msg/) `` | 5082 | 12.46 | 12.56 | 12.59
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 5057 | 12.58 | 12.69 | 12.66
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 1940 | 32.84 | 33.08 | 32.96
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 1785 | 35.62 | 35.82 | 35.80
| [django](https://pypi.org/project/django/) `4.0.3` | 924 | 65.14 | 67.91 | 69.11


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep2-msg](https://pypi.org/project/blacksheep2-msg/) `` | 589155 | 6.73 | 6.79 | 6.87
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 561735 | 7.1 | 7.16 | 7.18
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 556590 | 6.97 | 7.03 | 7.01
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 391260 | 14.73 | 14.84 | 14.8
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 279990 | 17.13 | 17.24 | 17.33
| [django](https://pypi.org/project/django/) `4.0.3` | 50295 | 55.0 | 56.88 | 58.34

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)