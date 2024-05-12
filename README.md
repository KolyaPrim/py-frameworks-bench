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



<img src='https://quickchart.io/chart?width=800&height=400&c=%7Btype%3A%22bar%22%2Cdata%3A%7Blabels%3A%5B%22blacksheep2%22%2C%22blacksheep%22%2C%22starlette%22%2C%22fastapi%22%2C%22django%22%5D%2Cdatasets%3A%5B%7Blabel%3A%22num%20of%20req%22%2Cdata%3A%5B550485%2C548355%2C384270%2C283425%2C51015%5D%7D%5D%7D%7D' />

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
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 20534 | 3.09 | 3.12 | 3.48
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 20352 | 3.14 | 3.16 | 3.14
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 14888 | 4.16 | 4.21 | 4.30
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 10377 | 6.09 | 6.12 | 6.43
| [django](https://pypi.org/project/django/) `4.0.3` | 1285 | 46.81 | 47.98 | 50.37


</details>

<h3 id="api"> Parse path params, query string, JSON body and return a json response</h3>
<details open>
<summary> The test simulates a simple JSON REST API endpoint.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 11078 | 5.75 | 5.79 | 5.78
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 10967 | 5.81 | 5.85 | 5.84
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 8795 | 7.26 | 7.30 | 7.28
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 6712 | 9.48 | 9.52 | 9.53
| [django](https://pypi.org/project/django/) `4.0.3` | 1187 | 51.49 | 52.69 | 53.86

</details>

<h3 id="upload"> Parse uploaded file, store it on disk and return a text response</h3>
<details open>
<summary> The test simulates multipart formdata processing and work with files.  </summary>

Sorted by max req/s

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 5238 | 12.02 | 12.11 | 12.22
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 5087 | 12.48 | 12.57 | 12.58
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 1935 | 32.88 | 33.02 | 33.06
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 1806 | 35.18 | 35.37 | 35.42
| [django](https://pypi.org/project/django/) `4.0.3` | 929 | 64.16 | 67.29 | 68.64


</details>

<h3 id="composite"> Composite stats </h3>
<details open>
<summary> Combined benchmarks results</summary>

Sorted by completed requests

| Framework | Requests completed | Avg Latency 50% (ms) | Avg Latency 75% (ms) | Avg Latency (ms) |
| --------- | -----------------: | -------------------: | -------------------: | ---------------: |
| [blacksheep2](https://pypi.org/project/blacksheep2/) `` | 550485 | 7.11 | 7.16 | 7.28
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.18` | 548355 | 6.99 | 7.04 | 7.07
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 384270 | 14.77 | 14.84 | 14.88
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 283425 | 16.92 | 17.0 | 17.13
| [django](https://pypi.org/project/django/) `4.0.3` | 51015 | 54.15 | 55.99 | 57.62

</details>

## Conclusion

Nothing here, just some measures for you.

## License

Licensed under a MIT license (See LICENSE file)