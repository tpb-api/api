TPB API
===

Search TPB via an HTTP API. Online service [available here](https://api3-tpb.rhcloud.com/torrents/).

GET /torrents
======

Accepted content-types: `html` and `json`

- __Parameters__:

    - `keywords`
    - `page`
    - `sort` 

- __Results___:

    - `title`
    - `url`
    - `category`
    - `sub_category`
    - `magnet_link`
    - `torrent_link`

Todo
======

- Magnet to Torrent when `torrent_link` is `null`
- `clean_title` in the result
- `imdb_id` ?
- `quality` ?