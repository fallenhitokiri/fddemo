# Configuration

```
:8080 {
    log {
        format single_field common_log
    }

    reverse_proxy 127.0.0.1:8000 {
        @accel header X-Accel-Redirect *
        handle_response @accel {
            root * /home/timo/fddemo/src/media/
            rewrite {http.reverse_proxy.header.X-Accel-Redirect}
            file_server
        }
    }
}
```