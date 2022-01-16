# File Download Demo
This repository contains three example apps for authenticated file downloads
using Django.

TODO: add blog post.

## Setup
- clone this repository
- download [Caddy](https://caddyserver.com)
- copy and paste configuration from `docs/caddy.md` in `CaddyFile` located in the same directory as Caddy
- run caddy
- install requirements from `requirements.txt`

Before running the project using `python manage.py runserver` read on how to
configure it. 

### Configuration
Depending on which version you want to test you will need to set environment
variables.

Adjust the media path Caddy is serving files from - line 12 in `caddy.md`

**Django native**
```
VERSION=DJANGO
```

**Caddy**
```
VERSION=CADDY
```

**S3**
```
VERSION=S3
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
```

## License
MIT
